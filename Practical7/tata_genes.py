import re #import library

gene_dict = {}
seq = ''
current_gene = None

with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as input_file: #input file
    for line in input_file:
        line = line.strip()
        if re.search(r'^>',line): #find the lines with gene names
            if current_gene:
                gene_dict[current_gene] = seq
            match = re.search(r'gene:(\S+)', line) #get the name
            if match:
                current_gene = match.group(1)
            else:
                current_gene = line[1:].split()[0]  
            seq = ''
        else:
            seq += line

    if current_gene:
        gene_dict[current_gene] = seq

tata_genes = {}
for gene, seq in gene_dict.items():
    if gene and re.search(r'TATA[AT]A[AT]', seq): #find the sequence
        tata_genes[gene] = seq

with open('tata_genes.fa', 'w') as output_file: #output file
    for gene, seq in tata_genes.items():
        output_file.write(f'>{gene}\n{seq}\n') #output