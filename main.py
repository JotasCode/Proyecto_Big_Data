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
    
#Tabla de comapñías

def create_companys_data():
    print('---------- Registrando compañía ----------')

    while True:
        name = input('Nombre de la compañía: ').strip()
        if not name:
            print('Debe insertar el nombre obligatoriamente.')
        else:
            break
    
    try:
        supabase.table('compañias').insert({'id_compañia': new_id('compañias', 'id_compañia'),'nombre_compañia': name}).execute()

        print(f'Compañía {name} creada con éxito.')
    except Exception as e:
        print(f'Ocurrió un error al intentar crear la compañía: {e}.')

def update_companys_data():
    print('---------- Editando registro ----------')
    
    while True:
        id_to_update = int(input('ID de la compañía: '))
        if not id_to_update:
            print('Debe insertar un id obligatoriamente.')
        else:
            break

    while True: 
        new_name = input('Nuevo nombre de la compañía: ').strip()
        if not new_name:
            print('Debe insertar el nombre obligatoriamente.')
        else:
            break

    try:
        supabase.table('compañias').update({'nombre_compañia': new_name}).eq('id_compañia', id_to_update).execute()

        print(f'Compañía con el ID: {id_to_update} editada con éxito.')
    except Exception as e:
        print(f'Ocurrió un error al intentar editar la compañía: {e}.')

#Tabla de categorías

def create_categorys_data():
    print('---------- Registrando categoría ----------')

    while True:
        name = input('Nombre de la categoría: ').strip()
        if not name:
            print('Debe insertar el nombre obligatoriamente.')
        else:
            break
    
    try:
        supabase.table('categorias').insert({'id_categoria': new_id('categorias', 'id_categoria'),'nombre_categoria': name}).execute()

        print(f'Categoría {name} creada con éxito.')
    except Exception as e:
        print(f'Ocurrió un error al intentar crear la categoría: {e}.')

def update_categorys_data():
    print('---------- Editando categoría ----------')
    
    while True:
        id_to_update = int(input('ID de la categoría: '))
        if not id_to_update:
            print('Debe insertar un id obligatoriamente.')
        else:
            break

    while True: 
        new_name = input('Nuevo nombre de la categoría: ').strip()
        if not new_name:
            print('Debe insertar el nombre obligatoriamente.')
        else:
            break

    try:
        supabase.table('categorias').update({'nombre_categoria': new_name}).eq('id_categoria', id_to_update).execute()

        print(f'Categoría con el ID: {id_to_update} editada con éxito.')
    except Exception as e:
        print(f'Ocurrió un error al intentar editar la categoría: {e}.')

#Tabla de productos

def create_products_data():
    print('---------- Registrando producto ----------')

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

def update_products_data():
    print('---------- Editando registro ----------')

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

#Menú

def menu():
    print('-' * 60)
    print('Programa de registro de inventario.')

    while True:
        print('-' * 60)
        print('---------- Opciones ----------')
        print('-' * 60)
        print('1. Compañías')
        print('2. Categorías')
        print('3. Productos')
        print('-' * 60)
        print('4. Salir.')
        print('-' * 60)

        selection = input('Por favor seleccione un opción: ')

        if selection == '1':
            while True:
                print('-' * 60)
                print('---------- Elegiste la opción de Compañías ----------')
                print('-' * 60)
                print('1. Registrar compañía.')
                print('2. Ver compañías registradas.')
                print('3. Editar registro de compañía.')
                print('4. Eliminar compañía.')
                print('-' * 60)
                print('5. Salir.')
                print('-' * 60)

                companys_selection = input('Por favor seleccione un opción: ')

                if companys_selection == '1':
                    create_companys_data()
                elif companys_selection == '2':
                    read_data('compañias')
                elif companys_selection == '3':
                    update_companys_data()
                elif companys_selection == '4':
                    delete_data('compañias', 'id_compañia')
                elif companys_selection == '5':
                    print('-' * 60)
                    print('Saliendo del registro de compañías.')
                    print('-' * 60)
                    break
                else:
                    print('-' * 60)
                    print('Opción invalida. Seleccione el número de la opción que desea elegir.')

        elif selection == '2':
            while True:
                print('-' * 60)
                print('---------- Elegiste la opción de Categorías ----------')
                print('-' * 60)
                print('1. Registrar categoría.')
                print('2. Ver categorías registradas.')
                print('3. Editar registro de categoría.')
                print('4. Eliminar categoría.')
                print('-' * 60)
                print('5. Salir.')
                print('-' * 60)

                categorys_selection = input('Por favor seleccione un opción: ')

                if categorys_selection == '1':
                    create_categorys_data()
                elif categorys_selection == '2':
                    read_data('categorias')
                elif categorys_selection == '3':
                    update_categorys_data()
                elif categorys_selection == '4':
                    delete_data('categorias', 'id_categoria')
                elif categorys_selection == '5':
                    print('-' * 60)
                    print('Saliendo del registro de categorías.')
                    print('-' * 60)
                    break
                else:
                    print('-' * 60)
                    print('Opción invalida. Seleccione el número de la opción que desea elegir.')

        elif selection == '3':
            while True:
                print('-' * 60)
                print('---------- Elegiste la opción de Productos ----------')
                print('-' * 60)
                print('1. Registrar producto.')
                print('2. Ver productos registrados.')
                print('3. Editar registro.')
                print('4. Eliminar producto.')
                print('-' * 60)
                print('5. Salir.')
                print('-' * 60)

                products_selection = input('Por favor seleccione un opción: ')

                if products_selection == '1':
                    create_products_data()
                elif products_selection == '2':
                    read_data('productos')
                elif products_selection == '3':
                    update_products_data()
                elif products_selection == '4':
                    delete_data('productos', 'id_productos')
                elif products_selection == '5':
                    print('-' * 60)
                    print('Saliendo del registro de productos.')
                    print('-' * 60)
                    break
                else:
                    print('-' * 60)
                    print('Opción invalida. Seleccione el número de la opción que desea elegir.')

        elif selection == '4':
            print('-' * 60)
            print('Gracias por utilizar nuestros servicios, hasta la próxima.')
            print('-' * 60)
            break

        else:
            print('-' * 60)
            print('Opción invalida. Seleccione el número de la opción que desea elegir.')

if __name__ == '__main__':
    menu()
else:
    print('No puedes ejecutar este programa.')