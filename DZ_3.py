package = {'фонарик': 1, 'еда': 4, 'спальный мешок': 3, 'горелка': 5, 'палатка': 10, 'спреи': 2, 'генератор': 20,
        'ружьё': 6, 'столовые приборы': 2, 'гитара': 3}
in_backpack = []
max_weight = int(input('Введите грузоподъёмность рюкзака'))

for keys in sorted(package, key=package.get, reverse=True):
    if package.get(keys) <= max_weight:
        max_weight -= package.get(keys)
        in_backpack.append(keys)
print(in_backpack)
