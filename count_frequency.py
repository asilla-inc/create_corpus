import jijilla_char_list
import pandas as pd

filepath = './annotation_train.txt'
data = []
with open(filepath, 'r') as file:
    lines = file.readlines()
    for line in lines:
        text = line.strip('\n')
        data.append(text.split(',')[1])
    

data_combined = ''.join(data)

freq = {}
for char in jijilla_char_list.kanjis:
    count = data_combined.count(char)
    # print(char, count)
    freq[char] = count


df = pd.DataFrame.from_dict(freq, orient='index', columns=['count'])
df['size'] = None
df = df.sort_values(by='count', ascending=False)
for index, row in df.iterrows():
    if len(str(row[0])) == 5:
        size = str(row[0])[0:3]
        df.at[index, 'size'] = size
    elif len(str(row[0])) == 4:
        size = str(row[0])[0:2]
        df.at[index, 'size'] = size
    elif len(str(row[0])) == 3:
        size = str(row[0])[0]
        df.at[index, 'size'] = size
    else:
        df.at[index, 'size'] = 0

grouped_df = df.groupby('size')

counts = {}
for name, group in grouped_df:
    print(name)
    print(group.index.values)
    words = group.index.values.tolist()
    words = ' '.join(words)
    counts[name] = words

print(counts)
freq_df = pd.DataFrame.from_dict(counts, orient='index', columns=['words'])
freq_df.to_csv('freq_grouped.csv')