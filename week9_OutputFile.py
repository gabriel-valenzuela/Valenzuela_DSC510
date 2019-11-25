# File: week9_OutputFile.py
# Name: Gabriel Valenzuela
# Date: 10/27/2019
# Course: DSC 510 - Introduction to Programming
# Purpose: To read a text file and count the frequency of each word within the document and output the results into a
#           file.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: add_word(d, w)
# Desc: Function will count the number of times a word is used within the text
#
# In:   dictionary d - dictionary that the words are being counted in
# In:   string w - the word that is being added to the dictionary or increasing the count too
# Out:  none
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def add_word(d, w):
    if w in d:
        d[w] = d[w] + 1
    else:
        d[w] = 1

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: Process_line(line, d)
# Desc: Function will strip each line of the text of unwanted characters and appropriately space them out to be counted
#
# In:   string line - a line of text from the document
# In:   dictionary d - dictionary the words are going to be counted in
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def Process_line(line, d):
    nonWantedChars = ["-",",",".",""]
    line = line.rstrip()
    line = line.lower()
    for x in line.lower():
        if x in nonWantedChars:
            line = line.replace(x,"")
    words = line.split(" ")
    for word in words:
        add_word(d,word)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: process_file(d, file)
# Desc: Function will write out the appropriate headings and the count of each word within the file that the user
#       wanted it to be written to
#
# In:   dictionary d - dictionary that is going to be written to the file
# In:   string file - name of the file that the count will be written to
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def process_file(d, file):
    blank = d.pop("")
    lengthLine = ("Length of the dictionary: " + str(d.__len__()) + '\n')
    titleLine = ("Word            Count" + '\n')
    longLine = ("_______________________" + '\n')

    sortedList = sorted(d.items(),reverse= True,key=lambda x: x[1])

    with open(file, 'w') as fileHandle:
        fileHandle.writelines([lengthLine, titleLine, longLine])
        for elem in sortedList:
            fileHandle.write('{0:<12} {1:>5}'.format(*elem) + '\n')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Function: main()
# Desc: Function will open and read the text document and call upon other functions to determine the number of each
#       word and display them for the user.
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def main():
    file = open('Gettysburg.txt', "r")
    wordCounter = {}
    for line in file:
            Process_line(line,wordCounter)
    file.close()
    fileNameInputted =  input("What would you like to name the file for your output? ")
    fileNameInputted = fileNameInputted + ".txt"
    process_file(wordCounter, fileNameInputted)


main()
