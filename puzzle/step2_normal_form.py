"""Приводим слова к нормальным формам"""
from pymorphy2 import MorphAnalyzer


def to_normal_form(words):
    """
    Приводит слова к нормальным формам
    :param words: список слов
    :return: список нормальных форм
    """
    result = []
    # создаем анализатор
    morph = MorphAnalyzer()
    # перебираем слова
    for word in words:
        # получаем нормальную форму
        normal = morph.parse(word)[0].normal_form
        # добавляем в новый список
        result.append(normal)
    #возвращаем нормальные формы
    return result


if __name__ == '__main__':
    words = ['красивое', 'лучше', 'чем', 'уродливое', 'явное', 'лучше', 'чем', 'неявное', 'хороший']
    normals = to_normal_form(words)
    print(words)
    print(normals)

