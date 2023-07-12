def run():
    # my_list = [1, "Hello", True, 4.5]
    # my_dict = {"firstname": "Facundo", "lastname": "García"}

    super_list = [
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Luis", "lastname": "Nicolás"},
        {"firstname": "María", "lastname": "Montero"},
        {"firstname": "Rafael", "lastname": "Alarcón"},
    ]

    super_dicts = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, 0, 9],
        "floating_nums": [2.3, 5.89, 4.56],
    }

    for key, value in super_dicts.items():
        print(key, "-", value)

    for item in super_list:
        print(item)

if __name__ == '__main__':
    run()