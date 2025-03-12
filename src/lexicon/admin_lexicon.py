from enum import Enum


class AdminLexicon(Enum):
    prefix: str = "#"
    button_add: str = "Добавить текст"
    button_add_role: str = "Добавить роль"
    button_add_me: str = "Добавить меня"
    answer_if_text_already_include: str = "Данный текст уже добавлен!"
    answer_success: str = "Успех!"
    answer_insert_text: str = "Вставьте желаемый текст:"
    answer_role_successfully_added: str = "Роль успешно добавлена!"
    answer_success_text_added: str = "Текст успешно добавлен!"
    answer_insert_role_name: str = "Введите название роли:"
    answer_insert_role_description: str = "Введите описание роли:"
    answer_incorrect_role_name: str = (
        "Некорректное имя роли, используйте имя содержащее только буквы."
    )
