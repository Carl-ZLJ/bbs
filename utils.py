import time


def log(*args, **kwargs):
    formatory = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(formatory, value)
    with open('gua.log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)
