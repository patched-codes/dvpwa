from functools import wraps
from typing import Optional

from aiohttp.web import Application
from aiohttp.web_exceptions import HTTPForbidden, HTTPUnauthorized
from aiohttp.web_request import Request
from aiohttp_session import get_session

from sqli.dao.user import User


def authorize(ensure_admin=False):
    """Decorator for authorizing requests and optionally ensuring admin privileges.
    
    Args:
        ensure_admin (bool, optional): If True, requires the user to have admin privileges. Defaults to False.
    
    Returns:
        Callable: A decorator function that wraps the handler with authorization logic.
    
    Raises:
        HTTPUnauthorized: If the user is not authenticated.
        HTTPForbidden: If ensure_admin is True and the user is not an admin.
    """
    def __decorator__(handler):
        @wraps(handler)
        async def __wrapper__(request: Request):
            user = await get_auth_user(request)
            if user is None:
                raise HTTPUnauthorized()
            if ensure_admin and not user.is_admin:
                raise HTTPForbidden()
            return await handler(request)
        return __wrapper__
    return __decorator__


async def get_auth_user(request: Request) -> Optional[User]:
    """Retrieves the authenticated user based on the session information.
    
    Args:
        request (Request): The incoming HTTP request object containing the session and application data.
    
    Returns:
        Optional[User]: The authenticated User object if found, or None if the user is not authenticated or doesn't exist.
    
    Raises:
        None
    
    Notes:
        This method uses the session to get the user_id and then fetches the corresponding User object from the database.
        It requires an active database connection from the application context.
    """
    app: Application = request.app
    session = await get_session(request)
    user_id = session.get('user_id')
    async with app['db'].acquire() as conn:
        return await User.get(conn, user_id)
