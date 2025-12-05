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

def read_data(table_name):
    print(f'---------- {table_name} ----------')

    try:
        data_select = supabase.table(table_name).select('*').execute()

        if data_select.data == []:
            print('No hay datos registrados.')
        else:
            print(data_select)
    except Exception as e:
        print(f'Ocurrió un error al intentar ver los datos registrados: {e}')