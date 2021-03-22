#! /usr/bin/env python3

# This script will return general composition statistics for an inputted fasta file.

# change fasta file
filename = 'nad4L.fasta'

# open the input file, assign to file handle called 'infile'
infile = open(filename, 'r')

# read the file
dna_sequence = infile.read().rstrip()

# print the DNA sequence
#print(dna_sequence)

# close the file
infile.close()

# print the sequence length
seqlen = len(dna_sequence)
print('Sequence length: ', seqlen)


# frequency of A
numA = dna_sequence.count('A')
freqA = round((numA/seqlen), 3)
print('Freq of A: ', freqA)

# frequency of C
numC = dna_sequence.count('C')
freqC = round((numC/seqlen), 3)
print('Freq of C: ', freqC)

# frequency of G
numG = dna_sequence.count('G')
freqG = round((numG/seqlen), 3)
print('Freq of G: ', freqG)

# frequency of T
numT = dna_sequence.count('T')
freqT = round((numT/seqlen), 3)
print('Freq of T: ', freqT)

# frequency of G+C
numGC = numG + numC
freqGC = round((numGC/seqlen), 3)
print('G+C content: ', freqGC)

# check that frequencies sum to 1
freq_sum = freqA + freqC + freqG + freqT
print('Sum of frequencies: ', freq_sum)
