while True:
    user_input = input('Я хочу поигать в игру угадайка! Введи число и попробуй угадай')
    magic_number = '5'
    if user_input == magic_number:
        print('Поздравляю! Вы угадали!')
        break
    elif user_input != magic_number:
        print('попробуйте снова')
