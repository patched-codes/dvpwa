import asyncio
from sqli.services.db import get_connection

async def test_sql_injection():
    # Connect to database
    conn = await get_connection()
    
    try:
        # Test 1: Normal case
        print("Test 1: Normal case")
        await conn.cursor().execute("DELETE FROM students WHERE name = 'Test Student'")
        from sqli.dao.student import Student
        await Student.create(conn, "Test Student")
        print("Created normal student successfully")

        # Test 2: SQL Injection case
        print("\nTest 2: SQL Injection case")
        malicious_input = "'; DELETE FROM students; --"
        try:
            await Student.create(conn, malicious_input)
            print("WARNING: SQL Injection might have succeeded!")
        except Exception as e:
            print(f"SQL Injection caught with error: {str(e)}")

    finally:
        conn.close()

if __name__ == "__main__":
    asyncio.run(test_sql_injection())