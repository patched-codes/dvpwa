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
        # Using a parameterized query with %s placeholders for SQL injection prevention
        # The placeholder %s will be safely substituted by the database driver
        # rather than using string concatenation or formatting
        q = 'SELECT id, name FROM students'
        
        # Store parameters in a dictionary to maintain mapping between placeholders
        # and their corresponding values. This ensures values are kept separate
        # from the query string until execution time.
        params = {}
        
        if limit is not None:
            q += ' LIMIT %s '  # %s placeholder ensures limit is treated as data, not SQL code
            params['limit'] = limit
        if offset is not None:
            q += ' OFFSET %s '  # %s placeholder ensures offset is treated as data, not SQL code
            params['offset'] = offset
            
        async with conn.cursor() as cur:
            # Convert params to a tuple for safe execution. Using a tuple:
            # 1. Ensures parameter order matches placeholder order
            # 2. Creates an immutable sequence that can't be tampered with
            param_values = tuple(params.values())
            
            # cur.execute handles parameter substitution securely by:
            # 1. Properly escaping special characters
            # 2. Maintaining strict separation between query and data
            # 3. Using the database driver's built-in substitution mechanism
            await cur.execute(q, param_values)
            results = await cur.fetchall()
            return [Student.from_raw(r) for r in results]

    @staticmethod
    async def create(conn: Connection, name: str):
        q = """
        INSERT INTO students (name)
        VALUES (%s)
        """
        async with conn.cursor() as cur:
            await cur.execute(q, (name,))
