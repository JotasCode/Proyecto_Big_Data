import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

url: str = os.environ.get('SUPABASE_URL')
key: str = os.environ.get('SUPABASE_KEY')

if not url:
    raise ConnectionError('No se ha colocado la url de la base de datos Todo-App.')
elif not key:
    raise ConnectionError('No se ha colocado la API key de la base de datos Todo-App.')

supabase: Client = create_client(url, key)

#Tabla de productos

def new_id():
    id_data = supabase.table("productos").select("id_producto").order("id_producto", desc=True).limit(1).execute()

    if len(id_data.data) == 0:
        return 1  
    else:
        lates_id = id_data.data[0]["id_producto"]
        return lates_id + 1 

def create_data():
    print('---------- Registrando producto ----------')

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
        exp_date = int(input('Fecha de expiración: '))
        if not exp_date:
            print('Debe insertar la feca obligatoriamente.')
        else: 
            break

    supabase.table('productos').insert({'id_producto': new_id(), 'nombre_producto': name, 'peso_producto_gramos': weight, 'fecha_exp': exp_date}).execute()

def read_data():
    print('---------- Productos ----------')

    data_select = supabase.table('productos').select('*').execute()

    if data_select.data == []:
        print('No hay productos registrados.')
    else:
        print(data_select)

def update_data():
    print('---------- Actualizando registro ----------')

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
        new_exp_date = int(input('Nueva fecha de expiración: '))
        if not new_exp_date:
            print('Debe insertar la fecha obligatoriamente.')
        else: 
            break

    supabase.table('productos').update({'nombre_producto': new_name, 'peso_producto_gramos': new_weight, 'fecha_exp': new_exp_date}).eq('id_producto', id_to_update).execute()

def delete_data():
    print('---------- Eliminando producto ----------')

    while True:
        check = input('¿Esta seguro(a) de querer eliminar un produto? (si/no) ')

        if check == 'no':
            break
        else:
            while True:
                id_to_delete = input('ID del producto: ')

                if not id_to_delete:
                    print('Debe insertar un id obligatoriamente.')
                else:
                    double_check = input('¿Estas seguro de querer elilminar este producto? si/no ')

                    if double_check == 'no':
                        break
                    else:
                        while True:
                            supabase.table('productos').delete().eq('id_producto', id_to_delete).execute()
                            break

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
            create_data()
        elif selection == 2:
            read_data()
        elif selection == 3:
            update_data()
        elif selection == 4:
            delete_data()
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