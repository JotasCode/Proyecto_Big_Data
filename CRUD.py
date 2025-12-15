import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
from new_id import new_id
from spb_con import supabase

#FUNCIÓN PARA CREAR
def create_data(table_name, table_id, table_column):
    print(f'---------- Registrando fila en {table_name} ----------')

    if table_name != 'productos':
        while True:
            name = input('Nombre: ').strip()
            if not name:
                print('Debe insertar el nombre obligatoriamente.')
            else:
                break
        
        try:
            supabase.table(table_name).insert({table_id: new_id(table_name, table_id),table_column: name}).execute()

            print(f'Fila con el nombre {name} creada con éxito.')
        except Exception as e:
            print(f'Ocurrió un error al intentar crear la fila: {e}.')
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
            supabase.table(table_name).insert({table_id: new_id(os.environ.get('TABLE_3'), os.environ.get('TABLE_3_ID')), os.environ.get('TABLE_2_ID'): category, os.environ.get('TABLE_1_ID'): company, table_column: name, os.environ.get('TABLE_3_COLUMN_2'): weight, os.environ.get('TABLE_3_COLUMN_3'): stock, os.environ.get('TABLE_3_COLUMN_4'): exp_date}).execute()

            print(f'Producto {name} creado con éxito.')
        except Exception as e:
            print(f'Ocurrió un error al intentar crear el producto: {e}.')
    else:
        pass

#FUNCIÓN PARA LEER
def read_data(table_name):
    print(f'---------- {table_name} ----------')

    try:
        data_select = supabase.table(table_name).select('*').execute()

        if data_select.data == []:
            print('No hay filas registradas.')
        else:
            df = pd.DataFrame(data_select.data)
            print(df.to_string(index=False))
    except Exception as e:
        print(f'Ocurrió un error al intentar ver las filas registradas: {e}')

#FUNCIÓN PARA ACTUALIZAR
def update_data(table_name, table_id, table_column):
    print(f'---------- Editando fila en {table_name} ----------')

    if table_name != 'productos':
        while True:
            if table_name == 'compañias':
                read_data('compañias')
            if table_name == 'categorias':
                read_data('categorias')
            else:
                pass

            id_to_update = int(input('ID a editar: '))
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
            supabase.table(table_name).update({table_column: new_name}).eq(table_id, id_to_update).execute()

            print(f'Fila con el ID: {id_to_update} editada con éxito.')

            read_data(table_name)
        except Exception as e:
            print(f'Ocurrió un error al intentar editar la fila: {e}.')
    else:
        pass

    if table_name == 'productos':
        while True:
            read_data('productos')
            products_id_to_update = int(input('ID del producto: '))
            if not products_id_to_update:
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
            supabase.table(table_name).update({os.environ.get('TABLE_2_ID'): new_category, os.environ.get('TABLE_1_ID'): new_company, table_column: new_name, os.environ.get('TABLE_3_COLUMN_2'): new_weight, os.environ.get('TABLE_3_COLUMN_3'): new_stock, os.environ.get('TABLE_3_COLUMN_4'): new_exp_date}).eq(table_id, products_id_to_update).execute()

            print(f'Producto con el ID: {products_id_to_update} editado con éxito.')

            read_data(table_name)
        except Exception as e:
            print(f'Ocurrió un error al intentar editar el producto: {e}.')
    else:
        pass

#FUNCIÓN PARA ELIMINAR
def delete_data(table_name, table_id):
    print(f'---------- Eliminando fila en {table_name} ----------')

    while True:
        check = input(f'¿Esta seguro(a) de querer eliminar una fila de {table_name}? (si/no) ')

        if check == 'no':
            print('Operación cancelada.')
            return
        elif check == 'si':
            break
        else:
            print('Respuesta no válida. Por favor introduzca "si" o "no".')

    while True:
        read_data(table_name)
        id_to_delete = input('ID a eliminar: ')

        if not id_to_delete:
            print('Debe insertar un id obligatoriamente.')
        else:
            while True:
                double_check = input(f'¿Esta seguro(a) de querer elilminar la fila con el ID: {id_to_delete} de {table_name}? (si/no) ')

                if double_check == 'no':
                    print('Doble verificación cancelada. Volviendo a la entrada del ID.')
                    break
                elif double_check == 'si':
                    try:
                        supabase.table(table_name).delete().eq(table_id, id_to_delete).execute()

                        print(f'Fila con el ID: {id_to_delete} en {table_name} eliminada con éxito.')

                        read_data(table_name)
                    except Exception as e:
                         print(f'Ocurrió un error al intentar eliminar la fila con el ID: {id_to_delete}: {e}.')
                    return
                else:
                   print('Respuesta no válida. Por favor, introduzca "si" o "no".')