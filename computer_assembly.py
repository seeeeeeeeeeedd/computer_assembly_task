from component import Component


class ComputerAssembly:
    def __init__(self, assembly_title: str):
        self.__assembly_title = assembly_title
        self.__component = []

    def get_computer_assembly_title(self) -> str:
        return self.__assembly_title

    def add_component(self, title: str, description: str):
        component = Component(title, description)
        self.__component.append(component)

    def show_assembly(self):
        print(f'Сборка: {self.__assembly_title}')
        if not self.__component:
            print('Компоненты отсутствуют')
        else:
            for component in self.__component:
                print(f'Компонент: "{component.get_title()}", характеристика: {component.get_description()}')
