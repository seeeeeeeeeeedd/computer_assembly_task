from component import Component
from computer_assembly import ComputerAssembly

processor = Component('Процессор', 'AMD Ryzen 7 9800X3D OEM 4.7 ГГц')
graphics_card = Component('Видеокарта', 'MSI GeForce RTX 5070 VENTUS 3X OC 12 ГБ')
storage_drive = Component('SSD', 'MSI SPATIUM S270 960 ГБ 500 ТБ')
power_supply = Component('Блок питания', 'Corsair RM850x 850W')
ram = Component('Оперативная память', 'Kingston FURY 32 ГБ DDR5')

personal_computer = ComputerAssembly('Игровой ПК')
office_computer = ComputerAssembly('Офисный ПК')

personal_computer.add_component(processor)
personal_computer.add_component(graphics_card)
personal_computer.add_component(storage_drive)
office_computer.add_component(power_supply)
office_computer.add_component(ram)

personal_computer.show_assembly()
print()
office_computer.show_assembly()
