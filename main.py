from component import Component
from service import Service
from computer_assembly import ComputerAssembly

service = Service('E2E3')

commands = {
    '1': 'Создать сборку',
    '2': 'Добавить компонент в сборку',
    '3': 'Посмотреть список всех сборок',
    '4': 'Показать компоненты конкретной сборки',
    '0': 'Выйти из программы'
}

(CREATE_ASSEMBLY_COMMAND, ADD_COMPONENT_COMMAND, SHOW_ALL_ASSEMBLIES_COMMAND,
 SHOW_ASSEMBLY_COMPONENTS_COMMAND, EXIT_COMMAND) = commands.keys()

is_program_running = True
while is_program_running:

    print()
    for number, command in commands.items():
        print(f'{number}: {command}')

    user_command_number = input('Выберете действие и укажите его номер: ')

    if user_command_number in commands:
        if user_command_number == CREATE_ASSEMBLY_COMMAND:
            user_assembly_title = input('Укажите название сборки: ').strip().title()
            new_assembly = ComputerAssembly(user_assembly_title)
            service.add_computer_assembly(new_assembly)
        elif user_command_number == ADD_COMPONENT_COMMAND:
            user_assembly_title = input('Укажите название сборки для добавления компонента: ').strip().title()
            assembly = service.find_computer_assembly_by_title(user_assembly_title)

            if assembly:
                user_component_title = input('Укажите название компонента: ').strip().title()
                user_component_description = input('Укажите характеристики компонента: ').strip().title()
                assembly.add_component(user_component_title, user_component_description)
            else:
                print()
                print('Сборки с таким названием не существует')
        elif user_command_number == SHOW_ALL_ASSEMBLIES_COMMAND:
            service.show_all_computer_assemblies()
        elif user_command_number == SHOW_ASSEMBLY_COMPONENTS_COMMAND:
            user_assembly_title = input('Укажите название сборки: ').strip().title()
            assembly = service.find_computer_assembly_by_title(user_assembly_title)
            if assembly:
                assembly.show_assembly()
            else:
                print()
                print('Сборки с таким названием не существует')
        elif user_command_number == EXIT_COMMAND:
            is_program_running = False
            print()
            print('Выход из программы')
        else:
            print()
            print('Неизвестная команда. Попробуйте снова')
