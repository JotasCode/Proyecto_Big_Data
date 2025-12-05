import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
from read import read_data
from new_id import new_id

try:
    url: str = os.environ.get('SUPABASE_URL')
    key: str = os.environ.get('SUPABASE_KEY')
    supabase: Client = create_client(url, key)
except Exception as e:
    print(f"Error al inicializar el cliente de Supabase: {e}")
    exit(1)

#FUNCIÓN PARA CREAR
def create_data(table_name, table_id, table_data):
    print(f'---------- Registrando dato en {table_name}----------')

    if table_name != 'productos':
        while True:
            name = input('Nombre: ').strip()
            if not name:
                print('Debe insertar el nombre obligatoriamente.')
            else:
                break
        
        try:
            supabase.table(table_name).insert({table_id: new_id(table_name, table_id),table_data: name}).execute()

            print(f'Dato con el nombre {name} creado con éxito.')
        except Exception as e:
            print(f'Ocurrió un error al intentar crear el dato: {e}.')
    else:
        pass

    if table_name == 'productos':
        while True:
            read_data('categorias')
            category = int(input('ID de la categoría del producto: '))
            if not category:
                print('Debe insertar la categoría obligatoriamente.')
            else: 
                break

        while True:
            read_data('compañias')
            company = int(input('ID de la compañía del producto: '))
            if not company:
                print('Debe insertar la compañía obligatoriamente.')
            else: 
                break

        while True:
            name = input('Nombre del producto: ').strip()
            if not name:
                print('Debe insertar el nombre obligatoriamente.')
            else:
                break

        while True:
            weight = int(input('Peso del producto (en gramos): '))
            if not weight:
                print('Debe insertar el peso obligatoriamente.')
            else: 
                break

        while True:
            stock = int(input('Cantidad del producto: '))
            if not stock:
                print('Debe insertar la cantidad obligatoriamente.')
            else: 
                break

        while True:
            exp_date = int(input('Fecha de expiración (YYMMDD): '))
            if not exp_date:
                print('Debe insertar la feca obligatoriamente.')
            else: 
                break
        
        try:
            supabase.table('productos').insert({'id_producto': new_id('productos', 'id_producto'),'id_categoria': category,'id_compañia': company,'nombre_producto': name, 'peso_producto_gramos': weight,'cantidad_stock': stock, 'fecha_exp': exp_date}).execute()

            print(f'Producto {name} creado con éxito.')
        except Exception as e:
            print(f'Ocurrió un error al intentar crear el producto: {e}.')
    else:
        pass