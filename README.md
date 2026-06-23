# Task Tracker

## Project Overview

Task Tracker is a simple web app for organizing personal tasks. It lets users create, view, update, and delete tasks while tracking status, priority, and due dates through an Angular frontend and Flask backend.

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

## Vercel Deployment

This project is configured for Vercel using `vercel.json` and the API function in `api/index.py`.

1. Connect the repository to Vercel or install the Vercel CLI:

```bash
npm install -g vercel
```

2. From the project root, run:

```bash
vercel
```

3. In the Vercel dashboard, add these environment variables for the project:

```text
SUPABASE_URL=<your-supabase-url>
SUPABASE_KEY=<your-supabase-key>
```

4. Deploy using GitHub integration or:

```bash
vercel --prod
```

5. After deployment, the frontend is served from the Vercel domain and the backend API is available at `/api/tasks`.

> On local development, the app uses `http://127.0.0.1:5000/api/tasks` when running on `localhost`, and on Vercel it uses the relative API path `/api/tasks`.

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
