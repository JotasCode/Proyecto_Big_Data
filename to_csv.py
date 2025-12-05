import os
from supabase import create_client, Client
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

try:
    url: str = os.environ.get('SUPABASE_URL')
    key: str = os.environ.get('SUPABASE_KEY')
    supabase: Client = create_client(url, key)
except Exception as e:
    print(f"Error al inicializar el cliente de Supabase: {e}")
    exit(1)

def from_table_to_csv(table_name, csv_name):
    try:
        response = supabase.table(table_name).select("*").execute()

        if not response.data:
            print(f"No se encontraron datos en la tabla '{table_name}'.")
            return
        
        df = pd.DataFrame(response.data)
        df.to_csv(csv_name, index=False) 

        print('-' * 60)
        print(f'Los datos de la tabla {table_name} pasaron al archivo {csv_name} de forma exitosa.')

    except Exception as e:
        print('-' * 60)
        print(f'Ocurrió un error al intentar crear el archivo {csv_name}: {e}')