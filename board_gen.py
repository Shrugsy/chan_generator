import random

f0 = "adjectives.txt"
f1 = "actions.txt"
f2 = "areas.txt"

listOne = []
listTwo = []
listThree = []

filename = [f0,f1,f2]
list = [listOne, listTwo, listThree]
listNum = [0]*3

for i in range(0,3):
    with open(filename[i]) as infile:
        list[i] = infile.readlines()
        list[i] = [x.strip() for x in list[i]]
##    print 'iteration = ', i
##    print 'list = ', list[i]
##    print 'list choice number = ', listNum[i]
##    print list[i][listNum[i]]
##    print '\n'

numGen = input("Generate how many names? ")
print "Generating ", numGen, "names."

for j in range(0,numGen):
    for i in range(0,3):
        listNum[i] = random.randrange(0,len(list[i]))
        assert (0 <= listNum[i] <= len(list[i]))
        print list[i][listNum[i]],
    print
