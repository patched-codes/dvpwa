async def add_pwd_salt_column(conn):
    """Add pwd_salt column to users table and initialize with random salts."""
    async with conn.cursor() as cur:
        # Add the new column
        await cur.execute(
            'ALTER TABLE users ADD COLUMN pwd_salt VARCHAR(255)'
        )
        
        # Set a default value for existing users to empty string
        # In production, this would require a password reset mechanism
        await cur.execute(
            "UPDATE users SET pwd_salt = ''"
        )