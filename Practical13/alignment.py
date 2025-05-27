import re
#input sequences
human = "MLSRAVCGTSRQLAPVLGYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"
mouse = "MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"
random = "LATEAIHIYFSISDKYFAKVMTFIVMFSRSLTWNIFTVCTQKDGHVERAECCHIKKAHKHTPMQCRVFSRGQMGMNNFCKDPEASTHAIKPLQANDHSHADVNKRKGLPNKWKRNDDFKSCEDYFDVYYFSCWPIDCLHMHEVRCIYWTPCRANMVVFYKYHQCMPDSDLVDRKCPNNDEIIETWFSFMHMQQDFILSCTGQKSFGSGVSSIYSEDCRWPAK"

def load_blosum62(filepath):
    matrix = {}
    with open(filepath) as file:
        lines = []
        for line in file:
            line = line.strip()
            if line and not re.search(r'^#', line):
                lines.append(line)
                header = lines[0].split()
                for line in lines[1:]:
                    parts = line.split()
                    row = parts[0]
                    scores = []
                    for s in parts[1:]:
                        scores.append(int(s))
                    row_dict = {}
                    for key, score in zip(header, scores):
                        row_dict[key] = score
                    matrix[row] = row_dict
    return matrix

blosum62 = load_blosum62("BLOSUM62.txt")#Load BLOSUM62 matrix

def align(seq1, seq2, matrix):
    score = 0
    identity = 0
    for a1, a2 in zip(seq1, seq2):
        if a1 == a2:
            identity += 1
        score += matrix[a1][a2]
    percent_identity = (identity / len(seq1))*100
    return score, percent_identity

pairs = [("Human vs Mouse", human, mouse),("Human vs Random", human, random),("Mouse vs Random", mouse, random),]

for name, seq1, seq2 in pairs:
    score, percent_identity = align(seq1, seq2, blosum62)
    print(f"{name}:")
    print(f" Score: {score}")
    print(f" Percentage identity: {percent_identity:.2f}%\n")
