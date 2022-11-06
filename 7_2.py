from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def func721():
    with open('input.7.2.txt', 'r') as file:
        file = file.readlines()
    for i in range(len(file)):
        file[i] = file[i].strip()
    dct = {0: ['A', 'T', 'G', 'C']}
    for i in range(len(file[0])):
        dct[i+1] = [0, 0, 0, 0]
    for seq in file:
        for i in range(len(seq)):
            if seq[i] == 'A':
                dct[i+1][0] += 1
            if seq[i] == 'T':
                dct[i+1][1] += 1
            if seq[i] == 'G':
                dct[i+1][2] += 1
            if seq[i] == 'C':
                dct[i+1][3] += 1
    dt = pd.DataFrame(dct).set_index(0)

    plt.figure(figsize=[16, 9])
    x_pos = np.arange(1, 10)

    wd = 0.5
    plt.bar(x_pos, dt.loc['A'].values, color='r', width=wd, label='A')
    plt.bar(x_pos, dt.loc['T'].values, bottom=dt.loc['A'].values, color='y', width=wd, label='T')
    plt.bar(x_pos, dt.loc['G'].values, bottom=dt.loc['A'].values+dt.loc['T'].values, color='b', width=wd, label='G')
    plt.bar(x_pos, dt.loc['C'].values, bottom=dt.loc['A'].values+dt.loc['T'].values+dt.loc['G'].values, color='c', width=wd, label='C')

    plt.xlabel("Number")
    plt.ylabel("Freq")

    plt.legend(["A", "T", "G", "C"])
    plt.savefig('7_2_1.png')

    plt.show()

codes = {
    'A': 'A', 'C': 'C', 'G': 'G', 'T': 'T', 
    'AG': 'R', 'CT': 'Y', 'CG': 'S', 'AT': 'W', 'GT': 'K', 'AC': 'M', 
    'CGT': 'B', 'AGT': 'D', 'ACT': 'H', 'ACG': 'V', 
    'ACGT': 'N'
}

def freq_to_code(pos):
    top_nucs = pos.dropna().index
    key = ''.join(sorted(top_nucs))
    return codes[key]

def func722():
    with open('input.7.2.txt', 'r') as file:
        file = file.readlines()
    for i in range(len(file)):
        file[i] = file[i].strip()
    dct = {0: ['A', 'T', 'G', 'C']}
    for i in range(len(file[0])):
        dct[i+1] = [0, 0, 0, 0]
    for seq in file:
        for i in range(len(seq)):
            if seq[i] == 'A':
                dct[i+1][0] += 1
            if seq[i] == 'T':
                dct[i+1][1] += 1
            if seq[i] == 'G':
                dct[i+1][2] += 1
            if seq[i] == 'C':
                dct[i+1][3] += 1
    dt = pd.DataFrame(dct).set_index(0)
    most_common = dt[dt == dt.max(axis=0)]

    consensus = most_common.apply(freq_to_code, axis=0)
    consensus = ''.join(consensus)

    labels, sizes = [], []

    dct = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'R': 0, 'Y': 0, 'S': 0, 'W': 0, 'K': 0, 'B': 0, 'D': 0, 'H': 0, 'V': 0, 'N': 0}
    for i in str(consensus):
        dct[i] += 1

    for x, y in dct.items():
        labels.append(x)
        sizes.append(y)

    plt.pie(sizes, labels=labels)
    plt.savefig('7_2_2.png')
    plt.show()

