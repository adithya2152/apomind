import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize Supabase Client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_user_data(user_id):
    """Fetch user's learning data from Supabase"""
    response = supabase.table("ques_dir").select("*").eq("direction_id", user_id).execute()
    if response.data:
        return response.data[0]  # Return first matching row
    return None
