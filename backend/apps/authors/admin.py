from django.contrib import admin
from .models import Author, AllowedRemotes

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

    url = forms.URLField(label='URL', widget=forms.URLInput, required=True)
    host = forms.URLField(label='Host', widget=forms.URLInput, required=True)
    displayName = forms.CharField(label='DisplayName', widget=forms.TextInput, required=True)

    class Meta:
        model = Author
        fields = ('id', 'url', 'host', 'displayName')

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

    url = forms.URLField(label='URL', widget=forms.URLInput, required=True)
    host = forms.URLField(label='Host', widget=forms.URLInput, required=True)
    displayName = forms.CharField(label='DisplayName', widget=forms.TextInput, required=True)


    class Meta:
        model = Author
        fields = ('id', 'url', 'host', 'displayName', 'github', 'profileImage', 'is_admin')
        # fields = ('__all__')


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'url', 'host', 'displayName', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('id', 'password')}),
        ('Personal info', {'fields': ('url', 'host', 'displayName', 'github', 'profileImage')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {'fields': ('id', 'password1', 'password2')}),
        ('Personal info', {'fields': ('url', 'host', 'displayName', 'github', 'profileImage')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    search_fields = ('id',)
    ordering = ('id',)
    filter_horizontal = ()


# Register your models here.
admin.site.register(Author, UserAdmin)
admin.site.register(AllowedRemotes)
