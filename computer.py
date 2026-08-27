from component import Component


class Computer:
    def __init__(self):
        self.__component = []

    def add_component(self, component: Component):
        self.__component.append(component)

    def show_assembly(self):
        if not self.__component:
            print('Компоненты отсутствуют')
        else:
            for component in self.__component:
                print(f'Компонент: "{component.get_title()}", характеристика: {component.get_description()}')
