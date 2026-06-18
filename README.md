# Task Tracker

## Project Overview

Task Tracker is for managing tasks with CRUD operations. 

## Tech Stack

- Frontend: Angular
- Backend: Python Flask
- Database/API: Supabase (PostgreSQL)

## Setup

### Backend

1. Install Python packages:

```bash
python -m pip install flask flask-cors python-dotenv supabase
```

2. Create a `.env` file with:

```env
SUPABASE_URL=<your-supabase-url>
SUPABASE_KEY=<your-supabase-key>
```

3. Start the backend server:

```bash
python backend/app.py
```

![backend running](/images/image.png)

### Frontend

1. Change to the frontend folder:

```bash
cd frontend
```

2. Install npm dependencies:

```bash
npm install
```

3. Run the Angular development server:

```bash
npm start
```

4. Open the app in your browser:

```text
http://localhost:4200/
```

![frontend running](/images/image-1.png)

## Works Implemented

- Repository creation in GitHub with README file
- Set up Supabase database and created the table
  ![Table creation in Supabase](/images/image-2.png)
- Counter showing pending and done
- Create tasks with title, description, priority, and due date
- Browser alert popup on successful task creation
  ![creation](/images/image-5.png)
- List of Tasks sorted by nearest due date
  ![sorted tasks list](/images/image-6.png)
- Filter tasks by status and priority
- Mark tasks as done or pending
  ![Filter and Status](/images/image-3.png)
- Delete tasks with confirmation
  ![Delete](/images/image-4.png)
- The list updates automatically after task creation, status changes, and deletion.

## Works not Implemented

- A search box that filters by title
- Pagination

## Notes

- The frontend expects the backend API at `http://127.0.0.1:5000/api/tasks`.
- There is no authentication, and the app is intended as a basic demo task tracker.
