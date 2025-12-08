import os
from CRUD import create_data, read_data, update_data, delete_data
from to_csv import from_table_to_csv as to_csv
from dotenv import load_dotenv
load_dotenv()

def menu():
    print('-' * 60)
    print('---------- Almacén Atlántida ----------')

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
            while True:
                print('---------- Elegiste la tabla de Compañías ----------')
                print('1. Registrar compañía.')
                print('2. Ver compañías registradas.')
                print('3. Editar registro de compañía.')
                print('4. Eliminar compañía.')
                print('5. Guardar compañias en un archvo local.')
                print('-' * 60)
                print('6. Salir.')
                print('-' * 60)

                companys_selection = input('Por favor seleccione una opción: ')

                if companys_selection == '1':
                    create_data(os.environ.get('TABLE_1'), os.environ.get('TABLE_1_ID'), os.environ.get('TABLE_1_COLUMN'))
                elif companys_selection == '2':
                    read_data(os.environ.get('TABLE_1'))
                elif companys_selection == '3':
                    update_data(os.environ.get('TABLE_1'), os.environ.get('TABLE_1_ID'), os.environ.get('TABLE_1_COLUMN'))
                elif companys_selection == '4':
                    delete_data(os.environ.get('TABLE_1'), os.environ.get('TABLE_1_ID'))
                elif companys_selection == '5':
                    to_csv(os.environ.get('TABLE_1'))
                elif companys_selection == '6':
                    print('-' * 60)
                    print('Saliendo del registro de compañías.')
                    print('-' * 60)
                    break
                else:
                    print('-' * 60)
                    print('Opción invalida. Seleccione el número de la opción que desea elegir.')

        elif selection == '2':
            while True:
                print('---------- Elegiste la tabla de Categorías ----------')
                print('1. Registrar categoría.')
                print('2. Ver categorías registradas.')
                print('3. Editar registro de categoría.')
                print('4. Eliminar categoría.')
                print('5. Guardar categorías en un archvo local.')
                print('-' * 60)
                print('6. Salir.')
                print('-' * 60)

                categorys_selection = input('Por favor seleccione una opción: ')

                if categorys_selection == '1':
                    create_data(os.environ.get('TABLE_2'), os.environ.get('TABLE_2_ID'), os.environ.get('TABLE_2_COLUMN'))
                elif categorys_selection == '2':
                    read_data(os.environ.get('TABLE_2'))
                elif categorys_selection == '3':
                    update_data(os.environ.get('TABLE_2'), os.environ.get('TABLE_2_ID'), os.environ.get('TABLE_2_COLUMN'))
                elif categorys_selection == '4':
                    delete_data(os.environ.get('TABLE_2'), os.environ.get('TABLE_2_ID'))
                elif categorys_selection == '5':
                    to_csv(os.environ.get('TABLE_2'))
                elif categorys_selection == '6':
                    print('-' * 60)
                    print('Saliendo del registro de categorías.')
                    print('-' * 60)
                    break
                else:
                    print('-' * 60)
                    print('Opción invalida. Seleccione el número de la opción que desea elegir.')

        elif selection == '3':
            while True:
                print('---------- Elegiste la tabla de Productos ----------')
                print('1. Registrar producto.')
                print('2. Ver productos registrados.')
                print('3. Editar registro.')
                print('4. Eliminar producto.')
                print('5. Guardar productos en un archvo local.')
                print('-' * 60)
                print('6. Salir.')
                print('-' * 60)

                products_selection = input('Por favor seleccione una opción: ')

                if products_selection == '1':
                    create_data(os.environ.get('TABLE_3'), os.environ.get('TABLE_3_ID'), os.environ.get('TABLE_3_COLUMN'))
                elif products_selection == '2':
                    read_data(os.environ.get('TABLE_3'))
                elif products_selection == '3':
                    update_data(os.environ.get('TABLE_3'), os.environ.get('TABLE_3_ID'), os.environ.get('TABLE_3_COLUMN'))
                elif products_selection == '4':
                    delete_data(os.environ.get('TABLE_3'), os.environ.get('TABLE_3_ID'))
                elif products_selection == '5':
                    to_csv(os.environ.get('TABLE_3'))
                elif products_selection == '6':
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
            print('Almacén Atlántica')
            print('-' * 60)
            break

        else:
            print('-' * 60)
            print('Opción invalida. Seleccione el número de la tabla que desea elegir.')

if __name__ == '__main__':
    menu()
else:
    print('No puedes ejecutar este programa.')