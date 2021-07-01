SEPARATORS = ['.',
              ' ',
              '\t',
              '\n',
              '!',
              '?',
              ',',
              ';',
              ':',
              '-',
              '(',
              ')',
              '[',
              ']',
              '"']
SPACES = [' ', '\t', '\n']


def get_array_of_words(string):
    words = []
    word = ''
    i = 0
    while i < len(string):
        if string[i] not in SEPARATORS or len(word) == 0:
            word += string[i]
            i += 1
        else:
            while i < len(string) and string[i] in SEPARATORS and string[i] not in SPACES:
                word += string[i]
                i += 1
            while i < len(string) and string[i] in SPACES:  # пропускаем пробельные символы после конца слова
                i += 1
            words.append(word)
            word = ''
    if word:
        words.append(word)

    return words
