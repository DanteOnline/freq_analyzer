"""Убираем стоп слова"""
# pip install nltk
import nltk
# скачиваем стопслова
nltk.download('stopwords')
from nltk.corpus import stopwords

def no_stop(words):
    """
    Убираем из списка стоп слова
    :param words: входной список слов со стоп словами
    :return: новый список слов без стоп слов
    """
    # получаем русские стоп слова
    stop_words = stopwords.words('russian')
    without_stop = []
    # перебираем слова
    for word in words:
        # если это не стоп слово
        if word not in stop_words:
            # записываем в список
            without_stop.append(word)
    # возвращаем слова без стоп слов
    return without_stop

if __name__ == '__main__':
    words = ['он', 'только', 'вошел', 'в', 'дверь', 'как', 'она', 'испугалась']
    result = no_stop(words)
    print(words)
    print(len(words))
    print(result)
    print(len(result))
