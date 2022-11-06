import pandas as pd
from Bio.Seq import Seq
from Bio import motifs
import prestools.bioinf
import seaborn as sns
import numpy as np

data = pd.read_csv('input.6.2.csv').set_index('number')
consensus = motifs.create([Seq(i) for i in data['sequence'].values]).consensus
rotation = []
for i in data['sequence'].values:
    rat = 0
    for j in range(len(i)):
        if i[j] != consensus[j]:
            rat += 1
    rotation.append(rat/len(i))
data['consensus_ratio'] = rotation

ki, jk = [], []
for i in data['sequence'].values:
    try:
        jk.append(prestools.bioinf.jukes_cantor_distance(str(consensus), i))
    except ValueError:
        jk.append(None)

for i in data['sequence'].values:
    try:
        ki.append(prestools.bioinf.kimura_distance(str(consensus), i))
    except ValueError:
        ki.append(None)

data['Jukes_kantor'] = jk
data['Kimura'] = ki

llst = []
for i, row in data.iterrows():
    a = 0
    for j in row.values[1:]:
        if np.isnan(j):
            a = 1
    if a == 1:
        llst.append('not all')
    else:
        llst.append('all')
data['rs'] = llst

fig = sns.violinplot(data, y = 'consensus_ratio', x = 'rs', palette="PRGn", color='skyblue')