import pandas as pd
import numpy as np

def pfm_to_pwd(pfm, bases, seq_len, n_seqs):
    #Make the "counts" "dictionary into a weights/frequencies np.array
    pwm = []
    for position in range(seq_len):
        val_A = pfm['A'][position]
        val_C = pfm['C'][position]
        val_G = pfm['G'][position]
        val_T = pfm['T'][position]
        values_at_position = [val_A, val_C, val_G, val_T]
        values = [number / n_seqs for number in values_at_position]
        pwm.append(values)
    np_pwm = np.array(pwm)
    return np_pwm

def four_strings(seq_len, prb_dict):
    #Returns four stringsm, similar structure to a seq logo, only without scale,
    #ordered from most common nucleotide in each position, to least common
    first_string = ''
    second_string = ''
    third_string = ''
    fourth_string = ''

    for position in range(seq_len):
        val_A = prb_dict['A'][position]
        val_C = prb_dict['C'][position]
        val_G = prb_dict['G'][position]
        val_T = prb_dict['T'][position]
        list_of_values = [val_A, val_C, val_G, val_T]
        list_of_values.sort(reverse = True) #Sort biggest to smallest
        order_string = ''
        nuc_list = ['A', 'C', 'G', 'T']
        for number in list_of_values:
            if number == val_A and 'A' in nuc_list:
                order_string += 'A'
                nuc_list.remove('A')
            if number == val_C and 'C' in nuc_list:
                nuc_list.remove('C')
                order_string += 'C'
            if number == val_G and 'G' in nuc_list:
                nuc_list.remove('G')
                order_string += 'G'
            if number == val_T and 'T' in nuc_list:
                nuc_list.remove('T')
                order_string += 'T'
        order_string = order_string[:4]
        #Four value string containgin nucleotides in order of abundance
        #The string is longer if there are identcal values, gotta chop!

        #Fill up the output strings
        first_string += order_string[0]
        second_string += order_string[1]
        third_string += order_string[2]
        fourth_string += order_string[3]

    return first_string, second_string, third_string, fourth_string

def groups_of_four(seq_len, first, second, third, fourth):
    #Returns an array containing the "colums" of the sequence logo
    out_list = []
    for i in range(seq_len):
        column = [first[i] + second[i] + third[i] + fourth[i]]
        out_list.append(column)

    return out_list
