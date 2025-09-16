def distance_converter():
    units = {
        'км': 1000,
        'м': 1,
        'см': 0.01,
        'мм': 0.001,
        'mi': 1609.34,
        'yd': 0.9144
    }
    print("Единицы: км, м, см, мм, mi, yd")

    source = input('Из: ').strip().lower()
    target = input('В: ').strip().lower()

    if source not in units or target not in units:
        print('Ошибка!')
        return
    try:
        value = float(input('Значение: '))
        result = value * units[source] / units[target]
        print(f'{value} {source} = {result:.6f} {target}')
    except:
        print('Ошибка')


distance_converter()
