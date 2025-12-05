from create import create_data
from read import read_data
from update import update_data
from delete import delete_data
from to_csv import from_table_to_csv as to_csv

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
                    create_data('compañias', 'id_compañia', 'nombre_compañia')
                elif companys_selection == '2':
                    read_data('compañias')
                elif companys_selection == '3':
                    update_data('compañias', 'id_compañia', 'nombre_compañia')
                elif companys_selection == '4':
                    delete_data('compañias', 'id_compañia')
                elif companys_selection == '5':
                    to_csv('compañias', 'compañias.csv')
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
                    create_data('categorias', 'id_categoria', 'nombre_categoria')
                elif categorys_selection == '2':
                    read_data('categorias')
                elif categorys_selection == '3':
                    update_data('categorias', 'id_categoria', 'nombre_categoria')
                elif categorys_selection == '4':
                    delete_data('categorias', 'id_categoria')
                elif categorys_selection == '5':
                    to_csv('categorias', 'categorias.csv')
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
                    create_data('productos', 'id_producto', 'nombre_producto')
                elif products_selection == '2':
                    read_data('productos')
                elif products_selection == '3':
                    update_data('productos', 'id_producto', 'nombre_producto')
                elif products_selection == '4':
                    delete_data('productos', 'id_productos')
                elif products_selection == '5':
                    to_csv('productos', 'productos.csv')
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
            print('-' * 60)
            break

        else:
            print('-' * 60)
            print('Opción invalida. Seleccione el número de la tabla que desea elegir.')

if __name__ == '__main__':
    menu()
else:
    print('No puedes ejecutar este programa.')