from computer_assembly import ComputerAssembly


class Service:
    def __init__(self, title: str):
        self.__title = title
        self.__computer_assemblies = []

    def add_computer_assembly(self, computer_assembly: ComputerAssembly):
        is_valid_computer_assembly = self.__is_valid_computer_assembly(computer_assembly)

        if is_valid_computer_assembly:
            self.__computer_assemblies.append(computer_assembly)
        else:
            print('Ошибка. Некорректные данные')

    def get_service_title(self) -> str:
        return self.__title

    def show_all_computer_assemblies(self):
        for computer_assembly in self.__computer_assemblies:
            computer_assembly.show()

    def find_computer_assembly_by_title(self, title: str):
        for computer_assembly in self.__computer_assemblies:

            if computer_assembly.get_computer_assembly_title().lower() == title.lower():
                return computer_assembly

        return None

    def add_component_to_computer_assembly(self, assembly_title: str,
                                           component_title: str, component_description: str) -> bool:
        assembly = self.find_computer_assembly_by_title(assembly_title)
        if assembly is None:
            print('Ошибка. Сборки с таким названием не найдено')
            return False
        else:
            assembly.add_component(component_title, component_description)
            return True

    def __is_valid_computer_assembly(self, computer_assembly: ComputerAssembly) -> bool:
        return isinstance(computer_assembly, ComputerAssembly)
