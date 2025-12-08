from spb_con import supabase
import pandas as pd

def from_table_to_csv(table_name):
    try:
        response = supabase.table(table_name).select("*").execute()

        if not response.data:
            print(f"No se encontraron datos en la tabla '{table_name}'.")
            return
        
        df = pd.DataFrame(response.data)
        df.to_csv(f'{table_name}.csv', index=False) 

        print('-' * 60)
        print(f'Los datos de la tabla {table_name} pasaron al archivo {table_name}.csv de forma exitosa.')

    except Exception as e:
        print('-' * 60)
        print(f'Ocurrió un error al intentar crear el archivo {table_name}.csv: {e}')