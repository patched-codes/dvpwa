```markdown
# Damn Vulnerable Python Web Application (DVPWA)


**Your Secure Sandbox for Mastering Web Application Vulnerability Exploitation**

---

## Table of Contents


*   [1. CRITICAL SECURITY WARNING / DISCLAIMER](#1-critical-security-warning--disclaimer)
*   [2. Description](#2-description)
*   [3. Features / Vulnerabilities Covered](#3-features--vulnerabilities-covered)
*   [4. Technologies Used](#4-technologies-used)
*   [5. Installation](#5-installation)
    *   [Prerequisites](#prerequisites)
    *   [Method A: Using Docker Compose (Recommended)](#method-a-using-docker-compose-recommended)
    *   [Method B: Manual Installation (Python, Pip, External Services)](#method-b-manual-installation-python-pip-external-services)
    *   [Verification](#verification)
*   [6. Usage](#6-usage)
    *   [Accessing the Application](#accessing-the-application)
    *   [Basic Usage Examples](#basic-usage-examples)
    *   [Resetting the Database](#resetting-the-database)
    *   [Important Note: Explore and Experiment](#important-note-explore-and-experiment)
    *   [Configuration Options and Customization](#configuration-options-and-customization)
*   [7. Project Structure](#7-project-structure)
*   [8. Contributing](#8-contributing)
*   [9. License](#9-license)
*   [10. Troubleshooting](#10-troubleshooting)
    *   [Common Issues](#common-issues)
    *   [Troubleshooting Steps](#troubleshooting-steps)

---

## 1. CRITICAL SECURITY WARNING / DISCLAIMER


**DVPWA is *deliberately insecure* and is provided for educational and testing purposes ONLY.**

**&#x26;C3; It MUST NEVER be deployed in a production environment or exposed to any public or untrusted network.&#x26;C3;**

Running this application in an insecure manner could lead to severe security compromises of your system, network, or data. Always operate DVPWA within an isolated, controlled, and secure testing environment (e.g., a dedicated virtual machine, a sandbox network, or a local-only setup).

**The creators and maintainers of DVPWA disclaim all liability for any misuse or damage caused by improper deployment, handling, or interaction with this intentionally vulnerable software.** You assume full responsibility for any risks associated with its use.

---

## 2. Description


Damn Vulnerable Python Web Application (DVPWA) is a purposefully insecure web application built with modern asynchronous Python technologies, specifically designed as a safe and controlled environment for learning about, demonstrating, and practicing common web application vulnerabilities. With a primary focus on various forms of SQL Injection, DVPWA provides a hands-on platform for security researchers, penetration testers, and developers to understand the intricacies of web security flaws.

Built using `aiohttp` for the web framework, `Jinja2` for templating, `PostgreSQL` as the database, and `Redis` for caching/session management, and containerized with Docker, DVPWA simulates a contemporary web development stack. This allows users to explore real-world attack vectors in a contained setting, making it an ideal tool for honing ethical hacking skills, validating security tools, and gaining practical insights into defense mechanisms.

By interacting with DVPWA, users can deepen their understanding of how vulnerabilities work, how they can be exploited, and, by extension, how to build more secure applications.

---

## 3. Features / Vulnerabilities Covered


DVPWA is engineered to expose a range of web vulnerabilities, primarily focusing on:

*   **SQL Injection (SQLi):** Various forms of SQL Injection are implemented throughout the application, providing a practical testing ground for different attack techniques (e.g., error-based, union-based, boolean-based, time-based, login bypass).
*   **Modern Technology Stack:** Utilizes `aiohttp`, `PostgreSQL`, and `Redis` to reflect vulnerabilities in a contemporary asynchronous Python web environment.

The project aims to be a comprehensive testbed for identifying and exploiting common web application vulnerabilities, specifically emphasizing SQL injection.

---

## 4. Technologies Used


DVPWA leverages the following core technologies:

*   **Python 3:** The primary language for backend logic.
*   **aiohttp:** Asynchronous web framework for building the web application.
*   **Jinja2:** Templating engine for rendering dynamic HTML content.
*   **PostgreSQL:** Relational database for data storage (`aiopg`, `psycopg2`).
*   **Redis:** In-memory data store used for caching and session management (`aioredis`, `hiredis`).
*   **Docker & Docker Compose:** For containerization and orchestration, providing an isolated and easily deployable environment.
*   **PyYAML & Trafaret:** For application configuration.
*   **pip:** Python's package installer for dependency management (`requirements.txt`).

---

## 5. Installation


This guide provides instructions on how to set up and run the Damn Vulnerable Python Web Application (DVPWA).

### Prerequisites


Before you begin, ensure you have the following tools installed on your system:

*   **Git:** For cloning the repository.
    *   [Download Git](https://git-scm.com/downloads)
*   **Docker:** For containerizing the application and its dependencies.
    *   [Download Docker Desktop](https://www.docker.com/products/docker-desktop)
*   **Docker Compose:** For orchestrating the multi-container application (usually included with Docker Desktop).
    *   [Install Docker Compose](https://docs.docker.com/compose/install/)

### Method A: Using Docker Compose (Recommended)


This is the easiest and most recommended method, as it sets up the application, database (PostgreSQL), and caching (Redis) services in isolated containers.

1.  **Clone the Repository:**
    Open your terminal or command prompt and clone the DVPWA repository:
    ```bash
