# DVPWA - Damn Vulnerable Python Web Application

[![StandWithUkraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://stand-with-ukraine.pp.ua)

## Description

DVPWA is a deliberately vulnerable web application written in Python, inspired by the famous [DVWA](http://dvwa.co.uk) project and [bobby-tables xkcd comics](https://xkcd.com/327/). The purpose is to implement a real-world-like application with intentional vulnerabilities while maintaining good design principles.

This project was originally used for demonstrating web vulnerabilities during the [Web vulnerabilities](https://www.slideshare.net/OlexandrKovalchuk/web-vulnerabilities-78366279) presentation at EVO Summer Python Lab'17.

## Running

### Docker-compose

DVPWA is packaged into a Docker container with dependencies defined in `docker-compose.yml`. To run:

```bash
docker-compose up
```

Then visit http://localhost:8080 in your browser.

To rebuild the container, use `./recreate.sh` which will delete the old container and create a new one from scratch.

If you need to recreate the database (e.g. after a DROP TABLE):

```bash
docker-compose stop postgres
docker-compose rm  # remove only images you want to recreate
docker-compose up postgres  # recreate container and run
```

### Running Natively

Requirements:
- Python 3.6.2
- PostgreSQL database
- Redis for session storage

Setup steps:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up PostgreSQL database:
```bash
# Create schema
psql -U postgres -d sqli -h localhost -p 5432 -f migrations/000-init-schema.sql

# Load fixtures
psql -U postgres -d sqli -h localhost -p 5432 -f migrations/001-fixtures.sql
```

3. Configure `config/dev.yaml`:
```yaml
db:
  user: postgres
  password: postgres
  host: localhost
  port: 5432
  database: sqli

redis:
  host: localhost
  port: 6379
  db: 0

app:
  host: 0.0.0.0
  port: 8080
```

4. Run the application:
```bash
python run.py
```

Visit http://localhost:8080 in your browser.

## Vulnerabilities

### Session Fixation

**Steps to reproduce:**
1. Open http://localhost:8080
2. Get AIOHTTP_SESSION cookie value from devtools
3. Open incognito tab and set the same cookie value
4. Log in on original tab
5. Refresh incognito tab

**Result:** You're logged in on both tabs with the same session.

**Mitigation:** Rotate session IDs on login/logout and permission changes.

### SQL Injection

**Steps to reproduce:**
1. Log in as `superadmin:superadmin`
2. Go to http://localhost:8080/students/
3. Add student named: `Robert'); DROP TABLE students CASCADE; --`

**Result:** Students table is deleted from database.

**Mitigation:** Use parameterized queries or ORM instead of string concatenation.

### Stored XSS

**Steps to reproduce:**
1. Go to http://localhost:8080/courses/1/review
2. Submit review with HTML/JavaScript content
3. View the course page

**Result:** Injected code executes when viewing reviews.

**Mitigation:** Enable template autoescape and sanitize user input.

### Password Storage Issues

The application uses MD5 hashing for passwords which has several problems:
- Same passwords produce identical hashes
- MD5 is cryptographically weak and easily brute-forced
- No salt is used

**Mitigation:** Use modern password hashing functions like argon2, bcrypt, or pbkdf2.

### Cross-Site Request Forgery

TBA
