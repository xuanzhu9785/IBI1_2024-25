import re
splice_combination=input("Enter slice combination (GTAG, GCAG, ATAC):")
filename = f"{splice_combination}_spliced_genes.fa"

dict = {}
seq = ''
current_gene = None

with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as input_file:
    for line in input_file:
        line = line.strip()
        if re.search(r'^>',line):
            if current_gene:
                dict[current_gene] = seq
            match = re.search(r'gene:(\S+)', line)
            if match:
                current_gene = match.group(1)
            else:
                current_gene = line[1:].split()[0]  
            seq = ''
        else:
            seq += line
    if current_gene:
        dict[current_gene] = seq

with open(filename, 'w') as output_file: #output file
    for gene_name, gene_seq in dict.items():
        tata_matches = re.findall(r'TATA[AT]A[AT]', gene_seq) #find the sequence
        count = len(tata_matches)
        if count == 0:
            continue

        if splice_combination in gene_seq:
            output_file.write(f">{gene_name} TATA_count:{count}\n")
            output_file.write(f"{gene_seq}\n")

print(f"Output file: {filename}") #output