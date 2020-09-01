from sys import argv
from os.path import exists

script, inout_file, output_file = argv

print(f"Dies input file exist? {exists(input_file)}")
print(f"Does output file exist? {exists(output_file)}")
print("hit RETURN to continue, CTRL-C to abort.")
input()
