#!/usr/bin/env python3

from Bio import SeqIO
import sys

# Path to the input FASTA file
fasta_file = sys.argv[1]

# Path to the text file containing the IDs to delete
ids_file = sys.argv[2]

# Read the IDs to delete from the text file
with open(ids_file, 'r') as file:
    ids_to_delete = file.read().splitlines()

# Create a new list to store the filtered sequences
filtered_sequences = []

# Create a set to store the IDs to delete
ids_to_delete_set = set(ids_to_delete)

# Create a set to store the remaining IDs
remaining_ids_set = ids_to_delete_set.copy()

# Iterate over the sequences in the FASTA file
for record in SeqIO.parse(fasta_file, "fasta"):
    # Check if the ID is in the list of IDs to delete
    if record.id not in ids_to_delete_set:
        filtered_sequences.append(record)
    else:
        remaining_ids_set.remove(record.id)

# Write the filtered sequences to a new FASTA file
output_file = "output.fasta"
SeqIO.write(filtered_sequences, output_file, "fasta")

# Check if there are any remaining IDs not identified in the input FASTA file
if remaining_ids_set:
    print(f"The following IDs were not identified in the input FASTA file: {', '.join(remaining_ids_set)}", file=sys.stderr)
