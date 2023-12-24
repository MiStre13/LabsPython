from functools import reduce
s = ['научиться плести рыболовные сети',
             'обучать нейронные сети',
             'паук ловит в сети мух']

# cap_count = reduce(lambda x: [x.count('сети')], sentences)

print(reduce(lambda x, y: x + y, map(lambda x: 'сети' in x.lower(), s), 0))

