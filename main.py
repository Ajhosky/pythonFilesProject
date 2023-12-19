import csv

file1 = open("./oceny.txt")
file2 = open("przedmioty.txt")
file3 = open("uczniowie.txt")

oceny = file1.read()
print(oceny)
