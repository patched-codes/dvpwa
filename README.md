# DVPWA: Damn Vulnerable Python Web Application


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Built with Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Docker Compose](https://img.shields.io/badge/Docker_Compose-20232A?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/compose/)

Your Safe Sandbox for Mastering Web Security Vulnerabilities, with a Focus on SQL Injection.

## Table of Contents


*   [Project Description](#project-description)
*   [Key Features](#key-features)
*   [Tech Stack](#tech-stack)
*   [Getting Started](#getting-started)
    *   [Prerequisites](#prerequisites)
    *   [Installation Methods](#installation-methods)
        *   [1. Using Docker (Recommended)](#1-using-docker-recommended)
        *   [2. Local Development Setup (For Contribution/Deeper Dive)](#2-local-development-setup-for-contributiondeeper-dive)
    *   [Troubleshooting (Installation)](#troubleshooting-installation)
*   [How to Use DVPWA](#how-to-use-dvpwa)
    *   [Accessing the Application](#accessing-the-application)
    *   [Exploring Vulnerabilities](#exploring-vulnerabilities)
    *   [Learning Objectives](#learning-objectives)
    *   [Resetting the Application](#resetting-the-application)
    *   [Ethical Hacking Reminder](#ethical-hacking-reminder)
*   [API Reference (Web Endpoints)](#api-reference-web-endpoints)
    *   [`run.py` - Main Application Entry Point](#runpy---main-application-entry-point)
    *   [`sqli/routes.py` - SQL Injection Vulnerability Endpoints](#sqliroutespy---sql-injection-vulnerability-endpoints)
    *   [How to Identify Specific Endpoints](#how-to-identify-specific-endpoints)
*   [Configuration Options and Customization](#configuration-options-and-customization)
*   [Error Handling and Troubleshooting](#error-handling-and-troubleshooting)
*   [Project Structure](#project-structure)
*   [Contributing](#contributing)
*   [License](#license)
*   [Acknowledgements](#acknowledgements)

---

## Project Description


DVPWA (Damn Vulnerable Python Web Application) is an intentionally vulnerable web application meticulously crafted in Python, designed as a dedicated educational and training platform for cybersecurity enthusiasts, developers, and students. Its primary purpose is to provide a safe, hands-on environment to understand, identify, and practice exploiting common web security vulnerabilities, with a strong emphasis on various types of SQL Injection (SQLi) attacks.

Built with modern Python technologies and containerized using Docker, DVPWA offers a realistic yet controlled setting to experiment with malicious payloads, observe application responses, and gain practical experience in web application penetration testing. It serves as an invaluable resource for learning ethical hacking techniques, strengthening defensive coding practices, and deepening one's understanding of how vulnerabilities manifest in real-world applications.

**Important Security Warning:** This application is purposefully insecure and is intended for educational and testing purposes **only**. It must **NEVER** be deployed in a production environment or exposed to the public internet, as it poses significant security risks.

### Overview


DVPWA functions as an interactive learning platform where users can explore and exploit a range of web application vulnerabilities. It provides a live, runnable environment that mimics a typical web application, but with deliberately introduced flaws.

**What DVPWA Does:**

*   **Demonstrates Vulnerabilities:** The core functionality revolves around showcasing how common web vulnerabilities, particularly SQL Injection, can be exploited. This includes various SQLi types like error-based, time-based, and union-based injections.
*   **Hands-on Practice:** Users can interact directly with the application, inputting payloads into forms, manipulating URLs, and observing the system's responses to understand the mechanics of an attack. This active engagement facilitates a deeper learning experience than theoretical study alone.
*   **Safe Learning Environment:** By being an isolated, intentionally vulnerable system, DVPWA ensures that learning and experimentation can occur without risking real-world systems or data. It encourages users to safely test their understanding and tools (like SQLMap).
*   **Easy Deployment:** Leveraging Docker and Docker Compose, the entire application and its associated database (PostgreSQL) and caching layer (Redis) can be set up quickly and consistently, allowing users to focus on learning rather than complex environment configurations.

**Target Audience:**

*   **Cybersecurity Students:** Ideal for those new to web security, providing practical examples of common attack vectors.
*   **Aspiring Penetration Testers:** A perfect starting point to practice using security tools and manual exploitation techniques.
*   **Web Developers:** Helps developers understand how vulnerabilities are introduced and how to write more secure code.
*   **Security Trainers/Educators:** A ready-to-use lab environment for teaching web application security concepts.

DVPWA empowers users to transition from theoretical knowledge to practical skills, making the complex world of web application security more accessible and engaging.

## Key Features


*   **Comprehensive SQL Injection Coverage:** Demonstrates various SQLi types including error-based, union-based, time-based, and boolean-based blind injections.
*   **Interactive Learning Sandbox:** Provides a live, exploitable environment for hands-on practice.
*   **Isolated and Safe:** Designed to be run in a contained environment, preventing real-world risks.
*   **Dockerized Deployment:** Quick and consistent setup using Docker and Docker Compose.
*   **Reset Functionality:** Easily reset the application and database to a clean, vulnerable state for repeated practice sessions.

## Tech Stack


DVPWA is built using a modern and robust set of technologies, providing a realistic web application environment for security training.

*   **Backend:** Python 3.x
*   **Web Framework:** [aiohttp](https://docs.aiohttp.org/en/stable/)
*   **Templating:** [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
*   **Database:** [PostgreSQL](https://www.postgresql.org/) (accessed via `aiopg` and `psycopg2`)
*   **Caching/Data Structure Store:** [Redis](https://redis.io/) (accessed via `aioredis`, `hiredis`)
*   **Containerization:** [Docker](https://www.docker.com/), [Docker Compose](https://docs.docker.com/compose/)
*   **Dependency Management:** [Pip](https://pip.pypa.io/en/stable/)

## Getting Started


This section will guide you through setting up and running DVPWA. The recommended method is using Docker and Docker Compose, which provides a consistent and isolated environment.

#### Prerequisites


Before you begin, ensure you have the following installed on your system:

*   **Git:** For cloning the repository.
    *   [Download Git](https://git-scm.com/downloads)
*   **Docker:** For containerizing the application and its services.
    *   [Install Docker Engine](https://docs.docker.com/engine/install/)
*   **Docker Compose:** For orchestrating the multi-container application (usually included with Docker Desktop).
    *   [Install Docker Compose](https://docs.docker.com/compose/install/)

#### Installation Methods


##### 1. Using Docker (Recommended)


This is the quickest and most consistent way to get DVPWA up and running, as it encapsulates all dependencies (Python, PostgreSQL, Redis) within containers.

1.  **Clone the Repository:**
    Open your terminal or command prompt and clone the DVPWA repository:

    ```bash
    git clone https://github.com/patched-codes/dvpwa.git
    cd dvpwa
    ```

2.  **Build and Run with Docker Compose:**
    Navigate into the cloned repository directory. From there, execute the following command to build the Docker images and start the services in the background:

    ```bash
    docker-compose up -d --build
    ```
    *   `-d`: Runs the containers in "detached" mode, leaving them running in the background.
    *   `--build`: Forces Docker Compose to rebuild the images, ensuring you have the latest application and database configurations.

    This process might take a few minutes as Docker downloads base images and builds the application and database containers.

3.  **Initial Database Setup / Reset:**
    DVPWA includes a `recreate.sh` script to set up or reset the database to a fresh, vulnerable state. It's crucial to run this after the initial setup or whenever you want to reset the application's data.

    ```bash
    ./recreate.sh
    ```
    This script will connect to the PostgreSQL container and initialize the necessary tables and data for the vulnerable application.

4.  **Verify Installation:**
    Once the Docker containers are running and the database is initialized, open your web browser and navigate to:

    ```
    http://localhost:8080
    ```
    You should see the DVPWA welcome page, indicating that the application is successfully running.

5.  **Stopping the Application:**
    To stop the running Docker containers, navigate to the `dvpwa` directory in your terminal and run:

    ```bash
    docker-compose down
    ```
    This command will stop and remove the containers, networks, and volumes created by `docker-compose up`.

##### 2. Local Development Setup (For Contribution/Deeper Dive)


If you plan to contribute to DVPWA, modify its code, or prefer to run it without Docker, you can set it up locally. This method requires manual installation of Python, PostgreSQL, and Redis.

1.  **Prerequisites:**
    *   **Python 3.x:** Ensure you have a recent version of Python 3 installed.
    *   **PostgreSQL:** Install and configure a PostgreSQL database server. You will need to create a dedicated database and a user with appropriate permissions for DVPWA.
    *   **Redis:** Install and run a Redis server.

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/patched-codes/dvpwa.git
    cd dvpwa
    ```

3.  **Set up Python Environment:**
    It's highly recommended to use a Python virtual environment to manage dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

4.  **Install Python Dependencies:**
    Install all required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure Database and Redis:**
    *   **PostgreSQL:** You'll need to configure DVPWA to connect to your local PostgreSQL instance. Refer to the `config/` directory for configuration examples (e.g., `config/dev.py` or similar). You'll likely need to set environment variables or modify a configuration file with your database credentials.
    *   **Redis:** Ensure your Redis server is running and DVPWA is configured to connect to it (again, check the `config/` files).

6.  **Run the Application:**
    Once dependencies are installed and configuration is set up, you can run the application directly:

    ```bash
    python run.py
    ```
    The application should start, typically accessible at `http://localhost:8080` or a port specified in your local configuration.

7.  **Initial Database Setup:**
    The `recreate.sh` script is designed to work with the Docker setup. For a local setup, you might need to manually run the SQL migrations or adapt the `recreate.sh` script to connect to your local PostgreSQL instance, or manually execute the SQL commands found in the `migrations/` directory.

#### Troubleshooting (Installation)


*   **Docker not starting:** Ensure Docker Desktop (or your Docker daemon) is running. Check `docker logs <container_name>` for specific errors (use `docker ps` to find container names).
*   **Application not accessible:** Verify that the Docker containers are running (`docker ps`) and that no other service is occupying port `8080`.
*   **Database connection errors (local setup):** Double-check your PostgreSQL and Redis configurations, including host, port, username, and password. Ensure the database user has the necessary permissions.
*   **Python dependency errors (local setup):** Make sure your virtual environment is activated and all packages from `requirements.txt` are installed.

## How to Use DVPWA


DVPWA is designed for interactive learning. Your primary goal is to identify and exploit the intentionally built-in vulnerabilities. This section will guide you on how to navigate the application and effectively use it as a learning tool.

#### Accessing the Application


After successfully setting up DVPWA using Docker Compose (as described in the "Installation" section), the application will be accessible in your web browser at:

```
http://localhost:8080
```

#### Exploring Vulnerabilities


DVPWA's structure is designed to highlight different types of vulnerabilities. The core learning experience will revolve around interacting with various input forms and parameters.

1.  **Navigate to Vulnerable Sections:**
    Upon accessing the application, you'll find navigation links or sections dedicated to different vulnerability types. Look for sections explicitly labeled "SQL Injection" or similar. These are your primary targets for practicing exploitation.

2.  **Interact with Input Fields:**
    Within the SQL Injection sections, you will encounter forms with input fields (e.g., username, password, search queries). Your task is to input various payloads into these fields to test for vulnerabilities.

    *   **Common SQLi Payloads to Experiment With (General Guidance):**
        *   `'` (single quote): Often causes syntax errors that reveal vulnerability.
        *   `admin' --` or `admin' #`: Used to bypass authentication.
        *   `' OR 1=1 --`: Classic authentication bypass.
        *   `' UNION SELECT ... --`: Used for data exfiltration.
        *   Time-based payloads (`SLEEP(X)`, `BENCHMARK(X)`) for blind SQLi.
        *   Error-based payloads (`EXTRACTVALUE`, `UPDATEXML`) for blind SQLi.

    *   **Observe Responses:** Pay close attention to how the application responds to your inputs:
        *   **Error Messages:** Database error messages often indicate a SQL Injection vulnerability.
        *   **Changed Behavior:** Does the application behave unexpectedly? Do you gain access you shouldn't have?
        *   **Time Delays:** Delays in response time can indicate time-based blind SQLi.

3.  **Utilize Security Tools:**
    While manual testing is crucial for understanding, you can also use automated tools like [SQLMap](http://sqlmap.org/) to identify and exploit vulnerabilities in DVPWA. This helps you understand how such tools work and what they automate.

    *   **Example (Conceptual, adapt to specific URLs):**
        ```bash
        sqlmap -u "http://localhost:8080/sqli/some_vulnerable_page?param=value" --dbs
        ```
        (Replace `http://localhost:8080/sqli/some_vulnerable_page?param=value` with the actual vulnerable URL you are targeting.)

#### Learning Objectives


By interacting with DVPWA, you can aim to achieve the following:

*   **Understand SQL Injection Types:** Differentiate between various SQLi techniques (e.g., error-based, union-based, time-based, boolean-based blind).
*   **Practice Manual Exploitation:** Develop skills in crafting payloads and interpreting application responses without automated tools.
*   **Learn Tool Usage:** Gain experience using security testing tools like SQLMap in a safe environment.
*   **Identify Vulnerable Code Patterns:** By examining the source code (`sqli/` directory), you can learn to recognize insecure coding practices that lead to SQL Injection.
*   **Improve Defensive Strategies:** Understanding how attacks work is the first step towards writing more secure and resilient code.

#### Resetting the Application


If you make too many changes, corrupt the database, or simply want to start fresh with a clean state of vulnerabilities, you can reset the application and its database using the `recreate.sh` script:

```bash
./recreate.sh
```
Run this command from the root directory of the `dvpwa` repository. This will wipe the existing database and reinitialize it with the default vulnerable data.

#### Ethical Hacking Reminder


Always remember that DVPWA is an educational tool. The techniques you learn and practice here are powerful. Ensure you apply them ethically and legally. **Never** use these skills or tools on systems you do not have explicit permission to test.

## API Reference (Web Endpoints)


DVPWA is a web application, and its "API" primarily refers to its web routes (endpoints) that handle HTTP requests. These routes are defined using the `aiohttp` framework. The core application logic and route definitions, especially for the vulnerable sections, can be found in `run.py` and within the `sqli/` directory, specifically `sqli/routes.py`.

The following section outlines the key web endpoints and their general purpose, particularly focusing on those designed to demonstrate vulnerabilities.

#### `run.py` - Main Application Entry Point


The `run.py` file initializes the `aiohttp` web application, sets up middleware, configures templates, and registers the main application routes.

**Key Routes and Handlers:**

*   **`/` (Home Page):**
    *   **Method:** `GET`
    *   **Purpose:** Serves the main landing page of the DVPWA application. This page typically provides an overview or links to different vulnerability sections.
    *   **Handler:** `main.index` (defined in `main.py` or similar, which then links to the `sqli` module).

#### `sqli/routes.py` - SQL Injection Vulnerability Endpoints


This file is crucial as it contains the specific routes designed to be vulnerable to SQL Injection. The exact names and parameters of these routes are dynamic based on the specific SQLi examples implemented, but they generally follow patterns for common web application functionalities.

**General Structure of Vulnerable Endpoints (Examples):**

The `sqli/routes.py` file registers various routes within the `/sqli` path. These routes typically handle user input via `GET` query parameters or `POST` form data.

*   **`GET /sqli/login`**
    *   **Purpose:** Displays a login form. This form is likely backed by a SQL query that is vulnerable to authentication bypass SQL Injection.
*   **`POST /sqli/login`**
    *   **Purpose:** Processes submitted login credentials. This is the primary target for SQLi authentication bypass attempts.
    *   **Parameters:** `username`, `password` (example names, may vary).
*   **`GET /sqli/search`**
    *   **Purpose:** Displays a search form. This endpoint's backend query is often vulnerable to search-based SQL Injection, where input in the search field directly influences the SQL query.
    *   **Parameters:** `query` (example name, may vary).
*   **`GET /sqli/profile` or `GET /sqli/users?id=<user_id>`**
    *   **Purpose:** Displays user profiles or retrieves user information based on an ID. These endpoints are often vulnerable to IDOR (Insecure Direct Object Reference) or SQL Injection if the ID parameter is not properly sanitized.
    *   **Parameters:** `id` (example name, may vary).
*   **Other `sqli` paths:**
    The `sqli/routes.py` will contain multiple distinct endpoints, each demonstrating a different flavor or context of SQL Injection (e.g., error-based, union-based, time-based, boolean-based, different database interaction patterns). You will need to explore the application's interface or the source code to find the exact URLs and parameters for each specific vulnerability.

**How to Identify Specific Endpoints:**

1.  **Browse the application:** Navigate through the DVPWA web interface and look for input fields, search bars, login forms, or URL parameters that change based on your interaction. These are potential targets.
2.  **Inspect browser network requests:** Use your browser's developer tools (Network tab) to see the exact URLs and parameters sent to the server when you interact with the application.
3.  **Review the source code:** For a complete and definitive list, examine `sqli/routes.py` and associated view files (e.g., in `sqli/views.py` if present) to understand how routes are defined and how they process user input. Look for `app.router.add_get()`, `app.router.add_post()`, etc., definitions.

## Configuration Options and Customization


DVPWA's configuration is primarily managed through:

1.  **Environment Variables:** Especially when running with Docker Compose, environment variables defined in `docker-compose.yml` can override default settings.
2.  **`config/` Directory:** This directory likely contains Python files (`.py`) or YAML files (`.yml`) that define application settings, such as database connection strings, Redis connection details, and other application-specific parameters.

**Key areas for customization:**

*   **Database Connection:**
    *   **Docker Compose:** Configured via environment variables in `docker-compose.yml` for the `app` service (e.g., `POSTGRES_HOST`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`).
    *   **Local Setup:** Modified directly in configuration files within `config/` or through local environment variables that `run.py` or its configuration loading mechanism consumes.
*   **Redis Connection:**
    *   Similar to the database, configured via environment variables in `docker-compose.yml` or within `config/` files for local setups.
*   **Application Port:**
    *   **Docker Compose:** The `ports` mapping in `docker-compose.yml` (`"8080:8080"`) determines the host port. You can change the host port (the first `8080`) if port 8080 is already in use on your system.
    *   **Local Setup:** The port is likely defined in a configuration file within `config/` or directly in `run.py`.
*   **Debug Mode:**
    The application might have a debug mode setting (e.g., `DEBUG = True` in a config file) that can enable more verbose logging or specific development features. This is useful for understanding application flow but should never be enabled in a production-like environment.

To modify these settings:

1.  **For Docker Compose:** Edit `docker-compose.yml` and then run `docker-compose up -d --build` to apply changes.
2.  **For Local Setup:** Edit the relevant files in the `config/` directory or set appropriate environment variables before running `python run.py`.

## Error Handling and Troubleshooting


While DVPWA is designed to be vulnerable, some errors may arise from incorrect setup or unexpected interactions.

*   **"Site cannot be reached" or "Connection refused" after `docker-compose up`:**
    *   **Cause:** Docker containers might not be running or the application within the container failed to start.
    *   **Solution:**
        *   Verify Docker is running on your machine.
        *   Run `docker ps` to see if the `dvpwa-app` and `dvpwa-db` containers are running.
        *   Check container logs for errors: `docker logs dvpwa-app-1` (or `dvpwa_app_1`, check `docker ps` for exact name) and `docker logs dvpwa-db-1`.
        *   Ensure no other service is using port `8080` on your host machine.
*   **Database Connection Errors (within application logs):**
    *   **Cause:** The application container cannot connect to the database container.
    *   **Solution:**
        *   Verify the `dvpwa-db` container is running (`docker ps`).
        *   Check the database container logs for errors during startup.
        *   Ensure the database credentials (host, port, user, password) in `docker-compose.yml` (for the `app` service environment variables) or your local configuration are correct and match the database setup.
*   **`recreate.sh` script fails:**
    *   **Cause:** The script cannot connect to the PostgreSQL database, or permissions issues.
    *   **Solution:**
        *   Ensure the `dvpwa-db` container is running and accessible.
        *   Check the script's output for specific error messages. It might indicate issues with `psql` command or database credentials.
*   **Application crashes after specific input (unexpectedly):**
    *   **Cause:** While some errors are expected (part of the vulnerability), unexpected crashes might indicate a bug in the application itself (not related to the intended vulnerability) or an unhandled exception.
    *   **Solution:**
        *   Check the `dvpwa-app` container logs for Python tracebacks (`docker logs dvpwa-app-1`).
        *   If you're in a local setup, the traceback will be printed to your terminal.
        *   These logs can provide clues about the line of code causing the issue.
*   **Python dependency errors (local setup):**
    *   **Cause:** Missing or incorrectly installed Python packages.
    *   **Solution:**
        *   Ensure your virtual environment is activated (`source venv/bin/activate`).
        *   Run `pip install -r requirements.txt` again to ensure all dependencies are installed.

When troubleshooting, always check the logs of the relevant Docker containers first, as they provide the most immediate feedback on what might be going wrong inside the isolated environment.

## Project Structure


Understanding the project's layout can help you navigate the codebase, particularly if you wish to inspect the vulnerable sections or contribute.

*   **Root Directory:** Contains core files for application execution and containerization.
    *   `run.py`: The main entry point for the Python web application, starting the `aiohttp` server.
    *   `requirements.txt`: Lists all Python dependencies required by the project.
    *   `Dockerfile.app`: Dockerfile for building the main Python web application container.
    *   `Dockerfile.db`: Dockerfile for setting up the PostgreSQL database container.
    *   `docker-compose.yml`: Defines and orchestrates the multi-container application (application, database, redis).
    *   `recreate.sh`: A shell script used to reset or reinitialize the application's database to a clean, vulnerable state.
    *   `LICENSE`: Contains the licensing information for the project.
    *   `.gitignore`: Specifies intentionally untracked files to ignore.
*   **`sqli/`:** This crucial directory contains the deliberately vulnerable code examples related to various types of SQL Injection. This is where you'll find the targets for your exploitation practice.
*   **`migrations/`:** Houses database migration scripts, used to manage schema changes for the PostgreSQL database.
*   **`config/`:** Likely holds application configuration settings, such as database connection details, Redis settings, and application-specific parameters.

## Contributing


We welcome contributions to DVPWA! If you have suggestions for new vulnerabilities, improvements to existing ones, bug fixes, or documentation enhancements, please feel free to contribute. Your input helps make this a better learning resource.

1.  **Report Issues:** If you find a bug or have a feature request, please open an issue on the [GitHub repository issues page](https://github.com/patched-codes/dvpwa/issues).
2.  **Fork the Repository:** Start by forking the `dvpwa` repository to your GitHub account.
3.  **Create a Branch:** Create a new branch for your specific feature or bug fix (e.g., `feature/add-xss-vuln`, `fix/login-bug`).
4.  **Make Your Changes:** Implement your changes, ensuring they align with the project's purpose as an educational security tool.
5.  **Submit a Pull Request:** Once your changes are complete and tested, submit a pull request to the `main` branch of the original repository. Please provide a clear description of your changes.

## License


This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements


We acknowledge all open-source projects, tools, and resources that inspired or were used in the development of DVPWA.
