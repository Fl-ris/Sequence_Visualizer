"""
Sequence visualization script to visualize a DNA sequence as a bitmap with a different color per nucleotide.
Author: Floris M
Date: 14-04-2024
Verion: 1
commandline use: python sequence_visualizer.py Path_to_fasta_file Path_to_output_dir
"""


from PIL import Image
from itertools import zip_longest
from datetime import date, datetime
import sys
# from pandas import factorize



def get_input():
    sequence_path = sys.argv[1]
    output_dir = sys.argv[2]

    return sequence_path, output_dir



       

def open_fasta(sequence_path):
    """
    Opens the fasta file.
    """
    # seq_path = "/home/floris/OneDrive_FLORIS/Project_1/Bioinformatics/bitmap/testfasta.fasta"
    color_list = []

    # Colors for the "A" nucleotide:
    a_color_red = 0
    a_color_green = 0
    a_color_blue = 255

    # Colors for the "T" nucleotide:
    t_color_red = 0
    t_color_green = 255
    t_color_blue = 255

    # Colors for the "G" nucleotide:
    g_color_red = 255
    g_color_green = 0
    g_color_blue = 0

    # Colors for the "C" nucleotide:
    c_color_red = 0
    c_color_green = 255
    c_color_blue = 0

    with open(sequence_path, "r") as sequence:
        next(sequence) # skip header
        for line in sequence:
            for nucleotide in line.strip():
                if nucleotide == "A":
                    color_list.append(tuple((a_color_red, a_color_green, a_color_blue))) # Blue color.
                elif nucleotide == "T":
                    color_list.append(tuple((t_color_red, t_color_green, t_color_blue))) # white
                elif nucleotide == "C":
                    color_list.append(tuple((c_color_red, c_color_green, c_color_blue))) # Purple
                elif nucleotide == "G":
                    color_list.append(tuple((g_color_red, g_color_green, g_color_blue))) # Red
                # else: # Unrecognized nucleotide
                    # color_list.append(0) 
                    # print(f"Error, unrecognized nucleotide in sequence.... {nucleotide}")
                    # print("Placeholder value: 0 inserted.")
                    #return # If the program needs to stop when encountering a wrong nucleotide, uncomment this line. 
                   
            if ">" in line:
                    return color_list
                  
                 
        return color_list



def make_bmp(color_list, ouput_dir):
    img = Image.new( 'RGB', (16,8), "black") # create a new black image
    pixels = img.load() # create the pixel map

 # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    for i, color in zip(range(img.size[0]), color_list): # for every col:
        #print(f"color_l: {i} en {color}") 
        for j in range(img.size[1]):    # For every row
            print(f"Regel: {i} en kolom: {j}")
            # pixels[i,j] = color[0], color[1], color[2] # set the colour accordingly
            pixels[i,j] = i*9,j*9,100 # set the colour accordingly


    # for i in range(img.size[0]):    # for every col:
    #     for j in range(img.size[1]):    # For every row

    #         pixels[i,j] = (i, j, 100) # set the colour 

def make_bmp_test(color_list, output_dir):
    img = Image.new( 'RGB', (8,8), "black") # create a new black image
    pixels = img.load() # create the pixel map

 # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    for  index, (i, color) in enumerate(zip(range(img.size[0]), color_list), start=0): # for every col:
        pixels[index, index] = color # set the colour accordingly

        for ii in range(img.size[0]):    # for every col:

            print(f"color_l: {i} en {color}, index: {index}") 
            pixels[index, ii] = color # set the colour accordingly


    # for i in range(img.size[0]):    # for every col:
    #     for j in range(img.size[1]):    # For every row

    #         pixels[i,j] = (i, j, 100) # set the colour 


    img.show()
    current_time = str(datetime.now())
    img.save(output_dir + current_time + ".bmp", "BMP")
    print(len(color_list))


if __name__ == "__main__":
    sequence_path, output_dir = get_input()
    color_list = open_fasta(sequence_path)
    # make_bmp(color_list, output_dir)
    make_bmp_test(color_list, output_dir)




