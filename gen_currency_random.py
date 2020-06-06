import random

def append_and_write(text, data_list, filepath):
    data_list.append(text)
    with open(filepath, 'a') as file:
        file.writelines(text+'\n')

data = []
filepath = './currency4.txt'


# 1,000円スタート
for integer in [random.randrange(1000, 990000, 1000) for i in range(10000)]:
    text = '{:,}'.format(integer)
    data.append(text)

# 10,000円スタート
for integer in [random.randrange(10000, 990000, 10000) for i in range(5000)]:
    text = '{:,}'.format(integer)
    data.append(text)

# 100万円台その他切り捨て
for integer in [random.randrange(1000000, 9000000, 1000000) for i in range(2000)]:
    text = '{:,}'.format(integer)
    data.append(text)

for integer in [random.randrange(1000000, 9000000, 100000) for i in range(5000)]:
    text = '{:,}'.format(integer)
    data.append(text)

for integer in [random.randrange(1000000, 9000000, 500000) for i in range(5000)]:
    text = '{:,}'.format(integer)
    data.append(text)



# 千万億円シリーズ
for integer in [random.randrange(50, 1000, 50) for i in range(5000)]:
    text = '{:,}'.format(integer) + '万円'
    data.append(text)

for integer in [random.randrange(1, 900, 7) for i in range(3000)]:
    text = '{:,}'.format(integer) + '万円'
    data.append(text)

for integer in [random.randrange(50, 10000, 50) for i in range(4000)]:
    text = '{:,}'.format(integer) + '千円'
    data.append(text)

for integer in [random.randrange(40, 1000, 3) for i in range(2000)]:
    text = '{:,}'.format(integer) + '千円'
    data.append(text)

for integer in [random.randrange(5, 100, 5) for i in range(1000)]:
    text = f"{integer}億円"
    data.append(text)

yen_add = 4000
for i in range(yen_add):
    position = random.randrange(0, len(data))
    while "¥" in str(data[position]) or '円' in str(data[position]):
        position = random.randrange(0, len(data))
    data[position] = '¥' + data[position]

hyphen_add = 2000
for i in range(hyphen_add):
    position = random.randrange(0, len(data))
    while '円' in str(data[position]):
        position = random.randrange(0, len(data))
    data[position] = data[position] + '-'

random.shuffle(data)

with open(filepath, 'a') as file:
    for text in data:
        file.write(text+'\n')
