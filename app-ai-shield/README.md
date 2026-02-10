# 🛡️ Resume-Shield AI (Compliance-First Screening)

This project was developed as a **technical test project for the internship selection process at Endee Labs**. It demonstrates a privacy-centric resume screening tool that integrates a local **PII Redaction Scanner** with the **Endee Labs Vector Engine** to ensure candidate data remains secure during AI processing.

---

## Overview of Project

**Resume-Shield AI** Privacy-First Semantic Recruitment Engine:

Resume-Shield AI is a vector-native recruitment platform built to bridge the gap between high-speed talent discovery and strict data privacy. In a world of increasing data regulations, we believe that:

This platform transforms the hiring pipeline by:

- **Zero-Trust Ingestion:** Automatically redacting PII (Names, Emails, Phone Numbers) before the data ever reaches the AI or the database..
- **Semantic Talent Discovery** Using 384-dimensional vector space to find candidates based on capability, not just keywords
- **Endee-Native Search:** Leveraging a high-performance C++ vector engine for sub-millisecond similarity matching.
- **Modular Architecture:** A clean separation between the React dashboard, the FastAPI gateway, and the Dockerized vector core.

---

## Problem Statement

Recruiters are currently trapped in a "Keyword Arms Race" where:

- **The Privacy Liability:** Storing raw resumes in plain text creates massive compliance risks (GDPR/CCPA).

- **The "Keyword Trap:** Qualified candidates are often filtered out simply because their terminology doesn't perfectly match a recruiter's specific search term.

- **Manual Bottlenecks:** Processing hundreds of resumes manually is slow and prone to unconscious bias.

---

## Solution:A Shielded Pipeline

**Resume-Shield AI** creates a secure "Intelligence Layer" that processes talent data through a specialized 5-stage pipeline:

1️⃣ **Secure Stream Parsing** Resumes are streamed via FastAPI and parsed into clean text using PyPDF2.

2️⃣ **PII Heuristics:** A custom scanner identifies and masks sensitive identifiers (Email, Phone, Names) to create a "Compliant Profile."

3️⃣ **Transformer Embedding:** The redacted profile is converted into a vector using the all-MiniLM-L6-v2 transformer model.

4️⃣ **Vector Persistence:** Storing vectors with int8d precision for optimized local performance

5️⃣ **Similarity Ranking:** Ranking candidates using cosine similarity to map job descriptions to the talent pool

---

## Technology Stack

### Frontend (The Dashboard)

- **React + Vite:** Optimized for high-speed development on Ubuntu.

- **Service Layer:** Modular Axios-based API client for clean separation of concerns.

- **Lucide Icons:** Visual cues for compliance and search status.

- **Tailwind CSS:** Professional "SaaS-style" dashboard layout.

---

### Backend (The Intelligence)

- **FastAPI:** Asynchronous Python framework managing the secure data flow.

- **Sentence-Transformers:** Generating semantic embeddings locally to ensure data never leaves the secure environment.

- **Compliance Heuristics:** Regex-based PII detection and redaction logic.

---

### Vector Core (The Engine)

Endee Engine: A C++ based vector database running in Docker.

Vector Specs: 384-dimension vectors with int8d precision.

Latency: Sub-10ms query response time for a seamless recruiter experience.

---

## Project Architecture

The system follows a modular architecture that prioritizes data privacy and local high-speed vector search.

- **`endee`**: The core Vector Database (C++ engine) used for local storage of semantic embeddings.
- **`PII Redaction Scanner`**: A custom Python module that scrubs sensitive candidate data (Phone, Email, Aadhaar-style patterns) before vectorization.
- **`FastAPI Backend`**: A high-performance application layer that handles PDF extraction, triggers the PII scanner, and communicates with the Endee Engine.

---

```
.
├── backend
│   ├── core
│   │   ├── embedder.py
│   │   ├── parser.py
│   │   └── scanner.py
│   ├── database.py
│   ├── main.py
│   ├── requirements.txt
│   └── services
│       └── endee_client.py
├── frontend
│   ├── eslint.config.js
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   └── vite.svg
│   ├── README.md
│   ├── src
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── assets
│   │   │   └── react.svg
│   │   ├── components
│   │   │   ├── SearchBox.jsx
│   │   │   └── UploadZone.jsx
│   │   ├── index.css
│   │   ├── main.jsx
│   │   └── services
│   │       └── api.js
│   └── vite.config.js
├── README.md
└── requirements.txt

```

## Setup & Installation

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
pip install -r app-ai-shield/requirements.txt
```

**Configure Environment Variables**
Create the .env file:

```
cd app-ai-shield
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

Step 2: Ensure your Hugging Face Token is set in .env file we created in /app-ai-shield

Step 3: Start the server on port 8000

Note:virtual Environment(HG_venv) should be active while u run the "uvicorn" command or app

```
cd app-ai-shield
uvicorn backend.main:app --reload --port 8000
```

Verification: Open http://localhost:8000/docs. If you see the Swagger UI, your backend is alive and ready.

Step 4: Start the Vite Frontend(Terminal 2)

```
#Open new terminal
# Navitage to the frontend directory(/endee/app-ai-shield/frontend)

# Install dependencies
npm install

# Start the Vite development server
npm run dev

```
