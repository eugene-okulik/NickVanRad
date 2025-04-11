text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, "
        "dignissim vitae libero")
list_homework = text.split()
for texts in list_homework:
    if texts[-1] in '.,':
        punct = texts[-1]
        print(texts[:-1] + 'ing' + punct, end=' ')
    else:
        print(texts + 'ing', end=' ')
