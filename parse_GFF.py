#! /usr/bin/env python3

import re
import csv
import argparse
from Bio import SeqIO
from collections import defaultdict

# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature from the genome')

# add positional arguments
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of the FASTA file')

# parse the arguments
args = parser.parse_args()

# read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')

# rev_comp function for Assn7 part 1
def rev_comp(feature_seq, strand):
	if strand == '-':
		return(feature_seq.reverse_complement())
	else:
		return(feature_seq)

# dictionary
gene_dict = defaultdict(dict)

# here goes nothing
# open and read in GFF file
with open(args.gff, 'r') as gff_in:

	# create a csv reader object
	reader = csv.reader(gff_in, delimiter='\t')

	# loop over all the lines in our reader object (i.e., parsed file)
	for line in reader:
		# skip blank lines
		if(not line):
			continue

		# skip comment lines
		elif(re.search('^#', line[0])):
			continue

		# else it's a data line
		else:
			species = line[0]
			feature = line[2]
			start = line[3]
			end = line[4]
			strand = line[6]
			attributes = line[8]
			exon_num = re.search(r"exon\s(\d)", attributes)

			# create entry header
			gene_header = ">" + species.replace(" ", "_") + "_" + attributes.split()[1]

			if feature == "CDS":

				if(not exon_num):
					gene_dict[gene_header] = rev_comp(genome.seq[int(start)-1:int(end)], strand)

				elif(not gene_dict[gene_header]):
					# using 10 placeholder spaces as watermelon.gff doesn't appear to have more than 5 exons for any gene
					gene_dict[gene_header] = [' ']*10

					gene_dict[gene_header][int(exon_num[1])-1] = rev_comp(genome.seq[int(start)-1:int(end)], strand)

				else:
					gene_dict[gene_header][int(exon_num[1])-1] = rev_comp(genome.seq[int(start)-1:int(end)], strand)

for key in gene_dict:
	gene_dict[key] = ''.join(str(exon) for exon in gene_dict[key])

# output
for key, value in gene_dict.items():
	print(key)
	print(value)
	print()
