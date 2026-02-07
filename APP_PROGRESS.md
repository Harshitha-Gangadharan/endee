### 🚀 Project Repository & Internship Submission

To ensure a structured development process and clear version control for the **AI Compliance Checker**, the primary codebase is hosted in a dedicated repository. This repo contains the full implementation of the privacy-preserving screening logic and the integration with the Endee Labs vector database.

- **Project Name:** AI Compliance Checker (Resume-Shield)
- **Primary Repository:** [https://github.com/Harshitha-Gangadharan/AI_compliance_checker]

- **Read me File:** [https://github.com/Harshitha-Gangadharan/AI_compliance_checker/blob/main/README.md]

- **Status:** Internship Test Project

> **Note to Reviewers:** All core logic, including the vector database indexing and compliance modules, is being updated in the repository linked above. This fork serves as the primary tracking point for project milestones and progress updates.

---

**Progess:**

The development was executed over a structured 5-day sprint on an **Ubuntu-based ThinkPad-L480**.

### **Day 1: Environment Orchestration & Scalability**

- Initialized a containerized environment using Docker to isolate the **Endee Engine**.
- Configured `ulimits` and thread detection to optimize the C++ engine performance for local hardware.

### **Day 2: The Compliance Pipeline (Extraction & Masking)**

- Developed a robust parsing layer to extract structured text from varied PDF layouts.
- Engineered a custom PII Redaction Scanner to mask sensitive candidate data before it enters the AI pipeline.

### **Day 3: Vector Space Engineering & Ingestion**

- Interfaced with the **Endee SDK** to initialize high-precision indexes (`INT8D` precision).
- Successfully synchronized the embedding pipeline to commit vectors to the local engine.
