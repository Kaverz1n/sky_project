def get_val(collection: dict, key, default='Животное'):
    '''
    Функция возвращает значение словаря по
    переданному в неё ключу, в противном случае
    возвращает default
    :param collection: передаваемый словарь
    :param key: ключ, по которому выводится его значение из словаря
    :param default: деффолтное значение, выводящиеся, если ключ в словаре
    не существует
    :return: значение ключа в словаре, иначе default
    '''
    for k, v in collection.items():
        if k == key:
            return v
    return default