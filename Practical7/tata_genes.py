import re #import necessary library
input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'tata_genes.fa'
with open(input_file, 'r') as infile:
    fasta_data = infile.read().split('>')[1:]
    tata_sequence = re.compile(r'TATA[AT]A[AT]')
with open(output_file, 'w') as output:
    for line in fasta_data:
        first_line, *sequence_lines = line.split('\n')
        gene_name = first_line.lstrip(">").split()[0]
        sequence = ''.join(sequence_lines).replace("\n", "") 
        if gene_name[-1] == "A":
            gene_name = gene_name.split("_mRNA")[0]
            if tata_sequence.search(sequence): 
                output.write(f'{gene_name}\n{sequence}\n')
output.close()