import pandas as pd
from pandas.io.excel import ExcelWriter
import openpyxl
import os.path
import os
from statistics import median

print('\n#6.1')

data = pd.read_excel('input.6.1.xlsx')

filename = '6.1.Desyukevich.xlsx'
if os.path.isfile(filename):
    os.remove(filename)

wb = openpyxl.Workbook()
wb.save(filename)

def func614(lst):
    dct = {}
    for i in range(99):
        dct[i+1] = 0

    for i in lst:
        for j in i:
            dct[j] += 1
    return ["intersection", max(dct.values())]
    

def func615(data):
    dt1 = pd.DataFrame(columns=['Janre', 'Players_median'])
    ind = 0
    for janre in set(data['Жанр'].values):
        sm = []
        for i in data[data['Жанр'] == janre]['Число игроков']:
            sm.append(int(i.split('-')[1]))
        dt1.loc[ind] = [janre, median(sm)]
        ind += 1
    return dt1

def func616(data):
    if 'IBWBG' in data.columns:
        data = data.drop(columns=['IBWBG'])
    data['IBWBG'] = data['Реиграбельность'] - data['Сложность']
    return data

def func617(data):
    new_data=data['Механики'].str.lower().str.get_dummies(sep='; ').astype(int)
    new_data.loc['frequency'] = (new_data.sum(numeric_only=True, axis=0))/(len(new_data.index))
    res_data= pd.DataFrame(new_data.loc['frequency'])
    return res_data

with ExcelWriter(filename, mode="a") as writer: 
    data.loc[[data['Цена'].idxmax()]].to_excel(writer, sheet_name='6_1_1')
    pd.DataFrame(data[['Год покупки']].value_counts().keys()[0]).to_excel(writer, sheet_name='6_1_2')
    pd.DataFrame(data['Издатель'].value_counts()[:3]).to_excel(writer, sheet_name='6_1_3')
    pd.DataFrame(func614([[i for i in range([int(j) for j in i.split('-')][0], [int(j) for j in i.split('-')][1])] for i in data['Число игроков'].values])).to_excel(writer, sheet_name='6_1_4')
    func615(data).to_excel(writer, sheet_name='6_1_5')
    func616(data).sort_values('IBWBG').to_excel(writer, sheet_name='6_1_6')
    func617(data).to_excel(writer, sheet_name='6_1_7')
