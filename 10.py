import requests
import re
import matplotlib.pyplot as plt
from scipy import stats

class Gene:
    def __init__(self, entry, organism, motif, aaseq, ntseq):
        self.entry = entry
        self.organism = organism
        self.motif = motif
        self.aaseq = aaseq
        self.ntseq = ntseq

def Pfam(content):
    obj = re.search(r"Pfam: (.*?)\n", content)
    if obj is not None:
        return obj.group(1).split()
    else:
        return None

def Aaseq(content):
    obj = re.search(r"AASEQ[\s|\S]*NTSEQ", content)
    if obj is not None:
        return "".join(obj.group(0).split()[2:-1])
    else:
        return None

def Ntseq(content):
    obj = re.search(r"NTSEQ[\s|\S]*", content)
    if obj is not None:
        return "".join(obj.group(0).split()[2:-1])
    else:
        return None

gene = "hsa:7314"
text = requests.get("https://rest.kegg.jp/get/" + gene).text
name, entry = gene.split(":")

parsed_gene = Gene(entry, name, Pfam(text), Aaseq(text), Ntseq(text))

print("#10.1:\n", parsed_gene.entry, parsed_gene.organism, parsed_gene.motif, parsed_gene.aaseq, parsed_gene.ntseq)
print("\n")

def Pie():
    _, ax = plt.subplots()
    ax.pie(
        list(map(lambda x: parsed_gene.ntseq.count(x), ['a', 't', 'g', 'c'])), 
        labels=['a', 't', 'g', 'c'], 
        autopct='%1.1f%%', 
        startangle=100,
    )
    plt.title("Распределение частот нуклеотидов в сиквенсе")
    plt.show();

print(list(parsed_gene.aaseq))

def Bar():
    _ = plt.figure(figsize = (16, 9))
    lst = list(parsed_gene.aaseq)
    plt.bar(
        lst, 
        list(map(lambda x: parsed_gene.aaseq.count(x), lst)), 
        width = 0.4,
    )
    plt.xlabel("Amino acid")
    plt.ylabel("Amino acid frequency")
    plt.title("Distribution")
    plt.show()

print("#10.2:\n")
Pie()
Bar()
print("\n")

text = requests.get("https://www.kegg.jp/ssdb-bin/ssdb_best?org_gene=hsa:7314").text

ortologs = re.findall(r"TARGET.*?&", text)

sw_scores = []
for i in ortologs:
    sw_scores.append(re.compile(r'\d+\s+\(').search(i).group(0))
sw_scores = [int(i.split()[0]) for i in sw_scores]

identities = []
for entry in ortologs:
    identities.append(re.compile(r'\d\.\d+').search(entry).group(0))
identities = [float(i) for i in identities]

print("#10.3:\n")
print("Correlation between 10:", stats.pearsonr(sw_scores[:10], identities[:10]))
print("Correlation between 100:", stats.pearsonr(sw_scores[:100], identities[:100]))
print("Correlation between all:", stats.pearsonr(sw_scores, identities))
print("\n")


sub_pattern = re.compile(r'HREF="')

def link_builder(pattern):
    clean_links = []
    for i in re.findall(r"HREF=[\S]+:\d+", text):
        clean_links.append(pattern.sub(r"", i))
    return clean_links

def helper(link):
    text = requests.get(link).text
    obj = re.findall(r'entry.pf.*?"', text)
    return [i.split(":")[-1].replace('"', '') for i in obj]

def motifier(links_lst, n):
    motifs = []
    for url in links_lst[:n]:
        cur_motifs = helper(url)
        motifs += cur_motifs
    return list(set(motifs)), list(map(lambda x: motifs.count(x), set(motifs)))

def Cert(links_lst, n):
    labels, sizes = motifier(links_lst, n)
    _ = plt.figure(figsize = (16, 9))
    plt.bar(labels, sizes, width = 0.4)
    plt.xlabel("Domain")
    plt.ylabel("Frequency in protein")
    plt.title("Distribution")
    plt.show()

print("#10.4:\n")
Cert(link_builder(sub_pattern), 10)
Cert(link_builder(sub_pattern), 100)

