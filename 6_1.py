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

with ExcelWriter(filename, mode="a") as writer: 
    data.loc[[data['Цена'].idxmax()]].to_excel(writer, sheet_name='6_1_1')
    pd.DataFrame(data[['Год покупки']].value_counts().keys()[0]).to_excel(writer, sheet_name='6_1_2')
    pd.DataFrame(data['Издатель'].value_counts()[:3]).to_excel(writer, sheet_name='6_1_3')
    func615(data).to_excel(writer, sheet_name='6_1_5')
    func616(data).sort_values('IBWBG').to_excel(writer, sheet_name='6_1_6')
    data.groupby(['Механики']).count().to_excel(writer, sheet_name='6_1_7')
