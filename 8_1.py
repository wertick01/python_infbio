from Bio import SeqIO

with open("8.1 sequence.gb") as input_handle:
    for record in SeqIO.parse(input_handle, "genbank"):
        print(record.seq.complement().translate().split('*'))