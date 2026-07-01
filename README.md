# Task Tracker

## Project Overview

Task Tracker is a full-stack web application built and developed using Angular for the frontend, Flask for the backend REST API, and Supabase (PostgreSQL) as the database.

The application allows a user to:

* Create tasks
* View tasks sorted by due date
* Update task status (Done / Pending)
* Filter tasks by status and priority
* Delete tasks with confirmation

---

## Requirements Covered

### Functional Requirements Implemented

* Add a task with:

  * Title (required)
  * Description (optional)
  * Due Date (optional)
  * Priority (Low / Medium / High)

* View list of tasks sorted by nearest due date

* Mark task as Done / Pending with one click

* Delete task with confirmation prompt

* Filter tasks by:

  * Status (All / Pending / Done)
  * Priority

* Show counter:

  * X Pending
  * Y Done

### Additional Work

* Responsive task list UI
* Automatic UI refresh after CRUD actions
* Successful deployment using Vercel + Render

---

## Tech Stack

* Frontend:  
![Angular](https://img.shields.io/badge/Angular-DD0031?style=flat-square&logo=angular&logoColor=white)

* Backend:  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)

* Database:  
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white)

* Deployment:  
![Vercel](https://img.shields.io/badge/Frontend-Vercel-black?style=flat-square&logo=vercel&logoColor=white)
![Render](https://img.shields.io/badge/Backend-Render-46E3B7?style=flat-square)

---

## Project Structure

```bash
task-tracker/
│
├── frontend/              # Angular frontend
│   ├── src/
│   ├── package.json
│   ├── angular.json
│   └── vercel.json
│
├── backend/               # Flask backend
│   ├── app.py
│   └── requirements.txt
│
├── images/                # Screenshots
│
└── README.md
```

---

## Database Schema

```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    due_date DATE,
    priority VARCHAR(10) NOT NULL CHECK (priority IN ('Low', 'Medium', 'High')),
    is_done BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
```

---

## REST API Endpoints

| Method | Endpoint        | Description       |
| ------ | --------------- | ----------------- |
| GET    | /api/tasks      | Fetch all tasks   |
| GET    | /api/tasks/<id> | Fetch single task |
| POST   | /api/tasks      | Create new task   |
| PUT    | /api/tasks/<id> | Update task       |
| DELETE | /api/tasks/<id> | Delete task       |

---

## Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/JaysreeSS/task-tracker.git
cd task-tracker
```

---

## 2. Backend Setup

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Create `.env` file inside backend:

```env
SUPABASE_URL=<your-supabase-url>
SUPABASE_KEY=<your-supabase-key>
```

Run backend:

```bash
python backend/app.py
```

Backend runs at:

```text
http://127.0.0.1:5000
```

---

## 3. Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run Angular app:

```bash
npm start
```

Frontend runs at:

```text
http://localhost:4200
```

---

## Deployment

### Production Architecture

```text
Frontend (Vercel)
      ↓
Backend API (Render)
      ↓
Supabase Database
```

---

## Screenshots

### Project Setup
#### Backend Running
![backend running](/images/backend-running.png)

#### Frontend Running
![frontend running](/images/frontend-running.png)

### Database Setup
#### Tasks table schema
![Database Schema](/images/db-schema.png)

#### Seed data
![Seed Data](/images/db-seed.png)

### Core Features
#### Task Form with Counter
![Task Form](/images/task-form.png)

#### Task Created Successfully
![Task Created](/images/task-created.png)

#### Full Task List, sorted nearest due date
![Full Tasks](/images/full-task.png)

#### Filter by Status
![Status Filter](/images/status-filter.png)

#### Filter by Priority
![Priority Filter](/images/priority-filter.png)

#### Delete Confirmation
![Delete](/images/delete-confirm.png)

### API Testing
#### GET
![GET API](/images/get-api.png)

#### POST
![POST API](/images/post-api.png)

#### PUT
![PUT API](/images/put-api.png)

#### DELETE
![DELETE API](/images/delete-api.png)

---

## Features Working

* Create task
* Read tasks
* Update task status
* Delete task
* Sort by due date
* Filter by status
* Filter by priority
* Pending/Done counter
* Auto-refresh UI after updates

---

## Features Not Implemented

* Search by task title
* Pagination

These were listed as stretch goals and were not completed due to time constraints.

---

## Assumptions

* Single-user application (no authentication)
* Tasks are managed by one user only
* Priority values are restricted to:

  * Low
  * Medium
  * High
* Due date is optional

---

## Challenges Faced

* Configuring frontend and backend communication
* Handling Angular API integration with Flask
* Deploying Angular frontend on Vercel
* Deploying Flask backend on Render
* Managing environment-based API configuration

---

## Future Improvements

Given more time, I would implement:

* Search functionality
* Pagination
* Authentication
* Better UI/UX
* Full cloud deployment with CI/CD

---

## Final Note

This project successfully implements the core requirements of the Task Tracker with working CRUD operations, filtering, sorting, counters, and deployment.

The remaining work includes optional stretch goals such as search and pagination.