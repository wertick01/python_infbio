from Bio import SeqIO
import os

filename = '8_1.fasta'
if os.path.isfile(filename):
    os.remove(filename)
outputFile = open(filename, 'a')

with open("8.1 sequence.gb") as input_handle:
    for record in SeqIO.parse(input_handle, "genbank"):
        for feature in record.features:
            if feature.type == "gene" and feature.location.strand == -1:
                SeqIO.write(feature.extract(record), outputFile,'fasta')