import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
from read import read_data

try:
    url: str = os.environ.get('SUPABASE_URL')
    key: str = os.environ.get('SUPABASE_KEY')
    supabase: Client = create_client(url, key)
except Exception as e:
    print(f"Error al inicializar el cliente de Supabase: {e}")
    exit(1)

def update_data(table_name, table_id, table_data):
    print(f'---------- Editando dato en {table_name} ----------')

    if table_name != 'productos':
        while True:
            if table_name == 'compañias':
                read_data('compañias')
            if table_name == 'categorias':
                read_data('compañias')
            else:
                pass

            id_to_update = int(input('ID: '))
            if not id_to_update:
                print('Debe insertar un id obligatoriamente.')
            else:
                break

        while True: 
            new_name = input('Nuevo nombre: ').strip()
            if not new_name:
                print('Debe insertar el nombre obligatoriamente.')
            else:
                break

        try:
            supabase.table(table_name).update({table_data: new_name}).eq(table_id, id_to_update).execute()

            print(f'Datos con el ID: {id_to_update} editado con éxito.')
        except Exception as e:
            print(f'Ocurrió un error al intentar editar el dato: {e}.')
    else:
        pass

    if table_name == 'productos':
        while True:
            read_data('productos')
            id_to_update = int(input('ID del producto: '))
            if not id_to_update:
                print('Debe insertar un id obligatoriamente.')
            else:
                break
        
        while True:
            read_data('categorias')
            new_category = int(input('ID de la nueva categoría del producto: '))
            if not new_category:
                print('Debe insertar la categoría obligatoriamente.')
            else: 
                break

        while True:
            read_data('compañias')
            new_company = int(input('ID de la nueva compañía del producto: '))
            if not new_company:
                print('Debe insertar la compañía obligatoriamente.')
            else: 
                break

        while True: 
            new_name = input('Nuevo nombre del producto: ').strip()
            if not new_name:
                print('Debe insertar el nombre obligatoriamente.')
            else:
                break

        while True:
            new_weight = int(input('Nuevo peso del producto (en gramos): '))
            if not new_weight:
                print('Debe insertar el peso obligatoriamente.')
            else:
                break
        
        while True:
            new_stock = int(input('Nueva cantidad del producto: '))
            if not new_stock:
                print('Debe insertar la cantidad obligatoriamente.')
            else: 
                break
        
        while True:
            new_exp_date = int(input('Nueva fecha de expiración (YYMMDD): '))
            if not new_exp_date:
                print('Debe insertar la fecha obligatoriamente.')
            else: 
                break
        try:
            supabase.table('productos').update({'id_categoria': new_category,'id_compañía': new_company, 'nombre_producto': new_name, 'peso_producto_gramos': new_weight,'cantidad_stock': new_stock,'fecha_exp': new_exp_date}).eq('id_producto', id_to_update).execute()

            print(f'Producto con el ID: {id_to_update} editado con éxito.')
        except Exception as e:
            print(f'Ocurrió un error al intentar editar el producto: {e}.')
    else:
        pass