git clone https://github.com/your-repo-link/dvpwa.git

# (Note: Replace with the actual repository URL)

    ```

2.  **Navigate to the Project Directory:**
    Change into the cloned repository's directory:
    ```bash
cd dvpwa
    ```

3.  **Build and Run with Docker Compose:**
    From within the `dvpwa` directory, use Docker Compose to build the application image and start all services:
    ```bash
docker-compose up --build
    ```
    This command will:
    *   Build the `dvpwa` application Docker image based on `Dockerfile.app`.
    *   Pull the PostgreSQL and Redis images.
    *   Start the application, database, and Redis services.
    *   It may take a few minutes for the first build.

4.  **Database Initialization (Important):**
    Once the Docker Compose services are running (you should see logs from `app`, `db`, and `redis` services), you need to initialize the database schema and populate it with some data. Open a *new* terminal window, navigate back to the `dvpwa` directory, and run the `recreate.sh` script:
    ```bash
./recreate.sh
    ```
    This script is crucial for setting up the database required by the application. You might need to make it executable first: `chmod +x recreate.sh`.

### Method B: Manual Installation (Python, Pip, External Services)


This method requires you to manage Python, PostgreSQL, and Redis installations separately. Use this method if you prefer a non-containerized setup or need more granular control over the environment.

**WARNING:** This method requires careful manual setup of PostgreSQL and Redis, including creating databases/users and ensuring network accessibility. The Docker Compose method is significantly simpler for a working environment.

1.  **Clone the Repository:**
    ```bash
git clone https://github.com/your-repo-link/dvpwa.git
cd dvpwa
    ```

2.  **Set up Python Environment:**
    It is highly recommended to use a Python virtual environment to avoid conflicts with your system's Python packages:
    ```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Python Dependencies:**
    Install the required Python packages using pip:
    ```bash
pip install -r requirements.txt
    ```

4.  **Install and Configure PostgreSQL and Redis:**
    You must have a running **PostgreSQL database server** and a **Redis server** accessible from your DVPWA installation.
    *   **PostgreSQL:** Install PostgreSQL and create a database and user for DVPWA. You will need to configure the `config/default.py` or similar configuration files to point to your PostgreSQL instance (host, port, database name, user, password).
    *   **Redis:** Install Redis. DVPWA will connect to it for sessions/caching. Ensure Redis is running and accessible.

5.  **Run the Application:**
    After configuring your database and Redis connections in the application's configuration files (typically `config/default.py`), you can start the DVPWA application:
    ```bash
python run.py
    ```

6.  **Database Initialization:**
    Similar to the Docker method, you'll need to initialize the database. The `recreate.sh` script is designed to work with the Docker Compose setup. For a manual setup, you might need to manually run the SQL migrations and data seeding, or adapt `recreate.sh` to connect to your standalone PostgreSQL instance.

### Verification


After successfully running DVPWA using either method, you can verify its operation:

1.  **Access the Application:**
    Open your web browser and navigate to:
    ```
http://localhost:8080
    ```
    You should see the DVPWA home page. If you are running Docker on a remote machine or a VM, replace `localhost` with the appropriate IP address.

2.  **Check Docker Container Status (Docker Compose Method):**
    In a new terminal, navigate to the `dvpwa` directory and run:
    ```bash
docker-compose ps
    ```
    You should see `app`, `db`, and `redis` services listed with a `State` of `Up`.

3.  **Check Application Logs:**
    If the application isn't loading, check the logs for errors:
    *   **Docker Compose:** `docker-compose logs app`
    *   **Manual:** Check your terminal where `python run.py` was executed.

