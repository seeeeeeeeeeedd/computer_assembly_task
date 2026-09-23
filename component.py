class Component:
    def __init__(self, title: str, description: str):
        is_valid = self.__is_valid_component(title, description)

        if is_valid:
            self.__title = title
            self.__description = description
        else:
            self.__title = 'Без названия'
            self.__description = 'Описание отсутствует'

    def get_title(self) -> str:
        return self.__title

    def get_description(self) -> str:
        return self.__description

    def __is_valid_component(self, title: str, description: str) -> bool:
        if isinstance(title, str) and isinstance(description, str):
            if title.strip() and description.strip():
                return True

        return False
