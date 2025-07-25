# Damn Vulnerable Python Web Application (DVPWA)

**Tagline:** A Hands-On Playground for Mastering Web Security Vulnerabilities.

---

### Project Description

The Damn Vulnerable Python Web Application (DVPWA) is an intentionally insecure web application developed in Python, leveraging `aiohttp` for its asynchronous web framework, `PostgreSQL` for its database, and `Redis` for caching. Designed specifically as a comprehensive educational tool, DVPWA provides a safe and controlled environment for security researchers, developers, students, and educators to practice, learn, and identify common web vulnerabilities.

By interacting with DVPWA, users can gain practical experience in discovering and exploiting flaws such as SQL Injection (as indicated by the dedicated `sqli` module) and potentially other prevalent web application security issues. The application is fully containerized using Docker and Docker Compose, ensuring an easy and consistent setup across different environments, making it ideal for cybersecurity training, ethical hacking practice, and secure coding demonstrations.

---

### Overview

DVPWA serves as a practical sandbox for exploring the intricacies of web application security. Its primary function is to demonstrate and expose common vulnerabilities in a controlled manner, allowing users to safely test various attack techniques without compromising real-world systems.

**What it Does:**
DVPWA simulates a typical web application but with deliberately engineered security weaknesses. Users can interact with different sections of the application, such as user authentication, data input forms, and retrieval mechanisms, all of which are designed to be vulnerable.

**Key Features & Benefits:**
*   **Educational Focus:** Provides a hands-on learning experience for web security.
*   **Real-World Vulnerabilities:** Implements common flaws like SQL Injection, mirroring those found in production applications.
*   **Safe Environment:** Intended for isolated use, preventing accidental damage to live systems.
*   **Containerized Setup:** Easy deployment with Docker and Docker Compose, minimizing setup complexities.
*   **Python-centric:** Great for those looking to understand vulnerabilities in Python-based web applications.

**Technology Highlights:**
*   **Python:** Core programming language.
*   **Aiohttp:** Asynchronous web framework.
*   **PostgreSQL:** Relational database management system.
*   **Redis:** In-memory data store for caching.
*   **Docker & Docker Compose:** For environment containerization and orchestration.

**Use Cases & Applications:**
*   **Cybersecurity Training:** Ideal for hands-on labs in cybersecurity courses.
*   **Penetration Testing Practice:** Allows aspiring and professional penetration testers to hone their skills.
*   **Secure Coding Demonstrations:** Helps developers understand common pitfalls and how to write more secure code.
*   **Security Tool Testing:** A target for evaluating the effectiveness of vulnerability scanners and other security tools.

**Target Audience:**
This project is invaluable for anyone passionate about web security, including:
*   Cybersecurity students and educators.
*   Aspiring and professional penetration testers.
*   Web developers interested in secure coding practices.
*   Security researchers exploring new attack vectors.

---

### Installation Guide for Damn Vulnerable Python Web Application (DVPWA)

This guide provides comprehensive instructions for setting up and running the Damn Vulnerable Python Web Application (DVPWA). Due to its nature as an intentionally vulnerable application, it is **crucial** to follow these instructions carefully and ensure DVPWA is run in an isolated and controlled environment.

---

#### 1. Prerequisites

Before you begin, ensure you have the following software installed on your system:

