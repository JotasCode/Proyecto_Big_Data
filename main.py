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

#Tabla de productos

def new_products_id():
    id_data = supabase.table("productos").select("id_producto").order("id_producto", desc=True).limit(1).execute()

    if len(id_data.data) == 0:
        return 1  
    else:
        lates_id = id_data.data[0]["id_producto"]
        return lates_id + 1 

def create_products_data():
    print('---------- Registrando producto ----------')

    while True:
        category = int(input('ID de la categoría del producto: '))
        if not category:
            print('Debe insertar la categoría obligatoriamente.')
        else: 
            break

    while True:
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
        exp_date = int(input('Fecha de expiración: '))
        if not exp_date:
            print('Debe insertar la feca obligatoriamente.')
        else: 
            break

    supabase.table('productos').insert({'id_producto': new_products_id(),'id_categoria': category,'id_compañía': company,'nombre_producto': name, 'peso_producto_gramos': weight,'cantidad_stock': stock, 'fecha_exp': exp_date}).execute()

def read_products_data():
    print('---------- Productos ----------')

    data_select = supabase.table('productos').select('*').execute()

    if data_select.data == []:
        print('No hay productos registrados.')
    else:
        print(data_select)

def update_products_data():
    print('---------- Actualizando registro ----------')

    while True:
        new_category = int(input('ID de la nueva categoría del producto: '))
        if not new_category:
            print('Debe insertar la categoría obligatoriamente.')
        else: 
            break

    while True:
        new_company = int(input('ID de la nueva compañía del producto: '))
        if not new_company:
            print('Debe insertar la compañía obligatoriamente.')
        else: 
            break
    
    while True:
        id_to_update = int(input('ID del producto: '))
        if not id_to_update:
            print('Debe insertar un id obligatoriamente.')
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
        new_exp_date = int(input('Nueva fecha de expiración: '))
        if not new_exp_date:
            print('Debe insertar la fecha obligatoriamente.')
        else: 
            break

    supabase.table('productos').update({'id_categoria': new_category,'id_compañía': new_company, 'nombre_producto': new_name, 'peso_producto_gramos': new_weight,'cantidad_stock': new_stock,'fecha_exp': new_exp_date}).eq('id_producto', id_to_update).execute()

def delete_products_data():
    print('---------- Eliminando producto ----------')

    while True:
        check = input('¿Esta seguro(a) de querer eliminar un produto? (si/no) ')

        if check == 'no':
            print('Operación cancelada.')
            return
        elif check == 'si':
            break
        else:
            print('Respuesta no válida. Por favor, introduzca "si" o "no".')

    while True:
        id_to_delete = input('ID del producto: ')

        if not id_to_delete:
            print('Debe insertar un id obligatoriamente.')
        else:
            while True:
                double_check = input('¿Estas seguro(a) de querer elilminar este producto? (si/no) ')

                if double_check == 'no':
                    print('Doble verificación cancelada. Volviendo a la entrada del ID.')
                    break
                elif double_check == 'si':
                    try:
                        supabase.table('productos').delete().eq('id_producto', id_to_delete).execute()

                        print(f'Producto con ID {id_to_delete} eliminado con éxito.')
                    except Exception as e:
                         print(f'Ocurrió un error al eliminar el producto: {e}')
                    return
                else:
                   print('Respuesta no válida. Por favor, introduzca "si" o "no".')

def menu():
    print('-' * 60)
    print('Programa de registro de inventario.')

    while True:
        print('-' * 60)
        print('1. Registrar producto.')
        print('2. Ver productos registrados.')
        print('3. Alctualizar registro.')
        print('4. Eliminar producto.')
        print('-' * 60)
        print('5. Salir.')
        print('-' * 60)

        selection = int(input('Por favor seleccione un opción: '))

        if selection == 1:
            create_products_data()
        elif selection == 2:
            read_products_data()
        elif selection == 3:
            update_products_data()
        elif selection == 4:
            delete_products_data()
        elif selection == 5:
            print('-' * 60)
            print('Gracias por utilizar nuestros servicios, hasta la próxima.')
            print('-' * 60)
            break
        else:
            print('-' * 60)
            print('Opción invalida. Seleccione el numero de la opción que desea elegir.')

if __name__ == '__main__':
    menu()
else:
    print('El programa que quieres utilzar no se encuentra en el archivo que seleccionaste.')