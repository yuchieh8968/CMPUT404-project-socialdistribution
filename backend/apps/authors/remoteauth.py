from .models import AllowedRemotes
import base64


# https://stackoverflow.com/questions/38016684/accessing-username-and-password-in-django-request-header-returns-none
def get_username_password(request):
    if 'HTTP_AUTHORIZATION' in request.META.keys():
        auth_header = request.META['HTTP_AUTHORIZATION']
        encoded_credentials = auth_header.split(' ')[1]  # Removes "Basic " to isolate credentials
        decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8").split(':')
        username = decoded_credentials[0]
        password = decoded_credentials[1]
        # print(f"username = {username}")
        # print(f"password = {password}")
    else:
        username = None
        password = None
    return username, password


def RemoteAuth(request):
    """
    returns True or False, repending on if request came from a valid remote
    """
    username, password = get_username_password(request=request)
    if username is None or password is None:
        return False
    try:
        remote = AllowedRemotes.objects.get(username=username)
    except Exception as e:
        return False

    if remote is None:
        return False
    
    if remote.password == password:
        return True
    
    return False