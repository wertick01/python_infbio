print('\n#4.2')

from Bio import SeqIO

geneticCode = {'TTT':'F', 'TTC':'F', 'TCT':'S', 'TCC':'S',
                   'TAT':'Y', 'TAC':'Y', 'TGT':'C', 'TGC':'C',
                   'TTA':'L', 'TCA':'S', 'TAA':"*", 'TGA':"*",
                   'TTG':'L', 'TCG':'S', 'TAG':"*", 'TGG':'W',
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

def SeqSplitter(sequence):
    return {
        "0": sequence[:len(sequence)-len(sequence)%3],
        "+1": sequence[1:][:len(sequence[1:])-len(sequence[1:])%3],
        "+2": sequence[2:][:len(sequence[2:])-len(sequence[2:])%3],
    }
    
def FindStartPosition(sequence):
    return sequence.find('ATG')

def Translate(sequence):
    result = ""
    for i in range(0, len(sequence), 3):
        result += geneticCode[sequence[i:i+3]]
    return result

def Ramks(path, format):
    dct = {}
    for record in SeqIO.parse(path, format):
        dct[record.id] = SeqSplitter(str(record.seq))
    return dct

def Descriptor(protein, seq_type, start, end, M, stop):
    return {
        "Sequence": protein,
        "Type": seq_type,
        "Start": start,
        "End": end,
        "M": M,
        "STOP": stop,
    }

def TranslateHelper(protein):
    lst = []
    sec_type = None
    M = False
    start = 0
    if "*" in protein:
        for i in protein.split("*"):
            sec_type = None
            M = False
            if len(i) > 0:
                if "M" in i:
                    start = i.find("M")
                    sec_type = "complete"
                    M = True
                    i = i[start:]
                lst.append(Descriptor(i, sec_type, start*3, len(i)*3+start*3, M, True))
    else:
        if "M" in protein:
            start = protein.find("M")
            M = True
            protein = protein[start:]
        else:
            sec_type = "empty"
        lst.append(Descriptor(protein, sec_type, start*3, len(protein)*3+start*3, M, False))
    return lst

def Translated(path, format):
    ramked = Ramks(path, format)
    for id, ramks in ramked.items():
        for ramk, seq in ramks.items():
            ramks[ramk] = TranslateHelper(Translate(seq))
    return ramked

print(Translated("input.4.2.txt", "fasta"))