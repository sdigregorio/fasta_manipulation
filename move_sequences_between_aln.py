#!/usr/bin/env python3

from Bio import SeqIO
import sys

# Path to the input FASTA file
input_fasta = sys.argv[1]

# Path to the text file containing the IDs to move
ids_file = sys.argv[2]

# Path to the output FASTA file
output_fasta = sys.argv[3]


#define de method to move sequences between files
def move_sequences(input_fasta, ids_file, output_fasta):
    # Read the IDs from the text file
    with open(ids_file, 'r') as file:
        ids = file.read().splitlines()

    # Create a set to store the IDs to move
    ids_to_move_set = set(ids)

    # Create a set to store the remaining IDs
    remaining_ids_set = ids_to_move_set.copy()

    # Read the input fasta file
    sequences = SeqIO.parse(input_fasta, 'fasta')

    # Read the output fasta file and create a list to store its IDs
    ids_in_output = []

    with open(output_fasta, "r"):
        for record in SeqIO.parse(output_fasta, "fasta"):
            ids_in_output.append(record.description)

    # Filter the sequences based on the IDs and remove the corresponding IDs from remaining_ids_set
    filtered_sequences = []

    for seq_record in sequences:
        if seq_record.id in ids_to_move_set and seq_record.id not in ids_in_output:
            filtered_sequences.append(seq_record)
            remaining_ids_set.remove(seq_record.id)
    
    # Check if there are any remaining IDs not identified in the input FASTA file
    if remaining_ids_set:
        print(f"The following IDs were not identified in the input FASTA file or were already present in the output FASTA file: {', '.join(remaining_ids_set)}", file=sys.stderr)
    else:
        print('Extraction completed successfully.')

    # Append the filtered sequences to the output fasta file
    with open(output_fasta, 'a') as file:
        SeqIO.write(filtered_sequences, file, 'fasta')


# Extract the desired sequences
move_sequences(input_fasta, ids_file, output_fasta)
