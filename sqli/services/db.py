import aiopg
from aiohttp.web import Application


def setup_database(app: Application):
    app.on_startup.append(_init_pg)
    app.on_cleanup.append(_close_pg)


async def _init_pg(app: Application):
    conf = app['config']['db']

    dsn = (
        'dbname={database} user={user} password=<SECRET> host={host} port={port}'
        .format(**conf)
    )
    db = await aiopg.create_pool(dsn)
    app['db'] = db


async def _close_pg(app: Application):
    app['db'].close()
    await app['db'].wait_closed()
