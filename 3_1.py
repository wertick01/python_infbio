print('\n#3.1')

dna_sec = input('Input the DNA Sequence: ')

def FindStartPosition(seq):
    return seq.find('ATG')


def DnaToProtein(dna):
    dna = dna.upper()

    dna = [dna, dna[1:], dna[2:]]

    for seq in dna:
        start = FindStartPosition(seq)
        if start != -1:
            seq = seq[start:]

    print(dna[0])
    print('-', dna[1], sep = '')
    print('--', dna[2], sep = '')

    protein = {
            "TTT" : "F", "CTT" : "L", "ATT" : "I", "GTT" : "V",
            "TTC" : "F", "CTC" : "L", "ATC" : "I", "GTC" : "V",
            "TTA" : "L", "CTA" : "L", "ATA" : "I", "GTA" : "V",
            "TTG" : "L", "CTG" : "L", "ATG" : "M", "GTG" : "V",
            "TCT" : "S", "CCT" : "P", "ACT" : "T", "GCT" : "A",
            "TCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
            "TCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
            "TCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
            "TAT" : "Y", "CAT" : "H", "AAT" : "N", "GAT" : "D",
            "TAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
            "TAA" : "STOP", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
            "TAG" : "STOP", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
            "TGT" : "C", "CGT" : "R", "AGT" : "S", "GGT" : "G",
            "TGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
            "TGA" : "STOP", "CGA" : "R", "AGA" : "R", "GGA" : "G",
            "TGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
            }

    index = 0
    for seq in dna:
        protein_sequence = ''
        for i in range(0, len(seq)-(index+len(seq)%3), 3):
            if protein[seq[i:i+3]] == 'STOP' :
                break
            protein_sequence += protein[seq[i:i+3]]

        print(f'Protein Sequence [ramk +{index}]: ', protein_sequence)
        index += 1
    return

DnaToProtein(dna_sec)