import os
from supabase import create_client, Client

# Setting up Supabase
os.environ["SUPABASE_URL"] = "https://lhwzdmbnwcjerfvtlzsn.supabase.co"
os.environ["SUPABASE_KEY"] = "sb_publishable_tt4_ts4iYz7gqyusuvQtFA_LPuB481S"

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def test_sdk_crud():
    try:
        # CREATE
        new_task = {
            "title": "Learn Angular Basics",
            "description": "Watch a 10 min tutorial",
            "priority": "High",
        }
        response = supabase.table("tasks").insert(new_task).execute()
        created_id = response.data[0]['id']
        print(f"Created Task with ID: {created_id}\n")

        # READ
        read_response = supabase.table("tasks").select("*").execute()
        print(f"Fetched Tasks: {read_response.data}\n")

        # UPDATE
        update_response = supabase.table("tasks").update({"is_done": True}).eq("id", created_id).execute()
        print(f"Updated Task {created_id} 'is_done' to True\n")

        # DELETE
        delete_response = supabase.table("tasks").delete().eq("id", created_id).execute()
        print(f"Deleted Task {created_id} successfully!\n")

        print("Success!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_sdk_crud()