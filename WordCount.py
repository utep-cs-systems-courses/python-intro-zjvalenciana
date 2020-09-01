from sys import argv
from os.path import exists

script, inout_file, output_file = argv

print(f"Dies input file exist? {exists(input_file)}") #check if files exist
print(f"Does output file exist? {exists(output_file)}")
print("hit RETURN to continue, CTRL-C to abort.")
input()

file_copy = open(input_file, 'r') #open file
file_data = file_copy.read() #read file and store file_data

file_data = file_data.lower() #replace uppercase with lowercase

punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~''' #non alphabetical characters
for element in file_data: #traverse file and remove all non letters
    if element in punc:
        file_data = file_data.preplace(element, " ")
