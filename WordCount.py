from sys import argv
from os.path import exists

script, input_file, output_file = argv

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
        file_data = file_data.replace(element, " ")

word_list = file_data.split() #store in a list

dictionary = {}
for word in word_list:
    dictionary[word] = dictionary.get(word, 0) + 1 #add words and increment values

out_file = open(output_file, 'w') #open file
out_file.truncate() #delete everything

for ele in sorted(dictionary):
    string = str(dictionary[ele]) + "\t" + str(ele)
    out_file.write(string)
    out_file.write("\n")

out_file.close()
file_copy.close()
