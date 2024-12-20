import aiopg
from aiohttp.web import Application


def setup_database(app: Application):
    # create connection to the database
    app.on_startup.append(_init_pg)
    # shutdown db connection on exit
    app.on_cleanup.append(_close_pg)


async def _init_pg(app: Application):
    conf = app['config']['db']

    dsn = (
        'dbname={database} user={user} password={password} host={host} port={port}'
        .format(**conf)
    )
    db = await aiopg.create_pool(dsn)
    app['db'] = db


async def _close_pg(app: Application):
    """Closes the PostgreSQL database connection associated with the application.
    
    Args:
        app (Application): The application instance containing the database connection.
    
    Returns:
        None: This method doesn't return anything.
    
    """
    app['db'].close()
    await app['db'].wait_closed()
