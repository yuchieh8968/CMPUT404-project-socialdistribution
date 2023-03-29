from django.contrib import admin
from .models import Author

from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError


class CustomUserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    username = forms.CharField(label='Username', widget=forms.TextInput, required=True)
    displayName = forms.CharField(label='DisplayName', widget=forms.TextInput, required=True)

    class Meta:
        model = Author
        fields = ('username', 'displayName')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    username = forms.CharField(label='Username', widget=forms.TextInput, disabled=True)
    displayName = forms.CharField(label='DisplayName', widget=forms.TextInput, required=True)


    class Meta:
        model = Author
        fields = ('displayName', 'github', 'profileImage', 'is_admin')
        # fields = ('__all__')


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'username', 'displayName', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('displayName', 'github', 'profileImage')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Personal info', {'fields': ('displayName', 'github', 'profileImage')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


# Register your models here.
admin.site.register(Author, UserAdmin)
# admin.site.register(AllowedRemotes)
