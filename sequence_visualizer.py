"""
Sequence visualization script to visualize a DNA sequence as a bitmap with a different color per nucleotide.
Author: Floris M
Date: 14-04-2024
Verion: 1

"""


from PIL import Image
from itertools import zip_longest
import sys
# from pandas import factorize



def get_input():
    sequence_path = sys.argv[1]
    output_dir = sys.argv[2]

    return sequence_path, output_dir



       

def open_fasta(sequence_path, output_dir):
    """
    Opens the fasta file.
    """
    # seq_path = "/home/floris/OneDrive_FLORIS/Project_1/Bioinformatics/bitmap/testfasta.fasta"
    color_list = []
    with open("/home/floris/OneDrive_FLORIS/Project_1/Bioinformatics/bitmap/testfasta.fasta", "r") as sequence:
        next(sequence) # skip header
        for line in sequence:
            for nucleotide in line.strip():
                if nucleotide == "A":
                    color_list.append(tuple((0,0,255))) # Blue color.
                elif nucleotide == "T":
                    color_list.append(tuple((255,255,255))) # white
                elif nucleotide == "C":
                    color_list.append(tuple((100,0,233))) # Purple
                elif nucleotide == "G":
                    color_list.append(tuple((255, 0, 0))) # Red
                else: # Unrecognized nucleotide
                    color_list.append(0) 
                    print(f"Error, unrecognized nucleotide in sequence.... {nucleotide}")
                    print("Placeholder value: 0 inserted.")
                   
            if ">" in line:
                    return color_list
                  
                 
        return color_list



def make_bmp(color_list):
    img = Image.new( 'RGB', (1920,1080), "black") # create a new black image
    pixels = img.load() # create the pixel map

 # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    for i, color in zip(range(img.size[0]), color_list): # for every col:
        print(f"color_l: {i} en {color}") 
        for j in range(img.size[1]):    # For every row
            pixels[i,j] = color[0], color[1], color[2] # set the colour accordingly
           # pixels[i,j]=  234 # set the colour accordingly

    # for i in range(img.size[0]):    # for every col:
    #     for j in range(img.size[1]):    # For every row

    #         pixels[i,j] = 44 # set the colour 


    img.show()
    img.save("/home/floris/OneDrive_FLORIS/Project_1/Bioinformatics/bitmap/img.bmp", "BMP")
    print(len(color_list))


if __name__ == "__main__":
    sequence_path, output_dir = get_input()
    color_list = open_fasta(sequence_path, output_dir)
    make_bmp(color_list)



