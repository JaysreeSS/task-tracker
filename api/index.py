import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("Error: set SUPABASE_URL and SUPABASE_KEY in environment")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# GET /api/tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    try:
        query = supabase.table("tasks").select("*")

        status_filter = request.args.get('status')
        priority_filter = request.args.get('priority')
        
        if status_filter:
            if status_filter.lower() == 'done':
                query = query.eq('is_done', True)
            elif status_filter.lower() == 'pending':
                query = query.eq('is_done', False)
                
        if priority_filter:
            query = query.eq('priority', priority_filter)
        
        response = query.order('due_date').execute()
        
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET /api/tasks/:id
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        response = supabase.table("tasks").select("*").eq("id", task_id).execute()
        if not response.data:
            return jsonify({"error": "Task not found"}), 404
        return jsonify(response.data[0]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# POST /api/tasks
@app.route('/api/tasks', methods=['POST'])
def create_task():
    try:
        data = request.json
        
        if not data or 'title' not in data or not data['title'].strip():
            return jsonify({"error": "Title is required"}), 400
            
        new_task = {
            "title": data['title'],
            "description": data.get('description', ''),
            "due_date": data.get('due_date') or None,
            "priority": data.get('priority', 'Medium'),
            "is_done": False
        }
        
        response = supabase.table("tasks").insert(new_task).execute()
        return jsonify(response.data[0]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# PUT /api/tasks/:id
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        data = request.json
        
        updated_fields = {}
        if 'title' in data: updated_fields['title'] = data['title']
        if 'description' in data: updated_fields['description'] = data['description']
        if 'due_date' in data: updated_fields['due_date'] = data['due_date'] or None
        if 'priority' in data: updated_fields['priority'] = data['priority']
        if 'is_done' in data: updated_fields['is_done'] = data['is_done']
        
        response = supabase.table("tasks").update(updated_fields).eq("id", task_id).execute()
        if not response.data:
            return jsonify({"error": "Task not found"}), 404
            
        return jsonify(response.data[0]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# DELETE /api/tasks/:id
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        response = supabase.table("tasks").delete().eq("id", task_id).execute()
        if not response.data:
            return jsonify({"error": "Task not found"}), 404
            
        return jsonify({"message": f"Task {task_id} successfully deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
