
dna_sec = input('Input the DNA Sequence: ')

def DnaToProtein(dna):
    dna = dna.upper()

    print('DNA Sequence: ', dna)

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

    protein_sequence = ''

    for i in range(0, len(dna)-(3+len(dna)%3), 3):
        if protein[dna[i:i+3]] == 'STOP' :
            break
        protein_sequence += protein[dna[i:i+3]]

    print('Protein Sequence: ', protein_sequence)
    return

DnaToProtein(dna_sec)