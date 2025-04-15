def cut_sites(DNA_sequence, enzyme_sequence):
    bases = {'A', 'C', 'G', 'T'}
    def validate_sequence(seq, label="DNA"):
        for base in seq.upper():
            if base not in bases:
                raise ValueError(f"{label} sequence contains invalid character: {base}")
            validate_sequence(DNA_sequence, "DNA")
            validate_sequence(enzyme_sequence, "Enzyme")
    positions = []
    for i in range(len(DNA_sequence) - len(enzyme_sequence) + 1):
        if DNA_sequence[i:i+len(enzyme_sequence)].upper() == enzyme_sequence.upper():
            positions.append(i)

    return positions

print("Cut positions:", cut_sites("ACTGACTGA", "ACT"))
