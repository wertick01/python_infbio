import matplotlib.pyplot as plt
import pandas as pd

def func711(seq):
    dct = {}
    for i in set(seq):
        dct[i] = seq.count(i)
    dct
    plt.bar(range(len(dct)), list(dct.values()), align='center')
    plt.xticks(range(len(dct)), list(dct.keys()))
    plt.savefig('7_1_1.png')
    plt.show()

def func712(seq):
    dct = {}
    for i in set(seq):
        dct[i] = seq.count(i)
    dct

    labels, sizes = [], []

    for x, y in dct.items():
        labels.append(x)
        sizes.append(y)

    plt.pie(sizes, labels=labels)
    plt.axis('equal')
    plt.savefig('7_1_2.png')
    plt.show()

def func713(seq):
    geneticCode = {'TTT':'F', 'TTC':'F', 'TCT':'S', 'TCC':'S',
                'TAT':'Y', 'TAC':'Y', 'TGT':'C', 'TGC':'C',
                'TTA':'L', 'TCA':'S', 'TAA':None, 'TGA':None,
                'TTG':'L', 'TCG':'S', 'TAG':None, 'TGG':'W',
                'CTT':'L', 'CTC':'L', 'CCT':'P', 'CCC':'P',
                'CAT':'H', 'CAC':'H', 'CGT':'R', 'CGC':'R',
                'CTA':'L', 'CTG':'L', 'CCA':'P', 'CCG':'P',
                'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGG':'R',
                'ATT':'I', 'ATC':'I', 'ACT':'T', 'ACC':'T',
                'AAT':'N', 'AAC':'N', 'AGT':'S', 'AGC':'S',
                'ATA':'I', 'ACA':'T', 'AAA':'K', 'AGA':'R',
                'ATG':'M', 'ACG':'T', 'AAG':'K', 'AGG':'R',
                'GTT':'V', 'GTC':'V', 'GCT':'A', 'GCC':'A',
                'GAT':'D', 'GAC':'D', 'GGT':'G', 'GGC':'G',
                'GTA':'V', 'GTG':'V', 'GCA':'A', 'GCG':'A',
                'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGG':'G'}

    seq = seq[:len(seq)-len(seq) % 3]
    res = []
    for i in range(0, len(seq), 3):
        for key, _ in geneticCode.items():
            if key == seq[i:i+3]:
                res.append(key)
    dct2 = {}
    for i in set(res):
        dct2[i] = 0

    for i in res:
        dct2[i] += 1
    plt.bar(dct2.keys(), dct2.values())
    plt.savefig('7_1_3.png')
    plt.show()

def func714(seq):
    geneticCode = {'TTT':'F', 'TTC':'F', 'TCT':'S', 'TCC':'S',
                'TAT':'Y', 'TAC':'Y', 'TGT':'C', 'TGC':'C',
                'TTA':'L', 'TCA':'S', 'TAA':None, 'TGA':None,
                'TTG':'L', 'TCG':'S', 'TAG':None, 'TGG':'W',
                'CTT':'L', 'CTC':'L', 'CCT':'P', 'CCC':'P',
                'CAT':'H', 'CAC':'H', 'CGT':'R', 'CGC':'R',
                'CTA':'L', 'CTG':'L', 'CCA':'P', 'CCG':'P',
                'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGG':'R',
                'ATT':'I', 'ATC':'I', 'ACT':'T', 'ACC':'T',
                'AAT':'N', 'AAC':'N', 'AGT':'S', 'AGC':'S',
                'ATA':'I', 'ACA':'T', 'AAA':'K', 'AGA':'R',
                'ATG':'M', 'ACG':'T', 'AAG':'K', 'AGG':'R',
                'GTT':'V', 'GTC':'V', 'GCT':'A', 'GCC':'A',
                'GAT':'D', 'GAC':'D', 'GGT':'G', 'GGC':'G',
                'GTA':'V', 'GTG':'V', 'GCA':'A', 'GCG':'A',
                'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGG':'G'}

    seq = seq[:len(seq)-len(seq) % 3]
    res = []
    for i in range(0, len(seq), 3):
        for key, _ in geneticCode.items():
            if key == seq[i:i+3]:
                res.append(key)
    dct2 = {}
    for i in set(res):
        dct2[i] = 0

    for i in res:
        dct2[i] += 1
    pd.DataFrame([dct2.keys(), dct2.values()]).transpose().rename(columns = {0: 'codon', 1: 'freq'}).boxplot(column=['freq'], by=['codon'])