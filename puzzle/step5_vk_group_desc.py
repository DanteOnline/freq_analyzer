import requests
import json


def vk_api(method, **kwargs):
    """
    Получение данных из контакта
    :param method: метод vk api
    :param kwargs: параметры
    :return:
    """
    # формируем строку запроса
    api_request = 'https://api.vk.com/method/'+method + '?'
    # добавляем параметры
    api_request += '&'.join(['{}={}'.format(key, kwargs[key]) for key in kwargs])
    # получаем результат в формате json и приводим к словарю
    return json.loads(requests.get(api_request).text)

# result = vk_api('wall.get', owner_id=-1)
# print(result)
def get_groups_descriptions(ids):
    """
    Ищем описание групп
    :param ids: идентификаторы групп, например '1,2,3,4,5'
    :return: словарь с парами название группы: описание группы
    """
    # отправляем запрос в контакт
    result = vk_api('groups.getById', group_ids=ids, fields='description')
    # получаем ответ
    result = result['response']
    res_dict = {}
    # в ответе словари с данными о группе
    for r in result:
        if 'description' in r:
            if r['description']:
                res_dict[r['name']] = r['description']
    return res_dict

# будем искать в описании группы
ids = ','.join([str(i) for i in range(1,100)])
#print(ids)
# result = vk_api('groups.getById', group_ids=ids, fields='description')
# print(result)
# result = result['response']
# for r in result:
#     if 'description' in r:
#         if r['description']:
#             print(r['name'],'--->',r['description'])

if __name__ == '__main__':
    # возьмем 1-ые 100 групп (описание есть не у всех)
    ids = ','.join([str(i) for i in range(1, 100)])
    # находим их описание
    result = get_groups_descriptions(ids)
    for k, v in result.items():
        print(k,':::',v)
