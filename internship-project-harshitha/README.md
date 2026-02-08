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

Clone your forked repository which contains both the Endee core and the internship project..

Using HTTP:

```
git clone https://github.com/Harshitha-Gangadharan/endee.git
```

Using SSH:

```
git clone git@github.com:Harshitha-Gangadharan/endee.git
```

### 2. Set up Endee Vector DB

Change dir

```
cd endee

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

### 3. Setting Up the Application

We use a Python Virtual Environment (venv) to manage dependencies for the FastAPI backend located in the internship folder.

Step 1: Create the Virtual Environment This isolates your project libraries from the system-wide Python installation.

```
python3 -m venv HG_venv
```

Step 2: Activate the Environment

```
source venv/bin/activate
```

Step 3: Install Project Requirements

```
pip install -r internship-project-harshitha/requirements.txt
```

**Configure Environment Variables**
Create the .env file:

```
cd internship-project-harshitha
touch .env
```

Add your Hugging Face token to the file. Open it with your preferred editor and insert the following line:

```
HF_TOKEN="your_hugging_face_token_here"
```

How to Obtain Your Hugging Face Token
Follow these brief steps to generate your access key:

1.  Login: Sign in to your account at huggingface.co.

2.  Settings: Click your profile icon in the top-right corner and select Settings.

3.  Access Tokens: Select Access Tokens from the left-side navigation menu.

4.  Generate: Click New token, provide a name, and select the Read role

5.  Copy: Copy the token and paste it into the .env file you created.

### 4. Running the Application

Step 1: Activate the Environment from the root(i.e endee)

```
source HG_venv/bin/activate
```

Step 2: Ensure your Hugging Face Token is set in .env file we created in /internship-project-harshitha

Step 3: Start the server on port 8000

```
uvicorn backend.main:app --reload --port 8000
```

Verification: Open http://localhost:8000/docs. If you see the Swagger UI, your backend is alive and ready.

Step 4: Start the Vite Frontend(Terminal 2)

```
#Open new terminal
# Navitage to the frontend directory(/endee/internship-project-harshitha/frontend)

# Install dependencies
npm install

# Start the Vite development server
npm run dev

```
