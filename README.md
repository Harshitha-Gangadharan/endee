# 🛡️ Resume-Shield AI (Compliance-First Screening)

This project was developed as a **technical test project for the internship selection process at Endee Labs**. It demonstrates a privacy-centric resume screening tool that integrates a local **PII Redaction Scanner** with the **Endee Labs Vector Engine** to ensure candidate data remains secure during AI processing.

---

## 🏗️ Project Architecture

The system follows a modular architecture that prioritizes data privacy and local high-speed vector search.

- **`endee`**: The core Vector Database (C++ engine) used for local storage of semantic embeddings.
- **`PII Redaction Scanner`**: A custom Python module that scrubs sensitive candidate data (Phone, Email, Aadhaar-style patterns) before vectorization.
- **`FastAPI Backend`**: A high-performance application layer that handles PDF extraction, triggers the PII scanner, and communicates with the Endee Engine.

---

## 🚀 Setup & Installation

### 1. Workspace Initialization

Create your project workspace to house both the database engine and the application logic.

```bash
# Create and enter the workspace
mkdir ResumeShield_Project
cd ResumeShield_Project
```

### 2. Set up Endee Vector DB

**Create Project Directory**

```
mkdir endee && cd endee
```

**Create docker-compose.yml**

Create a file named docker-compose.yml with the following content:

```
services:
  endee:
    image: endeeio/endee-server:latest
    container_name: endee-server
    ports:
      - "8080:8080"
    ulimits:
      nofile: 100000
    logging:
      driver: "json-file"
      options:
        max-size: "200m"
        max-file: "5"
    environment:
      NDD_NUM_THREADS: 0    # Automatic thread detection
      NDD_AUTH_TOKEN: ""    # Authentication token (optional)
    volumes:
      - endee-data:/data
    restart: unless-stopped

volumes:
  endee-data:

```

**Start Endee**

```
docker compose up -d
```

**Verify the Server is Running**

```
docker ps

```

You should see a container named endee-server

### 3. Clone the Application Repository

Using HTTP:

```
git clone https://github.com/Harshitha-Gangadharan/AI_compliance_checker.git
```

Using SSH:

```
git clone git@github.com:Harshitha-Gangadharan/AI_compliance_checker.git
```

### 4. Setting Up the Application

To ensure a clean development environment, we use a Python Virtual Environment (HG_venv) to manage dependencies for the FastAPI backend.

**Navigate to the application directory:**

```bash
cd ../ResumeShield_Project
```

**Step 1: Create the Virtual Environment This isolates our project libraries from the system-wide Python installation.**

```
python3 -m venv HG_venv
```

**Step 2: Activate the Environment On Ubuntu, run the following command to enter the virtual environment:**

```
source HG_venv/bin/activate
```

**Step 3: Install Project Requirements We install the core libraries required for AI processing and API development:**

```
pip install -r backend/requirements.txt
```

