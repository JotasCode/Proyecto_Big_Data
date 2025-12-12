import os
from CRUD import create_data, read_data, update_data, delete_data
from to_csv import from_table_to_csv as to_csv
from dotenv import load_dotenv
load_dotenv()

def menu():
    print('-' * 60)
    print('Programa de registro de inventario.')

    while True:
        print('---------- Tablas ----------')
        print('-' * 60)
        print('1. Compañías')
        print('2. Categorías')
        print('3. Productos')
        print('-' * 60)
        print('4. Salir.')
        print('-' * 60)

        selection = input('Por favor seleccione una tabla: ')

        if selection == '1':
            selection = 'compañía'
            selection_table = 'TABLE_1'
            selection_id = 'TABLE_1_ID'
            selection_column = 'TABLE_1_COLUMN'
            break

        elif selection == '2':
            selection = 'categoría'
            selection_table = 'TABLE_2'
            selection_id = 'TABLE_2_ID'
            selection_column = 'TABLE_2_COLUMN'
            break

        elif selection == '3':
            selection = 'producto'
            selection_table = 'TABLE_3'
            selection_id = 'TABLE_3_ID'
            selection_column = 'TABLE_3_COLUMN_1'
            break

        elif selection == '4':
            print('-' * 60)
            print('Gracias por utilizar nuestros servicios, hasta la próxima.')
            print('-' * 60)
            break

        else:
            print('-' * 60)
            print('Opción invalida. Seleccione el número de la tabla que desea elegir.')

            while True:
                print('---------- Elegiste la tabla de Compañías ----------')
                print(f'1. Registrar {selection}.')
                print('2. Ver registro.')
                print(f'3. Editar registro de {selection}.')
                print(f'4. Eliminar {selection}.')
                print('5. Guardar registro en un archvo local.')
                print('-' * 60)
                print('6. Salir.')
                print('-' * 60)

                selection_2 = input('Por favor seleccione una opción: ')

                if selection_2 == '1':
                    create_data(os.environ.get(selection_table), os.environ.get(selection_id), os.environ.get(selection_column))
                elif selection_2 == '2':
                    read_data(os.environ.get(selection_table))
                elif selection_2 == '3':
                    update_data(os.environ.get(selection_table), os.environ.get(selection_id), os.environ.get(selection_column))
                elif selection_2 == '4':
                    delete_data(os.environ.get(selection_table), os.environ.get(selection_id))
                elif selection_2 == '5':
                    to_csv(os.environ.get(selection_table))
                elif selection_2 == '6':
                    print('-' * 60)
                    print('Saliendo del registro.')
                    print('-' * 60)
                    break
                else:
                    print('-' * 60)
                    print('Opción invalida. Seleccione el número de la opción que desea elegir.')

if __name__ == '__main__':
    menu()
else:
    print('No puedes ejecutar este programa.')