---

## 6. Usage


DVPWA is designed for you to explore its vulnerabilities. Here are some basic steps and examples to help you get started with testing.

### Accessing the Application


Once all services are running and the database is initialized, open your web browser and navigate to:

```
http://localhost:8080
```

You should now see the DVPWA home page.

### Basic Usage Examples


The core purpose of DVPWA is to demonstrate SQL Injection. Based on the repository structure, the `sqli/` directory indicates that the primary focus is on SQL Injection vulnerabilities.

*   **Identifying Vulnerable Sections:** After accessing `http://localhost:8080`, look for navigation links or directly try accessing paths related to SQL Injection. A common pattern in such applications is `/sqli` or similar. Explore the application's interface to find input fields, search forms, or login forms that interact with the database.

While the exact vulnerable parameters will vary depending on the specific page implementation within DVPWA, a common scenario involves injecting malicious SQL into an input field.

**Example Scenario (Illustrative):**

Imagine a search box where you enter a "Product ID". Internally, the application might be running a query like:

```sql
SELECT * FROM products WHERE product_id = 'YOUR_INPUT';
```

**Common SQL Injection Payloads:**

1.  **Always True Condition (Bypass Authentication/Retrieve All Data):**
    If the input field is vulnerable, you can often make the condition always true.
    *   **Input:** `' OR '1'='1`
    *   **Expected Resulting Query:** `SELECT * FROM products WHERE product_id = '' OR '1'='1';`
    *   **Outcome:** This often returns all records from the table, as `'1'='1'` is always true.

2.  **Comments to Bypass Remainder of Query:**
    You can use SQL comments (`--` for MySQL/PostgreSQL, or `/* ... */`) to ignore the rest of the original query.
    *   **Input:** `' OR 1=1 --`
    *   **Expected Resulting Query:** `SELECT * FROM products WHERE product_id = '' OR 1=1 --';`
    *   **Outcome:** Similar to the above, bypassing the original condition.

3.  **Union-Based SQL Injection (Retrieving Data from Other Tables):**
    This is more advanced and requires knowing the number of columns and data types in the original query.
    *   **Input:** `' UNION SELECT null, database(), version() --`
    *   **Expected Resulting Query:** `SELECT * FROM products WHERE product_id = '' UNION SELECT null, database(), version() --';`
    *   **Outcome:** If successful and the column counts/types match, this could return the database name and version along with your original query results. You'll need to adapt the `null` values and functions to match the actual number of columns returned by the original query.

**How to Practice:**

*   **Identify Input Fields:** Look for search bars, login forms, parameter in URLs (GET requests), or any user-supplied input that might interact with the database.
*   **Test with Simple Payloads:** Start with single quotes (`'`) to check for errors, then try `OR '1'='1'` or similar.
*   **Observe Responses:** Pay attention to error messages (which can reveal database details), unexpected data, or changes in application behavior.

### Resetting the Database


If you corrupt the database during your testing or wish to revert it to its initial state, you can simply re-run the `recreate.sh` script:

```bash
./recreate.sh
```

Ensure your Docker containers are running (`docker-compose ps`) or restart them if necessary before running the script.

### Important Note: Explore and Experiment


DVPWA is built for hands-on learning. The best way to understand its vulnerabilities is to actively explore different input fields, try various SQL injection payloads, and observe the application's responses. The specific vulnerable endpoints and the exact payloads might vary, so experimentation is key.

### Configuration Options and Customization


DVPWA uses `trafaret-config` and `pyyaml` for configuration, typically found in the `config/` directory.

The main configuration file is likely `config/default.py` or similar. This file would contain settings for:

*   **Database Connection:** Host, port, database name, username, password for PostgreSQL.
*   **Redis Connection:** Host, port for Redis.
*   **Application Server:** Host and port for the `aiohttp` web server (e.g., `localhost:8080`).
*   **Logging:** Logging levels and destinations.

**To Customize:**

1.  **Locate Configuration Files:** Explore the `config/` directory to find `.py` or `.yaml` files defining application settings.
2.  **Modify Values:** Directly edit these files to change database credentials, Redis connections, or the application's listening address/port.
    *   **Note:** If running with Docker Compose, you might need to rebuild your Docker image (`docker-compose build app`) and restart services (`docker-compose up`) after changing application-specific configuration files (those not related to Docker Compose itself).

---

## 7. Project Structure


