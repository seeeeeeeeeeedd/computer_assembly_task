from component import Component
from computer import Computer

processor = Component('Процессор', 'AMD Ryzen 7 9800X3D OEM 4.7 ГГц')
graphics_card = Component('Видеокарта', 'MSI GeForce RTX 5070 VENTUS 3X OC 12 ГБ')
storage_drive = Component('SSD', 'MSI SPATIUM S270 960 ГБ 500 ТБ')

personal_computer = Computer()

personal_computer.add_component(processor)
personal_computer.add_component(graphics_card)
personal_computer.add_component(storage_drive)

personal_computer.show_assembly()
