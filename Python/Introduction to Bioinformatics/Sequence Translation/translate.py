'''
translate.py - translates DNA/RA sequences using the standard genetic code

Author: Yesahel Scicluna (assisted by ChatGPT)

Source: Arthur M. Lesk, Introduction to Bioinformatics. Chapter 1. Problems 1.1, 1.4
- Task Description: see README.md
'''

def translate(sequence):

    print()

    # sets up a dictionary of the standard genetic code
    genetic_code = {
        "ttt": "Phe", "tct": "Ser", "tat": "Tyr", "tgt": "Cys",
        "ttc": "Phe", "tcc": "Ser", "tac": "Tyr", "tgc": "Cys",
        "tta": "Leu", "tca": "Ser", "taa": "TER", "tga": "TER",
        "ttg": "Leu", "tcg": "Ser", "tag": "TER", "tgg": "Trp",
        "ctt": "Leu", "cct": "Pro", "cat": "His", "cgt": "Arg",
        "ctc": "Leu", "ccc": "Pro", "cac": "His", "cgc": "Arg",
        "cta": "Leu", "cca": "Pro", "caa": "Gln", "cga": "Arg",
        "ctg": "Leu", "ccg": "Pro", "cag": "Gln", "cgg": "Arg",
        "att": "Ile", "act": "Thr", "aat": "Asn", "agt": "Ser",
        "atc": "Ile", "acc": "Thr", "aac": "Asn", "agc": "Ser",
        "ata": "Ile", "aca": "Thr", "aaa": "Lys", "aga": "Arg",
        "atg": "Met", "acg": "Thr", "aag": "Lys", "agg": "Arg",
        "gtt": "Val", "gct": "Ala", "gat": "Asp", "ggt": "Gly",
        "gtc": "Val", "gcc": "Ala", "gac": "Asp", "ggc": "Gly",
        "gta": "Val", "gca": "Ala", "gaa": "Glu", "gga": "Gly",
        "gtg": "Val", "gcg": "Ala", "gag": "Glu", "ggg": "Gly"
        }

    # eliminates potential supply of space characters
    sequence = sequence.replace(' ', '')

    # accomodates supply of RNA sequences
    sequence = sequence.replace('u', 't')
    
    # stores all possible forward reading frames
    frames = [sequence, sequence[1:], sequence[2:]]
    
    # stores all possible reverse reading frames
    frames.extend([sequence[::-1], sequence[-2::-1], sequence[-3::-1]])
    
    # initialises list in which to store translations
    peptides = [''] * 6
    
    # loops over each possible reading frame
    for index, frame in enumerate(frames):

        # initialises lists in which to store codons, amino_acids
        codons = []
        amino_acids = []

        # loops over each codon (triplet of bases) in sequence
        for base in range(0, len(frame)-2, 3):    
            codon = frame[base:base+3]
            
            # checks codon validity
            if codon in genetic_code:
                codons.append(codon)

                # translates genetic code, constructs peptide chain 
                # terminates translation upon signal
                amino_acid = genetic_code[codon]
                if amino_acid == 'TER':
                    amino_acids.append(amino_acid)
                    break
                amino_acids.append(amino_acid)                
            
            # crashes program if codon validity check is failed
            # indicates source of invalidity
            else:
                import re
                mark = re.sub('[^atucg]', '^', frame)
                mark = re.sub('[^^]', ' ', mark)
                raise Exception(f"Invalid bases supplied\n'{frame}'\n {mark}")

        # reformats reading frame to reveal codons
        frames[index] = ' '.join(codons)

        # stores peptide chain as  string
        peptides[index] = ' '.join(amino_acids)

    # prints translations
    print('Forward Frame 1:', frames[0], peptides[0], sep='\n', end='\n\n')
    print('Forward Frame 2:', frames[1], peptides[1], sep='\n', end='\n\n')
    print('Forward Frame 3:', frames[2], peptides[2], sep='\n', end='\n\n')
    print('Reverse Frame 1:', frames[3], peptides[3], sep='\n', end='\n\n')
    print('Reverse Frame 2:', frames[4], peptides[4], sep='\n', end='\n\n')
    print('Reverse Frame 3:', frames[5], peptides[5], sep='\n', end='\n\n')

# tests function
print('-'*100, '\n\nTEST 1')
translate('actatctatattcgcccgatacggagtagcttaa')
print('-'*100, '\n\nTEST 2')
translate(' atgag cgtt gagt act cgta gcgatat ga ')
print('-'*100, '\n\nTEST 3')
translate('agcgauacaucagugugaugaugaucgguauauau')
print('-'*100, '\n\nTEST 4')
translate('atgatcgabgagctagbctagtagcb')