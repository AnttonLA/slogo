import sys
import matplotlib.pyplot as plt
from matplotlib import transforms
import matplotlib.patheffects as path_effects
import pandas as pd
import numpy as np
from plotting_script import drawlogo, draw_barplot, draw_logo_plain
from formatting_script import pfm_to_pwd, four_strings, groups_of_four

# Get consensus sequence
def get_consensus_sec(seq_len, bases, prb_dict):
    consensus_sec = ''
    for position in range(seq_len):
        consensus_nuc = 'A'
        for nuc in bases:
            if prb_dict[nuc][position] > prb_dict[consensus_nuc][position]:
                consensus_nuc = nuc
        consensus_sec = consensus_sec + consensus_nuc

    return consensus_sec

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Unexpected number of arguments: ", len(sys.argv)-1)
        print("Usage: slogo_main Data/sample.fasta")

    with open(sys.argv[1], "r") as fasta: # Open input file. Exctract sequences.
        seqs_only = []
        for line in fasta:
            if not line.startswith(">"):
                seqs_only.append(line.strip())

    seq_length = len(seqs_only[0]) # Sequence length
    num_seqs = len(seqs_only) # Number of sequences
    base_list = ['A', 'C', 'G', 'T']

    #Initizalise dictionary
    PFM_dict = {'A': [0] * seq_length, 'C': [0] * seq_length, 'G': [0] * seq_length, 'T': [0] * seq_length}

    #Fill up dictionary
    for sequence in seqs_only:
        position = 0
        for base in sequence:
            PFM_dict[base.upper()][position] += 1
            position += 1
    #Make the frequencies dictionary into a "weights" np.array
    pwd = pfm_to_pwd(PFM_dict, base_list, seq_length, num_seqs)
    #draw_barplot(pwd)
    #sequence = get_consensus_sec(seq_length, base_list, PFM_dict)
    first, second, third, fourth = four_strings(seq_length, PFM_dict)
    nuc_columns = groups_of_four(seq_length, first, second, third, fourth)
    #draw_logo_plain(first + '\n' + second + '\n' + third + '\n' + fourth)
    drawlogo(seq_length, nuc_columns, pwd)
