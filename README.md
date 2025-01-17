# Student Management System

A web application for managing students, courses, reviews and grades built with Python, aiohttp, and PostgreSQL.

## Features

- Student management (view, add, list students)
- Course management (view courses and enrollment)
- Course reviews and ratings
- Student grade evaluation
- User authentication and authorization
- Admin and regular user roles
- CSRF protection
- Session handling

## Technical Stack

- **Backend**: Python 3.x with aiohttp web framework
- **Database**: PostgreSQL 
- **Session Store**: Redis
- **Frontend**: Materialize CSS framework, jQuery
- **Templates**: Jinja2
- **Containerization**: Docker & Docker Compose

## Project Structure

```
├── config/               # Configuration files
├── migrations/          # Database migrations
├── sqli/               # Main application package
│   ├── dao/           # Data Access Objects
│   ├── schema/        # Data schemas and forms
│   ├── services/      # Database and Redis services
│   ├── static/        # Static assets (CSS, JS)
│   ├── templates/     # Jinja2 templates
│   ├── utils/         # Utility functions
│   ├── app.py         # Application initialization
│   ├── middlewares.py # Middleware functions
│   ├── routes.py      # URL routing
│   └── views.py       # View handlers
├── docker-compose.yml  # Docker compose configuration
├── Dockerfile.app     # Application Dockerfile
├── Dockerfile.db      # Database Dockerfile  
├── requirements.txt   # Python dependencies
└── run.py            # Application entry point
```

## Getting Started

1. Clone the repository
2. Install Docker and Docker Compose
3. Build and start containers:
```bash
docker-compose up --build
```

4. Initialize database:
```bash
./recreate.sh
```

5. Access the application at http://localhost:8080

## Development

- Use `dev.yaml` in config directory for development settings
- Database migrations are in `migrations/` directory
- Frontend assets are in `sqli/static/`
- Templates are in `sqli/templates/`

## Functionality

- **Students**: View student profiles, grades and enrollment
- **Courses**: Browse courses, view details and enrollment
- **Reviews**: Submit and view course reviews
- **Grades**: Evaluate student performance
- **Authentication**: Login/logout functionality
- **Authorization**: Admin and regular user access control

## API Overview

- `/` - Home page
- `/students` - List students
- `/students/{id}` - Student details
- `/courses` - List courses  
- `/courses/{id}` - Course details
- `/review` - Submit course review
- `/evaluate` - Grade student performance

## Security Features

- Session-based authentication
- CSRF protection
- Error handling pages
- Admin role restrictions
- Input validation

## License

This project is licensed under the MIT License - see the LICENSE file for details.
