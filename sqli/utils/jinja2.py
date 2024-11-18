from uuid import uuid4

from aiohttp_session import get_session

from sqli.utils.auth import get_auth_user


async def csrf_processor(request):
    """Generates a CSRF token and provides a function to retrieve it.
    
    Args:
        request (Request): The incoming request object.
    
    Returns:
        dict: A dictionary containing a 'csrf_token' function that generates or retrieves a CSRF token.
    
    """
    session = await get_session(request)

    def csrf_token():
        if '_csrf_token' not in session:
            session['_csrf_token'] = uuid4().hex
        return session['_csrf_token']

    return {'csrf_token': csrf_token}


async def auth_user_processor(request):
    """Asynchronously authenticates a user based on the provided request.
    
    Args:
        request: The incoming request object containing authentication information.
    
    Returns:
        dict: A dictionary containing the authenticated user information.
            'auth_user': The authenticated user object.
    """
    auth_user = await get_auth_user(request)
    return {'auth_user': auth_user}
