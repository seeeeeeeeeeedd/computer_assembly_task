from component import Component


class ComputerAssembly:
    def __init__(self, assembly_title: str):
        self.__assembly_title = assembly_title
        self.__component = []

    def add_component(self, component: Component):
        if self.__is_valid_component(component):
            self.__component.append(component)
        else:
            print('Ошибка. Указаны некорректные комплектующие')
            return

    def show_assembly(self):
        print(f'Сборка: {self.__assembly_title}')
        if not self.__component:
            print('Компоненты отсутствуют')
        else:
            for component in self.__component:
                print(f'Компонент: "{component.get_title()}", характеристика: {component.get_description()}')

    def __is_valid_component(self, component: Component) -> bool:
        if isinstance(component, Component):
            return True
        else:
            return False
