import random

filename = ["adjectives.txt","actions.txt","areas.txt"]
list = [[]]*3

for i in range(0,3):
    with open(filename[i]) as infile:
        list[i] = infile.readlines()
        list[i] = [x.strip() for x in list[i]]

numGen = input("Generate how many names? ")
print "Generating", numGen, "names."

for j in range(0,numGen):
    for i in range(0,3):
        listNum = random.randrange(0,len(list[i]))
        print list[i][listNum],
    print
