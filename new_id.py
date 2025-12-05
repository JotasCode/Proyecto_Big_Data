import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

try:
    url: str = os.environ.get('SUPABASE_URL')
    key: str = os.environ.get('SUPABASE_KEY')
    supabase: Client = create_client(url, key)
except Exception as e:
    print(f"Error al inicializar el cliente de Supabase: {e}")
    exit(1)

def new_id(table_name, table_id):
    id_data = supabase.table(table_name).select(table_id).order(table_id, desc=True).limit(1).execute()
    lates_id = id_data.data[0][table_id]

    if len(id_data.data) == 0:
        return 1  
    else:
        return lates_id + 1