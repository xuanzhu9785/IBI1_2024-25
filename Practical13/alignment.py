
human = "MLSRAVCGTSRQLAPVLGYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"
mouse = "MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"
random = "LATEAIHIYFSISDKYFAKVMTFIVMFSRSLTWNIFTVCTQKDGHVERAECCHIKKAHKHTPMQCRVFSRGQMGMNNFCKDPEASTHAIKPLQANDHSHADVNKRKGLPNKWKRNDDFKSCEDYFDVYYFSCWPIDCLHMHEVRCIYWTPCRANMVVFYKYHQCMPDSDLVDRKCPNNDEIIETWFSFMHMQQDFILSCTGQKSFGSGVSSIYSEDCRWPAK"

# Step 2: Load BLOSUM62 matrix
def load_blosum62(filepath):
    matrix = {}
    with open(filepath) as f:
        lines = [line.strip() for line in f if not line.startswith("#") and line.strip()]
        header = lines[0].split()
        for line in lines[1:]:
            parts = line.split()
            row_aa = parts[0]
            scores = list(map(int, parts[1:]))
            matrix[row_aa] = dict(zip(header, scores))
    return matrix

blosum62 = load_blosum62("BLOSUM62.txt")

# Step 3: Alignment function
def align(seq1, seq2, matrix):
    score = 0
    identity = 0
    for a1, a2 in zip(seq1, seq2):
        if a1 == a2:
            identity += 1
        score += matrix[a1][a2]
    percent_identity = (identity / len(seq1)) * 100
    return score, percent_identity

# Step 4: Run all pairs
pairs = [
    ("Human vs Mouse", human, mouse),
    ("Human vs Random", human, random),
    ("Mouse vs Random", mouse, random),
]

for name, seq1, seq2 in pairs:
    score, percent_id = align(seq1, seq2, blosum62)
    print(f"{name}:")
    print(f"  Alignment score: {score}")
    print(f"  Percentage identity: {percent_id:.2f}%\n")
