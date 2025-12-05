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

def delete_data(table_name, table_id):
    print(f'---------- Eliminando dato en {table_name} ----------')

    while True:
        check = input(f'¿Esta seguro(a) de querer eliminar un dato de {table_name}? (si/no) ')

        if check == 'no':
            print('Operación cancelada.')
            return
        elif check == 'si':
            break
        else:
            print('Respuesta no válida. Por favor introduzca "si" o "no".')

    while True:
        id_to_delete = input('ID: ')

        if not id_to_delete:
            print('Debe insertar un id obligatoriamente.')
        else:
            while True:
                double_check = input(f'¿Esta seguro(a) de querer elilminar este dato de {table_name}? (si/no) ')

                if double_check == 'no':
                    print('Doble verificación cancelada. Volviendo a la entrada del ID.')
                    break
                elif double_check == 'si':
                    try:
                        supabase.table(table_name).delete().eq(table_id, id_to_delete).execute()

                        print(f'Dato con el ID: {id_to_delete} en {table_name} eliminado con éxito.')
                    except Exception as e:
                         print(f'Ocurrió un error al intentar eliminar este dato: {e}.')
                    return
                else:
                   print('Respuesta no válida. Por favor, introduzca "si" o "no".')