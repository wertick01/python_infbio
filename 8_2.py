from Bio.Seq import Seq
from Bio import motifs

instances = []

with open('8.2 sequences.txt', 'r') as file:
    for line in file:
        instances.append(Seq(line.strip()))
pwm = motifs.create(instances).counts.normalize(pseudocounts=0.5).log_odds()
print(pwm)