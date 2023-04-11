from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
        InlineKeyboardButton(text='Подобрать группу',callback_data='Podobrat-gruppu'),
        InlineKeyboardButton(text='Список групп',callback_data='spisok-grupp')
    ]
        ]
)




gruppa_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
        InlineKeyboardButton(text='Психология',callback_data='gr-Психология'),
        InlineKeyboardButton(text='Криптовалюта',callback_data='gr-Криптовалюта'),
        InlineKeyboardButton(text='Стартапы',callback_data='gr-Стартапы')
    ]
        ]
)

da_net = InlineKeyboardMarkup(
    inline_keyboard = [
        [
        InlineKeyboardButton(text='да',callback_data='da'),
        InlineKeyboardButton(text='нет',callback_data='net')
    ]
        ]
)

main_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [
        InlineKeyboardButton(text='Вернуться в меню',callback_data='menu')
    ]
        ]
)


