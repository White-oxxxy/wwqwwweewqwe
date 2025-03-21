from enum import Enum


class AllLexicon(Enum):
    command_button_start: str = "/start"
    command_button_help: str = "/help"
    command_button_start_description: str = "Для начала работы нажмите сюда!"
    command_button_help_description: str = "Информация"
    button_tag_search: str = "Поиск по: тэг"
    button_text_search: str = "Поиск по: текст"
    button_search: str = "Найти"
    button_next: str = "Далее"
    button_back: str = "Назад"
    button_back_to_search: str = "Назад к поиску"
    button_menu: str = "Меню"
    button_tag_list: str = "Тэги"
    button_help: str = "Помощь"
    answer_help: str = (
        "Вы можете найти интересующий вас текст по тэгу с префиксом # или по любому слову или предложению из этого текста"
    )
    answer_start: str = "Это база крутых текстов, нажмите Найти и следуйте инструкциям"
    answer_search: str = (
        "Выберите как провести поиск. Так же можете посмотреть список доступных тэгов."
    )
    answer_if_incorrect_prefix: str = (
        "Ошибка в префиксе и должны быть разделены запятыми! (Все должны начинаться с символа #)"
    )
    answer_insert_tag: str = "Введите тэг:"
    answer_insert_word: str = "Введите слово или предложение из искомого текста:"
    answer_if_tag_missing: str = "По такому тэгу ничего не найдено!"
    answer_to_another_things: str = "Я ничо не понял"
    answer_db: str = "тута будэ база данных"
    answer_menu: str = "Вы в главном меню."
    answer_result: str = "Результат поиска:"
    answer_empty_tag_list: str = "Пока еще нет тэгов"
    answer_result_not_found: str = "Ничего не найдено!"
