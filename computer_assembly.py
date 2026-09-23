from component import Component


class ComputerAssembly:
    def __init__(self, title: str):
        self.__title = title.capitalize()
        self.__components = []

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
