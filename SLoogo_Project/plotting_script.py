import sys
import matplotlib.pyplot as plt
from matplotlib import transforms
import matplotlib.patheffects as path_effects
import pandas as pd
import numpy as np

def drawlogo(seq_len, nuc_columns, nuc_freqs):
    fig, ax = plt.subplots()
    fig.set_size_inches(seq_len/2,5) #TODO: horizontal size proportional to seq length
    #it will require to change step-size in the for loop as well
    canvas = ax.figure.canvas
    nuc_columns = nuc_columns
    step_size = 1/(seq_len+1)
    x = step_size
    size_factor = 45 #multiply frequency by this factor to get final size
    for col, freqs in zip(nuc_columns, nuc_freqs):
        recol = list(reversed(col[0]))
        t = ax.transData
        for letter in recol:
            if letter == 'A':
                color= 'red'
                siz = freqs[0]*size_factor
            if letter == 'C':
                color= 'blue'
                siz = freqs[1]*size_factor
            if letter == 'G':
                color= 'green'
                siz = freqs[2]*size_factor
            if letter == 'T':
                color= 'black'
                siz = freqs[3]*size_factor
            #TODO: Get size data and tweek the size of each character
            text = ax.text(x, 0.42, letter + " ", color=color, transform=t,
                           rotation=0, va='bottom', ha='center', size=siz)
            text.draw(canvas.get_renderer())
            ex = text.get_window_extent()
            t = transforms.offset_copy(text._transform, y=ex.height, units='dots')
        x += step_size
    plt.show()

def draw_barplot(pwd):
    #Function that makes the inputed numpy array (Nx4) into a stacked barplot
    df = pd.DataFrame(pwd,columns=['A','C','G','T'])
    df.plot.bar(stacked=True)

def draw_logo_plain(input_string):
    #Draws the "logo" without altered sizes or colors
    fig = plt.figure(figsize=(5, 1.5))
    text = fig.text(0.5, 0.5, input_string, ha='center', va='center', size=20)
    text.set_path_effects([path_effects.Normal()])
    plt.show()
'''
    for letter, size in zip(string,sizes):
        text = ax.text(0.3, 0.2, letter + " ", color='blue', transform=t,
                       rotation=0, va='bottom', ha='center', size=size)
        text.draw(canvas.get_renderer())
        ex = text.get_window_extent()
        t = transforms.offset_copy(text._transform, y=ex.height, units='dots')
    #text = fig.text(0.5, 0.5, 'A',ha='center', va='bottom', size=25)
    #text2 = fig.text(0.5, 0.5, 'C',ha='center', va='baseline', size=10 )
'''
