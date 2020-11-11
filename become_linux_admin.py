#!/usr/bin/python3

"""
    become linux admin: reads text files, devides info by topic and asks user to
    choose which topic to see
"""

__author__  = "Pedro Barreiros"
__email__   = "pxcodename6@gmail.com"

import sys

titles = []
templine = []
linuxfile1 = open(sys.argv[1], "r")
linuxfile2 = open(sys.argv[1], "r")
count = 0

for line in linuxfile1:
    if line.startswith("#-"):
        templine = line.split(" ")
        title = templine[1]
        titles.append(str(count) + " " + title)
        print("(" + str(count) + ") " + title)
        count += 1

choice = str(input("Which title to check? "))

for listTitle in titles:
    if listTitle.split(" ")[0] == choice:
        titlechoice = listTitle.split(" ")[1] 
       
inside = False
for line in linuxfile2:
    if line.startswith("#-"):
        templine = line.split(" ")
        title = templine[1]
        if title == titlechoice:
            print("")
            print(line, end = "")
            inside = True
        else:
            inside = False
    else:
        if inside == True:
            print(line, end = "")


