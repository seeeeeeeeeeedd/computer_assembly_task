from component import Component


class ComputerAssembly:
    def __init__(self, title: str):
        self.__components = []

        is_valid = self.__is_valid_title(title)

        if is_valid:
            self.__title = title.capitalize()
        else:
            self.__title = 'Без названия'


    def get_computer_assembly_title(self) -> str:
        return self.__title

    def add_component(self, title: str, description: str):
        component = Component(title, description)
        self.__components.append(component)

    def show(self):
        print(f'Сборка: {self.__title}')
        if not self.__components:
            print('Компоненты отсутствуют')
        else:
            for component in self.__components:
                print(f'Компонент: "{component.get_title()}", характеристика: {component.get_description()}')

    def __is_valid_title(self, title: str) -> bool:
        if not isinstance(title, str):
            return False
        if not title.strip():
            return False

        return True
