ksla = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

# print('courses --> ', type(ksla['courses']))
# print('bag --> ', type(ksla['bag']))

del ksla['bag']
ksla['address'] = ['Chui 180a', 'Maksima Gorkogo 18']
ksla['contacts'] = ['+996 (312) 39-20-93', 'ksla.kg']
ksla['courses'].append('Python')
ksla['courses'].append('JavaScript')
ksla['courses'].append('PHP')

for keys, values in ksla.items():
    # print(f'{keys} --> {values}')
    print(f'{keys} --> {values}')
