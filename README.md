# 💼 Job Portal With Automation

A scalable **microservice-based Job Portal application** built using **React, Node.js, Spring Boot, FastAPI, .NET, and MySQL**. The application provides separate functionality for **Job Seekers and Employers**, along with AI chatbot support and automated job-alert notifications.

---

## 🛠️ Development Responsibility

This project was developed as a collaborative application, with the backend and service architecture divided into multiple technologies.

My major responsibilities included:

- Developing the **React frontend** and integrating it with backend APIs.
- Developing the main backend using **Java and Spring Boot**.
- Designing and managing the **MySQL database**.
- Implementing **authentication and authorization using Spring Security and JWT**.
- Developing the **Node.js API Gateway** for communication between frontend and backend services.
- Implementing the **AI-based chatbot using FastAPI and Python**.
- Implementing the **registration email notification service using .NET**.
- Implementing **automated job-alert notifications using Spring Scheduler**.
- Containerizing the complete application using **Docker and Docker Compose**.
- Configuring service-to-service communication using a **Docker bridge network**.

---

# ✨ Key Features

### 🔐 Secure Authentication

- JWT-based Authentication
- Spring Security
- Role-Based Authorization
- Separate functionality for Job Seekers and Employers
- Secure password handling

### 💼 Job Management

- Employers can create and manage job postings.
- Job Seekers can search and view available jobs.
- Job Seekers can apply for suitable jobs.
- Job-related data is stored in MySQL.

### 🤖 AI Chatbot

- AI-based chatbot developed using **FastAPI and Python**.
- Helps users interact with job-related information.
- Chatbot communicates with the Spring Boot backend.
- Uses the configured **Groq API** for AI functionality.

### 📧 Registration Email Notification

- Implemented a separate **.NET microservice** for registration emails.
- When a user registers successfully, the Spring Boot backend can communicate with the .NET service.
- The .NET service sends a registration-success email using **SMTP and MailKit**.

### 🔔 Automated Job Alerts

- Implemented using **Spring Scheduler**.
- The scheduler automatically checks job/user-related data.
- Relevant users can receive job-alert notifications.

---

# 👥 User Roles

## 🧑‍💼 Job Seeker

A Job Seeker can:

1. Register and log in.
2. Search for jobs.
3. View job details.
4. Apply for jobs.
5. Manage profile information.
6. Use the AI chatbot.
7. Receive job-related notifications.

## 🏢 Employer

An Employer can:

1. Register and log in.
2. Create job postings.
3. Manage job postings.
4. View applications.
5. Manage employer-related information.

---

# 🏗️ System Architecture

The project follows a **microservice-based architecture**.

```text
                         User
                           |
                           v
                    React Frontend
                           |
                           v
                         Nginx
                           |
                           v
                  Node.js API Gateway
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
   Spring Boot          FastAPI          .NET Service
     Backend            Chatbot          Email Service
          |                |                |
          v                v                v
       MySQL          Spring Boot       SMTP Server
````

The services communicate through the Docker Compose network:

```text
jobportal-network
```

---

# 🌐 Request Flow

A general API request follows this flow:

```text
React
  ↓
Nginx
  ↓
Node.js API Gateway
  ↓
Required Microservice
  ↓
Spring Boot / FastAPI / .NET
  ↓
Database / External Service
  ↓
Response
  ↓
