"""Разбиваем текст на слова"""
import re
import string
"""
установка pip install pymorphy2
pip install -U pymorphy2-dicts-ru
"""
from pymorphy2.tokenizers import simple_word_tokenize



def hands_simple(text):
    """
    Разбивает текст на слова самаы простым способом split
    :param text: Входной текст
    :return: список слов
    """
    words = text.split()
    return words


def pymorphy_simple(text):
    """
    Разбивает текст на слова функцией из pymorphy2
    :param text: Входной текст
    :return: список слов
    """
    words = simple_word_tokenize(text)
    return words


def hands_re(text):
    """
    Разбивает текст на слова регулярками
    :param text: Входной текст
    :return: список слов
    """
    # собираем символы которые будем отбрасывать
    punctuation = string.punctuation + '\u2014\u2013\u2012\u2010\u2212' + '«»‹›‘’“”„`'
    word_tokenize = re.compile(r"([^\w_\u2019\u2010\u002F-]|[+])")
    words = []
    for token in word_tokenize.split(text):
        # если слово не попадает в те которые мы исключаем
        if token and not token.isspace() and not token in punctuation:
            # добавляем слово в список
            words.append(token.lower())
    # возвращаем список слов
    return words



if __name__ == '__main__':
    # исходный текст
    text = '''
    Красивое лучше, чем уродливое.
    Явное лучше, чем неявное.
    Простое лучше, чем сложное.
    Сложное лучше, чем запутанное.
    Плоское лучше, чем вложенное.
    Разреженное лучше, чем плотное.
    Читаемость имеет значение.
    Особые случаи не настолько особые, чтобы нарушать правила.
    При этом практичность важнее безупречности.
    Ошибки никогда не должны замалчиваться.
    Если не замалчиваются явно.
    Встретив двусмысленность, отбрось искушение угадать.
    Должен существовать один — и, желательно, только один — очевидный способ сделать это.
    Хотя он поначалу может быть и не очевиден, если вы не голландец[12].
    Сейчас лучше, чем никогда.
    Хотя никогда зачастую лучше, чем прямо сейчас.
    Если реализацию сложно объяснить — идея плоха.
    Если реализацию легко объяснить — идея, возможно, хороша.
    Пространства имён — отличная штука! Будем делать их побольше!
    '''
    print('split','-'*100)
    words = hands_simple(text)
    print('слова: ', words)
    print('кол-во слов', len(words))
    print('pymorphy', '-' * 100)
    words = pymorphy_simple(text)
    print('слова: ', words)
    print('кол-во слов', len(words))
    print('re', '-' * 100)
    words = hands_re(text)
    print('слова: ', words)
    print('кол-во слов', len(words))