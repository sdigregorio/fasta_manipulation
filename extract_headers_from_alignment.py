#!/usr/bin/env python3
from Bio import SeqIO
import sys

# Path to the input FASTA file
fasta_file = sys.argv[1]

# Create a new list to store the headers of sequences
headers = []

with open(fasta_file, "r"):
    for record in SeqIO.parse(fasta_file, "fasta"):
        headers.append(record.description)

print(headers)