The DVPWA repository is organized to clearly separate concerns and highlight vulnerable areas:

*   `sqli/`: Contains the intentionally vulnerable code related to SQL Injection modules and routes.
*   `config/`: Holds application configuration files (e.g., database connection settings).
*   `migrations/`: Contains database schema migration scripts.
*   `run.py`: The main application entry point for the `aiohttp` web server.
*   `Dockerfile.app`: Dockerfile for building the main DVPWA application container.
*   `Dockerfile.db`: Dockerfile for the PostgreSQL database container.
*   `docker-compose.yml`: Orchestrates the setup and execution of the application, PostgreSQL database, and Redis cache within Docker containers.
*   `recreate.sh`: An executable script for initial database setup and resetting.
*   `requirements.txt`: Lists all Python dependencies required by the application.

---

## 8. Contributing


Contributions to DVPWA are welcome! If you'd like to contribute to making this vulnerable application even better for learning and testing, here are some guidelines:

*   **New Vulnerability Types:** Add new modules demonstrating different web application vulnerabilities (e.g., XSS, CSRF, File Upload vulnerabilities, SSRF, etc.).
*   **Improve Existing Vulnerabilities:** Enhance the complexity or variations of existing vulnerabilities (e.g., more intricate SQLi scenarios).
*   **Fix Non-Vulnerability Bugs:** Correct any unintended bugs or issues that are not related to the deliberate vulnerabilities (e.g., UI glitches, non-security-related logic errors).
*   **Documentation Enhancements:** Improve the README, add more detailed explanations for vulnerabilities, or create usage examples.

**Contribution Process:**

1.  **Fork** the repository.
2.  **Create a new branch** for your feature or bug fix (`git checkout -b feature/your-feature-name`).
3.  **Make your changes**, ensuring they align with the project's goal of being *intentionally insecure* in designated areas.
4.  **Test your changes** to ensure they work as expected (especially if adding a new vulnerability, verify it is indeed exploitable).
5.  **Commit your changes** with a clear and concise message.
6.  **Push your branch** to your forked repository.
7.  **Open a Pull Request** to the `main` branch of the original repository, describing your changes and their purpose.

---

## 9. License


This project is licensed under the MIT License - see the `LICENSE` file for details.

---

## 10. Troubleshooting


Here are common issues and troubleshooting tips when working with DVPWA:

### Common Issues


*   **Port Conflicts:** If `http://localhost:8080` is already in use by another application on your system, the DVPWA Docker container might fail to start or map its port correctly.
*   **Docker Daemon Not Running:** Docker commands will fail if the Docker daemon (engine) is not running on your system.
*   **Database/Redis Connection Issues:** Especially during manual setup, incorrect connection strings or inaccessible services can prevent the application from starting.
*   **`recreate.sh` Permission Denied:** The script might not be executable.
*   **Application Crashes on Startup:** Often due to missing dependencies (if installing manually) or incorrect configuration.

### Troubleshooting Steps


1.  **Check Docker Status:**
    Ensure Docker Desktop (or your Docker daemon) is running.
    Verify containers are up:
    ```bash
docker-compose ps
    ```
    All services (`app`, `db`, `redis`) should show `State` as `Up`.

2.  **Inspect Container Logs:**
    For issues with the application not starting or behaving unexpectedly, check its logs:
    ```bash
docker-compose logs app
    ```
    This will often reveal database connection errors, configuration issues, or Python tracebacks. You can also check logs for `db` and `redis` if those services seem problematic.

3.  **Address Port Conflicts:**
    If port 8080 is in use, modify `docker-compose.yml` to map to a different host port (e.g., `8081:8080`) and then run `docker-compose up --build`.

4.  **Grant Execute Permissions to `recreate.sh`:**
    If you get a "permission denied" error when running `./recreate.sh`, make it executable:
    ```bash
chmod +x recreate.sh
    ```

5.  **Database Initialization Issues:**
    If the application loads but no data appears or SQL errors occur, ensure you have successfully run `./recreate.sh`. You might need to bring down Docker Compose (`docker-compose down`) and then bring it up again (`docker-compose up --build`) before re-running `recreate.sh`.

6.  **Manual Installation - Dependency and Configuration Check:**
    If you installed manually:
    *   Ensure all `requirements.txt` dependencies are installed: `pip install -r requirements.txt`.
    *   Verify your PostgreSQL and Redis servers are running and accessible from the machine running DVPWA.
    *   Double-check your database and Redis connection settings in the `config/` files.
```