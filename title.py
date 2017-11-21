import vk_api
import time
import random

vk = vk_api.VkApi(token='b701f7ff2d5b79b24ccda29b734de4351f0a4f50953514669a29d8c6a9038f32814dca1579061063009fa')

values = {'out': 0, 'count': 100, 'time_offset': 60}


helloMas = ('Дарова', 'Привет', 'Ку', 'Хай', 'Кусай сбоку или отламывай', 'Сложна', 'В качалочку бы', 'Привет', 'Дарова', 'хммммм')


def write_msg(user_id, s):
    vk.method('messages.send', {'user_id': user_id, 'message': s})


while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
        if response['items'][0]['body'] == 'Привет':
            write_msg(item['user_id'], 'Ага')
        else:
            i = int(random.random() * 10)
            write_msg(item['user_id'], helloMas[i])
    time.sleep(1)
