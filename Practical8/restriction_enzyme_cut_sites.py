import re
def restriction_sites(dna_sequence, enzyme_sequence):
    
    if not re.fullmatch(r'[ACGT]+', dna_sequence.upper()):
        raise ValueError("DNA sequence contains invalid characters. Only A, C, G, T are allowed.")
    if not re.fullmatch(r'[ACGT]+', enzyme_sequence.upper()):
        raise ValueError("Enzyme recognition sequence contains invalid characters. Only A, C, G, T are allowed.")
    if enzyme_sequence not in dna_sequence:
        raise ValueError("The enzyme sequence is not included in the DNA sequece.")
    
    dna_sequence = dna_sequence.upper()
    enzyme_sequence = enzyme_sequence.upper()
    
    positions = []
    for i in range(len(dna_sequence) - len(enzyme_sequence) + 1):
        if dna_sequence[i:i + len(enzyme_sequence)] == enzyme_sequence:
            positions.append(i+1)
    
    return positions

dna = "ACGTACGTAGCTAGCTAGCTAGCTAGC"
enzyme = "XACT"
cut_sites = restriction_sites(dna, enzyme)
print(f"Restriction enzyme sites found at positions: {cut_sites}")

                    
                    
                    