React
```

The **Node.js API Gateway** acts as the central entry point for API communication.

---

# 🛠️ Tech Stack

| Technology           | Purpose                                         |
| -------------------- | ----------------------------------------------- |
| **React**            | Frontend user interface                         |
| **Axios**            | API communication                               |
| **Redux Toolkit**    | Global/shared frontend state                    |
| **Nginx**            | Serves React production build and reverse proxy |
| **Node.js**          | API Gateway                                     |
| **Express.js**       | Gateway server/API handling                     |
| **Java**             | Main backend programming language               |
| **Spring Boot**      | Main backend and business logic                 |
| **Spring Security**  | Authentication and authorization                |
| **JWT**              | Token-based authentication                      |
| **MySQL**            | Relational database                             |
| **FastAPI**          | AI chatbot backend                              |
| **Python**           | Chatbot service                                 |
| **Groq API**         | AI functionality                                |
| **.NET 10**          | Registration email microservice                 |
| **MailKit**          | SMTP email sending                              |
| **Spring Scheduler** | Automated job alerts                            |
| **Docker**           | Containerization                                |
| **Docker Compose**   | Multi-container application deployment          |

---

# 📂 Main Project Structure

```text
Job-Portal-With-Automation/
│
├── frontend/
│   └── React application
│
├── gateway/
│   └── Node.js API Gateway
│
├── backend/
│   └── spring_boot_backend_template/
│       └── Spring Boot application
│
├── chatbot/
│   └── FastAPI + Python chatbot
│
├── RegistrationEmailService/
│   └── .NET email service
│
├── compose.yml
│
└── README.md
```

---

# 🐳 Docker & Deployment

Each major service is containerized using Docker.

The Docker Compose file contains:

```text
mysql
email-service
backend
chatbot
gateway
frontend
```

### Important Port Mappings

| Service             | Host Port | Container Port |
| ------------------- | --------: | -------------: |
| Frontend / Nginx    |    `5173` |           `80` |
| API Gateway         |    `5000` |         `5000` |
| Spring Boot Backend |    `9090` |         `9090` |
| FastAPI Chatbot     |    `8000` |         `8000` |
| .NET Email Service  |    `5001` |         `8080` |
| MySQL               |    `3307` |         `3306` |

All services are connected through:

```text
jobportal-network
```

Inside Docker, services communicate using **service names**.

For example:

```text
backend:9090
chatbot:8000
email-service:8080
mysql:3306
```

---

# 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>

cd Job-Portal-With-Automation
```

### 2. Configure Environment Variables

Configure the required environment variables:

```text
MYSQL_ROOT_PASSWORD
MYSQL_DATABASE
JWT_SECRET
GROQ_API_KEY
SMTP_EMAIL
SMTP_PASSWORD
CLOUDINARY_CLOUD_NAME
CLOUDINARY_API_KEY
CLOUDINARY_API_SECRET
```

### 3. Build and Start the Application

From the directory containing `compose.yml`:

```bash
docker compose up -d --build
```

This command:

```text
Build Docker Images
        ↓
Create Containers
        ↓
Create Network
        ↓
Start Services
        ↓
Run Health Checks
        ↓
Application Ready
```

### 4. Check Running Containers

```bash
docker compose ps
```

### 5. View Logs

```bash
docker compose logs
```

For a particular service:

```bash
docker compose logs backend
```

### 6. Stop the Application

```bash
docker compose down
```

To also remove Docker-managed volumes:

```bash
docker compose down -v
```

> `docker compose down -v` removes the MySQL volume and therefore removes the persisted database data stored in that volume.

---

# 📧 Registration Email Flow

The registration email functionality is implemented as a separate .NET service.

```text
User
 ↓
React Registration Form
 ↓
Nginx
 ↓
Node.js API Gateway
 ↓
Spring Boot Backend
 ↓
MySQL
 ↓
.NET Email Service
 ↓
SMTP Server
 ↓
User's Email
```

The .NET service provides:

```text
POST /api/registration-email/send
```

The request contains:

```json
{
  "name": "User Name",
  "email": "user@example.com",
  "role": "JOB_SEEKER"
}
```

The .NET service creates the HTML email and sends it through SMTP using **MailKit**.

---

# 🔔 Job Alert Automation Flow

The application also includes automated job-alert processing.

```text
Spring Scheduler
       ↓
Check job/user data
       ↓
Find relevant users
       ↓
Process notification
       ↓
Send job alert
```

The purpose of the scheduler is to perform job-related notification tasks automatically without requiring the user to trigger them manually.

---

# ❤️ Why Microservices?

The application uses separate services for different responsibilities.

```text
Spring Boot
     ↓
Main business logic

Node.js
     ↓
API Gateway

FastAPI
     ↓
AI Chatbot

.NET
     ↓
Email Notification

MySQL
     ↓
Data Storage
```

This separation makes the system easier to maintain because each service has a specific responsibility.

---

# 🔒 Security

Security is implemented mainly in the Spring Boot backend using:

* Spring Security
* JWT authentication
* Role-based authorization
* Secure authentication flow

The backend validates the user's authentication and authorization before allowing protected operations.

---

# 📌 Key Project Highlights

* Microservice-based Job Portal.
* React-based frontend.
* Node.js API Gateway.
* Nginx reverse proxy and production frontend server.
* Spring Boot main backend.
* Spring Security + JWT.
* MySQL database.
* FastAPI AI chatbot.
* Groq API integration.
* .NET registration email microservice.
* SMTP email notification using MailKit.
* Automated job alerts using Spring Scheduler.
* Docker containerization.

---


```
```