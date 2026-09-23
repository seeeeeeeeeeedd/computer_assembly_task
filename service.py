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

    def __is_valid_computer_assembly(self, computer_assembly: ComputerAssembly) -> bool:
        return isinstance(computer_assembly, ComputerAssembly)
