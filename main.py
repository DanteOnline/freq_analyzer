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

from puzzle.step1_tokenize import hands_re
from puzzle.step2_normal_form import to_normal_form
from puzzle.step3_stop_words import no_stop
from puzzle.step4_freq_analyze import analize
from puzzle.step5_vk_group_desc import get_groups_descriptions

def get_theme(text):
    words = hands_re(text)
    normals = to_normal_form(words)
    words_no = no_stop(normals)
    theme = analize(words_no)
    return theme

# if __name__ == '__main__':
#     theme = get_theme(text)
#     #print(theme)

#     ids = ','.join([str(i) for i in range(1, 5)])
#     groups = get_groups_descriptions(ids)
#     for name, desc in groups.items():
#         theme = get_theme(desc)
#         if theme[1] > 3:
#             if theme[0] != 'br':
#                 print(name, '---------->', theme)


#1. большой текст из файла
#2. какой нибудь текст с сайта
#3. парсинг сайта и избавление от тегов
#4. title сайта, 