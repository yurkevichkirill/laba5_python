from xml.dom.minidom import ProcessingInstruction

import pandas as pd
import random
pd.set_option('display.max_columns', None)

data = pd.read_csv('datasets/test.csv')

newData = data.head(1000)
#Проверяем пропуски
print(data.isnull().sum())

#Заполняем пропуски LifeSquare значениями Square -KSquare -10
data['LifeSquare'] = data['LifeSquare'].fillna(data['Square'] - data['KitchenSquare'] - 10)

#Заполняем Healthcare_1 случайными значениями
data['Healthcare_1'] = data['Healthcare_1'].fillna(random.randint(0, 1000))
print(data.head(1000))

#Проверяем пропуски еще раз
print(data.isnull().sum())

#Проверяем условие площади
condition1 = data['Square'] < (data['LifeSquare'] + data['KitchenSquare'])
data.loc[condition1, 'Square'] = data['LifeSquare'] + data['KitchenSquare']+10

#Проверяем условие этажей
condition2 = data['Floor'] > data['HouseFloor']
data.loc[condition2, 'Floor'] = data['HouseFloor']

#Проверяем условие количества комнат
condition3 = data['Rooms']<1
data.loc[condition3, 'Rooms'] = 1

print(data.head(1000))

room_counts = data.head(1000)['Rooms'].value_counts()
print(room_counts)

first_1000 = data.head(1000)
first_1000.to_csv('datasets/yurkevich.csv', index=False)

