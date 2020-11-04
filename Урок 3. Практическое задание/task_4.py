"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib


def history_browse(url):
    salt = '1234567salt'
    url_hash = hashlib.sha256(url.encode()).hexdigest() + ':' + salt
    if url_hash not in history.values():
        history.update({url: url_hash})
        return f'URL {url} добавлена в кэш'
    else:
        return f'ссылка {url} уже есть в кэше'


history = dict()
while True:
    link = input('Введите URL (для выхода "q"): ')
    if link == 'q':
        break
    print(history_browse(link))