*   **Git**: For cloning the repository.
    *   [Download Git](https://git-scm.com/downloads)
*   **Docker**: A platform for developing, shipping, and running applications in containers.
    *   [Install Docker Engine](https://docs.docker.com/engine/install/)
*   **Docker Compose**: A tool for defining and running multi-container Docker applications. It's usually installed automatically with Docker Desktop.
    *   [Install Docker Compose](https://docs.docker.com/compose/install/)

---

#### 2. Installation Methods

DVPWA is designed to be easily deployed using Docker and Docker Compose, which is the recommended method. A manual setup is also outlined for advanced users, but it requires more configuration.

##### Method 1: Using Docker and Docker Compose (Recommended)

This is the fastest and most reliable way to get DVPWA up and running, as it encapsulates all dependencies within containers.

**Step 1: Clone the Repository**
Open your terminal or command prompt and clone the DVPWA repository from GitHub:

```bash
git clone https://github.com/patched-codes/dvpwa.git
```

**Step 2: Navigate to the Project Directory**
Change your current directory to the newly cloned `dvpwa` project folder:

```bash
cd dvpwa
```

**Step 3: Build and Run Docker Containers**
From within the `dvpwa` directory, execute the following command to build the application and database images, and then start the containers in detached mode (`-d`):

```bash
docker-compose up --build -d
```

This command will:
*   Build the `Dockerfile.app` for the Python application.
*   Build the `Dockerfile.db` for the PostgreSQL database.
*   Create and start the services defined in `docker-compose.yml` (application and database).

**Step 4: Initialize the Database (Optional, but Recommended for a Clean Start)**
The `recreate.sh` script is available to help initialize or reset the database. It's good practice to run this after the containers are up for the first time or if you want to reset the application's state.

```bash
chmod +x recreate.sh
./recreate.sh
```

*Note: You might need to wait a few moments after `docker-compose up` for the database container to be fully ready before running `recreate.sh`.*

**Step 5: Access the Application**
Once the containers are running, the DVPWA application will be accessible via your web browser.

*   Open your web browser and navigate to: `http://localhost:<port_number>`
    *   **To find the exact port number:** Inspect the `docker-compose.yml` file in the project's root directory under the `ports` mapping for the `app` service. Common ports include `80`, `8000`, or `5000`.

##### Method 2: Manual Setup (Python Environment)

This method involves setting up the Python environment, PostgreSQL, and Redis manually. This is generally more complex and prone to environment-specific issues, and therefore **not recommended for quick setup or beginners.**

**Step 1: Clone the Repository**
```bash
git clone https://github.com/patched-codes/dvpwa.git
cd dvpwa
```

**Step 2: Set Up a Python Virtual Environment**
It's highly recommended to use a virtual environment to manage Python dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Step 3: Install Python Dependencies**
Install all required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

**Step 4: Install and Configure PostgreSQL and Redis**
You will need to manually install and configure PostgreSQL and Redis on your system. This involves:

*   Installing PostgreSQL server.
*   Creating a new PostgreSQL database and user for DVPWA.
*   Installing Redis server.
*   Updating the DVPWA configuration files (likely in the `config/` directory) to point to your local PostgreSQL and Redis instances, including connection strings, usernames, and passwords.

**Step 5: Run Database Migrations**
If the project uses database migrations (indicated by the `migrations/` directory), you'll need to run them after configuring the database. The specific command will depend on the migration tool used (e.g., Alembic, Flask-Migrate). This information is not explicitly available in the provided context, so you might need to inspect the `migrations/` directory or `run.py` for clues.

**Step 6: Run the Application**
After all dependencies are installed and configured, you can run the application's main entry point:

```bash
python run.py
```

The application will usually indicate the address and port it's listening on in the console output.

---

#### 3. Verification Steps

To ensure DVPWA is running correctly:

1.  **Check Docker Container Status (if using Docker Compose):**
    ```bash
docker ps
    ```
    You should see `dvpwa-app` and `dvpwa-db` (or similar names) containers listed with `Up` status.

2.  **Access the Web Application:**
    Open your web browser and navigate to the application's URL (e.g., `http://localhost:<port_number>`). You should see the DVPWA interface.

3.  **Verify Functionality:**
    Try navigating to known vulnerable paths, such as the `sqli` section (e.g., `http://localhost:<port_number>/sqli`), to confirm the application loads and interacts with the database.

---

#### 4. Troubleshooting Common Issues

*   **Port Conflicts:** If the application fails to start due to a port conflict, another service might be using the port DVPWA is trying to bind to.
    *   **Solution (Docker Compose):** Modify the `ports` mapping in `docker-compose.yml` to use a different host port (e.g., `8080:80`).
    *   **Solution (Manual):** Change the port in `run.py` or the application's configuration.
*   **Docker Daemon Not Running:** Ensure Docker Desktop (or Docker daemon) is running on your system.
*   **Database Connection Errors:**
    *   **Docker Compose:** Ensure the `dvpwa-db` container is running without errors. Check its logs: `docker logs dvpwa-db`.
    *   **Manual Setup:** Verify your PostgreSQL and Redis servers are running and that the connection details in DVPWA's configuration are correct.
*   **Container Logs:** For detailed error messages from the application or database, check the Docker container logs:
    ```bash
docker logs dvpwa-app
docker logs dvpwa-db
    ```
*   **Rebuilding Containers (Docker Compose):** If you encounter persistent issues, try cleaning up and rebuilding the containers:
    ```bash
docker-compose down --volumes
docker-compose up --build -d
./recreate.sh
    ```

---

#### 5. Important Security Warning: Development Setup vs. Production Deployment

**DVPWA is an intentionally insecure application designed purely for educational and testing purposes.**

*   **NEVER DEPLOY DVPWA IN A PRODUCTION ENVIRONMENT.**
*   **NEVER EXPOSE DVPWA TO THE PUBLIC INTERNET.**
*   **ALWAYS RUN DVPWA IN AN ISOLATED AND CONTROLLED ENVIRONMENT** such as a virtual machine, a dedicated sandbox, or within a private network.
*   Using DVPWA with sensitive data is strongly discouraged.

This application contains deliberate vulnerabilities that could be exploited by malicious actors if exposed. Treat it as a lab environment for learning and practice only.

---

### Usage Guide for Damn Vulnerable Python Web Application (DVPWA)

This section guides you on how to interact with the DVPWA application and explore its intentionally designed vulnerabilities. Remember, DVPWA is built to be insecure for educational purposes.

---

#### 1. Accessing the Application

Once you have successfully installed and started DVPWA (preferably using Docker Compose), you can access it via your web browser.

*   **URL:** The application will be accessible at `http://localhost:<port_number>`.
    *   **To find the exact port number:** Refer to the `ports` mapping for the `app` service within your `docker-compose.yml` file. A common port used is `8000`, so try `http://localhost:8000`.

Upon navigating to the URL, you should see the DVPWA's main interface.

---

#### 2. Exploring Vulnerabilities (SQL Injection Example)

DVPWA is designed to demonstrate various web security flaws. A prominent vulnerability implemented is SQL Injection (SQLi), as indicated by the `sqli` directory in the project structure.

To begin exploring, navigate to the dedicated SQL Injection section of the application.

*   **SQL Injection Path:** `http://localhost:<port_number>/sqli` (e.g., `http://localhost:8000/sqli`)

Within this section, you will find input fields or parameters designed to be vulnerable to SQL Injection attacks.

**Example: Demonstrating SQL Injection**

Let's assume there's a user search feature or a product lookup where you can input an ID or a name. For a typical SQL Injection, you would try to manipulate the query executed on the backend.

1.  **Identify an input field:** On the `/sqli` page, locate an input field, for instance, one that might search for a user by ID or retrieve a product detail. Let's imagine it's a "User ID" input.

2.  **Test for SQLi:**
    *   **Normal Input:** Enter a valid ID, e.g., `1`. Observe the normal output.
    *   **Simple Injection Test:** Enter a common SQL injection payload. For example, if the backend query looks something like `SELECT * FROM users WHERE id = <INPUT>`, you can try to break out of the query.

    *   **Payload:** Try entering `1' OR '1'='1` into the input field.
        *   **Expected Behavior:** If vulnerable, this input might cause the application to return all users (or an unexpected result) because the `OR '1'='1'` condition is always true, effectively bypassing the original filter.

    *   **Payload (Union-based):** You might also try a union-based attack to extract data: `1' UNION SELECT NULL, version(), NULL, NULL --` (adjusting the number of `NULL`s based on the expected columns and the actual query).

    *   **Payload (Error-based):** To induce an error and gain information: `1' AND (SELECT 1 FROM RDB$DATABASE WHERE 1=1 AND 1=CAST((SELECT @@version) AS INT)) --` (or other database-specific error functions).

**Important Note:** The exact payloads and the vulnerable parameters will vary based on the specific implementation within the `sqli` module. Your goal is to identify these vulnerable points and craft appropriate injection strings.

---

#### 3. General Usage Tips for DVPWA

*   **Experiment Safely:** DVPWA is your lab. Feel free to try various attack vectors and payloads.
*   **Observe Errors:** Pay close attention to any error messages displayed by the application. These can often reveal valuable information about the backend database, its version, or the query structure, which is crucial for crafting more effective attacks.
*   **Analyze Network Traffic:** Use browser developer tools (F12) or a proxy tool like OWASP ZAP or Burp Suite to inspect HTTP requests and responses. This can help you understand how data is sent to and from the application and identify potential injection points.
*   **Review Source Code (Optional but Recommended):** Since you have the repository, you can examine the Python code in the `sqli/` directory and `run.py` to understand precisely how the vulnerabilities are implemented. This provides deeper insights into secure coding practices and common pitfalls.

---

#### 4. Security Warning: Intentionally Insecure

We cannot stress this enough: **DVPWA is built to be vulnerable.**

*   **DO NOT use this application in a production environment.**
*   **DO NOT expose this application to the public internet.**
*   **ONLY run DVPWA in isolated environments** such as a dedicated virtual machine, a sandbox container, or a private network that is not accessible from the outside.
*   **NEVER use DVPWA with real, sensitive data.**

This application is solely for educational and ethical hacking purposes. Treating it otherwise poses significant security risks.

---

### API Reference / Vulnerability Overview

In the context of DVPWA, a traditional "API Reference" might not apply in the same way as a robust, production-ready application. Instead, this section serves as an overview of the *vulnerable interfaces* or "APIs" you are expected to interact with.

The core of DVPWA's demonstrative vulnerabilities resides in the web endpoints it exposes.

*   **File:** `sqli/routes.py`
    *   **Description:** This file is identified as containing API-related code, strongly indicating that it defines the routes and handlers responsible for demonstrating SQL Injection vulnerabilities. You can expect to find Flask/Aiohttp route definitions here that process user input in an insecure manner, leading to SQLi.
    *   **Interaction:** The "API" in this case is the web interface served by `aiohttp`. You will interact with it by making HTTP requests (e.g., via your browser or tools like `curl`, Postman, or Burp Suite) to the defined routes, particularly those under the `/sqli` path.

**Key Concepts for Interaction:**

*   **HTTP Methods:** You will primarily use `GET` and `POST` requests to interact with the application's forms and parameters.
*   **Parameters:** Identify URL parameters (query strings) and form parameters that the application processes. These are often the entry points for injection attacks.
*   **Error Messages:** The application might intentionally leak verbose error messages to aid in vulnerability discovery, which can be part of its "API" for penetration testing.
*   **Source Code Review:** For a precise understanding of the exposed "APIs" and their vulnerabilities, reviewing the source code in `sqli/routes.py` and related files is highly recommended.

The purpose of this "API" is not to provide a stable, documented interface for integration, but rather to present a clear target for security testing and learning about web vulnerabilities.

---

### Configuration Options and Customization

DVPWA, as a Dockerized application, primarily relies on its Docker setup for configuration. However, there are also internal application configuration files you might want to adjust.

#### 1. Docker Compose Configuration (`docker-compose.yml`)

The `docker-compose.yml` file is the primary configuration point for the entire application stack (app and database).

*   **Location:** Root directory of the repository.
*   **Common Customizations:**
    *   **Port Mapping:** Change the host port on which the DVPWA application is accessible.
        ```yaml
services:
  app:
    ports:
      - "8080:80" # Changes host port from 8000 (example) to 8080
        ```
    *   **Environment Variables:** You might find environment variables defined for the `app` or `db` services, which can control database credentials, debug modes, or other application-specific settings. Consult the `Dockerfile.app` and `run.py` for variables that the application expects.
    *   **Volume Mounts:** For persistent data (e.g., PostgreSQL database data), you might see volume mounts. You can customize these paths if needed.

    **To apply changes to `docker-compose.yml`:** After modifying the file, you will need to rebuild and restart your services:
    ```bash
docker-compose down --volumes
docker-compose up --build -d
    ```

#### 2. Application-Specific Configuration Files

The `config/` directory is where DVPWA stores its internal application settings.

*   **Location:** `dvpwa/config/`
*   **Contents:** You will likely find `.yaml` files (e.g., `config.yaml`, `db.yaml`, `redis.yaml`) or similar configuration formats that the Python application (`run.py`) reads at startup.
*   **Common Customizations:**
    *   **Database Connection:** Modify PostgreSQL connection details (host, port, username, password, database name) if you are running the database outside of Docker Compose or if you've changed the default Docker network settings.
    *   **Redis Connection:** Adjust Redis connection settings if your Redis instance is not running as expected or is on a different host/port.
    *   **Application Settings:** Other application-specific parameters, such as debug flags, logging levels, or session settings, might be configured here.

    **To apply changes to `config/` files (when running via Docker Compose):**
    If these configuration files are *inside* the Docker image, you would typically need to rebuild the `app` Docker image for changes to take effect:
    ```bash
docker-compose up --build -d app # Rebuilds and restarts only the app service
    ```
    Alternatively, for development, you might mount the `config/` directory as a volume in `docker-compose.yml` so that changes are immediately reflected without rebuilding the image. (This is a common practice but might not be set up by default in DVPWA).

#### 3. `run.py` Adjustments (Manual Setup)

If you are performing a manual setup of DVPWA without Docker, `run.py` might contain hardcoded values or load configurations that you can directly modify. This is less recommended as it deviates from the intended containerized deployment.

**General Advice for Customization:**

*   **Consult Source Code:** For definitive answers on what can be configured and how, always refer to the source code of `run.py` and any files within the `config/` directory.
*   **Environment Variables vs. Config Files:** Understand whether a setting is controlled by environment variables (often preferred in Dockerized applications) or static configuration files.
*   **Security Implications:** When modifying configurations, especially those related to database credentials or exposing ports, be mindful of the security implications, even in a development environment.

By understanding these configuration points, you can adapt DVPWA to your specific learning environment or integrate it into a larger security training setup.
