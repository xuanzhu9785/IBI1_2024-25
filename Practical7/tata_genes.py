#import re
#openfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
#input_file=openfile.read()
#tata_sequence=re.findall(r'\n[A-Z\n]+.+TATA[AT]A[AT]+[A-Z\n]+\n',input_file)
#gene_name=re.findall(r'>(\S+)_.+[A-Z\n]+\S+TATA[AT]A[AT]+[A-Z\n]+',input_file)
#output=open('tata_genes.fa','w')
#for line in gene_name:
#    if line[0]==">":
#        continue
#    else:
#        line=line.strip()
#for i in range(len(tata_sequence)):
#    output .write(str(gene_name[i]))
#    output.write(tata_sequence[i])
#output.close()
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
            gene_name = gene_name.lstrip(">").split("_mRNA")[0]
            if tata_sequence.search(sequence): 
                output.write(f'>{gene_name}\n{sequence}\n')
