# coding: utf-8
# Exercise 6.15
"""Graphing frequencies of two dice rolls with Seaborn."""
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
import random 
import seaborn as sns
import sys

def update(frame_number, number_of_rolls, frequencies, faces):
    # we subtract two from the sum of the dice to increment frequencies elements based on index 0
    for i in range(number_of_rolls):
        frequencies[random.randrange(1, 7) + random.randrange(1, 7) - 2] += 1
        
    plt.cla()
    title = f'Rolling Dice {sum(frequencies):,} Times'
    sns.set_style('whitegrid')  # white backround with gray grid lines
    axes = sns.barplot(x=faces, y=frequencies, palette='bright')  # create bars
    axes.set_title(title)  # set graph title
    axes.set(xlabel='Face', ylabel='Frequency')  # label the axes

    # scale y-axis by 10% to make room for text above bars
    axes.set_ylim(top=max(frequencies) * 1.10)

    # display frequency & percentage above each patch (bar)
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0  
        text_y = bar.get_height() 
        text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, 
                  fontsize=11, ha='center', va='bottom')

frequencies = [0] * 11
faces = list(range(2, 13))
number_of_frames = int(sys.argv[1])  
rolls_per_frame = int(sys.argv[2])  
figure = plt.figure('Rolling Two Dice')

dice_animation = animation.FuncAnimation(figure, update, repeat=False, 
    interval=33, frames=number_of_frames, fargs=(rolls_per_frame, frequencies, faces))

plt.show()  # display graph 
