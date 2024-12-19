from typing import Optional, NamedTuple

from aiopg.connection import Connection


class Student(NamedTuple):
    id: int
    name: str

    @classmethod
    def from_raw(cls, raw: tuple):
        return cls(*raw) if raw else None

    @staticmethod
    async def get(conn: Connection, id_: int):
        async with conn.cursor() as cur:
            await cur.execute(
                'SELECT id, name FROM students WHERE id = %s',
                (id_,),
            )
            r = await cur.fetchone()
            return Student.from_raw(r)

    @staticmethod
    async def get_many(conn: Connection, limit: Optional[int] = None,
                       offset: Optional[int] = None):
        """Safely retrieves multiple students with optional pagination using SQL injection safe parameterized queries.
        
        This implementation uses proper SQL parameter binding with psycopg2's %(param)s style placeholders
        and a separate params dictionary. This approach prevents SQL injection by:
        1. Ensuring parameters are properly escaped and quoted by the database driver
        2. Keeping the query structure separate from the parameter values
        3. Avoiding vulnerable string formatting (like the one used in create() method)
        
        Args:
            conn: Database connection
            limit: Optional maximum number of records to return
            offset: Optional number of records to skip
        """
        q = 'SELECT id, name FROM students'
        params = {}
        # Safely add LIMIT clause using parameterized query - prevents SQL injection
        # by using %(limit)s placeholder instead of unsafe string formatting
        if limit is not None:
            q += ' LIMIT %(limit)s '
            params['limit'] = limit

        # Safely add OFFSET clause using the same secure parameterization approach
        # The params dictionary is passed to execute() which handles proper escaping
        if offset is not None:
            q += ' OFFSET %(offset)s '
            params['offset'] = offset
        async with conn.cursor() as cur:
            await cur.execute(q, params)
            results = await cur.fetchall()
            return [Student.from_raw(r) for r in results]

    @staticmethod
    async def create(conn: Connection, name: str):
        q = ("INSERT INTO students (name) "
             "VALUES ('%(name)s')" % {'name': name})
        async with conn.cursor() as cur:
            await cur.execute(q)


