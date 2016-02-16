#Apriori

import sys

#########################################       FORM CANDIDATE COMBINATIONS        #####################################################

#parameters : frequencylist of previous pass, same list with one less element
def candidatepairs(prevfreqList,prevfreqList1):
    candidateList = []
    for val1 in prevfreqList:
        for val2 in prevfreqList1:
            if i is 2 and val1 is not val2:
                val = set([val1,val2])
                candidateList.append(tuple(sorted(val)))
            elif i > 2 and val1 != val2:
                if(len(set(val1)&set(val2)) == i-2):
                    val = set(val1)| set(val2)
                    candidateList.append(tuple(sorted(val))) 
            
    candidateSet = set(candidateList)
    return candidateSet
#####################################################   FORM FREQUENT COMBINATIONS    ##############################################################

# parameters : candidate pairs, inputFile
def freqPairs(candPair,b_list):
    candidates = {}
    global i
    for x in candPair:
        for y in b_list.values():
            if len(set(x)&set(y)) is len(x):
                if x not in candidates:
                    candidates[x] = 1
                else:
                    candidates[x] = candidates[x] + 1
    freqList = [x[0] for x in candidates.items() if x[1] > min_sup-1]
    if len(freqList) > 0:
        print('Frequent Itemsets of size ',i)
        freqList = sorted(freqList)
        # printing freq-list
        for x in freqList:
            j = 0
            for y in x:
                if j == len(x)-1:
                   print(y,end = "\n") 
                else:
                    print(y,end = ",")
                j = j+1
    print("")       
    i = i+1
    return freqList
################################################      MAIN PROGRAM TO READ INPUT FILE AND CREATE FREQUENT ITEM SETS     ####################################  

b_list = {}
i= 1 #stores count of pass
count1 = 0
itemSize1 = {};
min_sup = int(sys.argv[2])
print("")
inputdata = open(sys.argv[1])
# read the input file and create buckets for each line
# word count - for creating frequency list 1
for line in inputdata:
    i = i+1
    wordlist=[]
    line = line.rstrip('\n')
    words = line.split(',')
    for word in words:
        wordlist.append(word)
        if word not in itemSize1:
            itemSize1[word] = 1
        else:
            itemSize1[word] = itemSize1[word] + 1
    b_list[i] = wordlist
#create frequency list of size 1
freqList = [x[0] for x in itemSize1.items() if x[1] > min_sup-1]     
print("Frequent Itemsets of size 1")
print("\n".join([x for x in sorted(freqList)]))
print("")
i = 2
prevfreqList = sorted(freqList)
#APRIORI - Runs as long as frequency list is not null for any number of passes. User can also put a limit here on howmany turns to run the algorithm
while len(prevfreqList) > 0:
    # create candidate pairs for every pass
    candPair = candidatepairs(prevfreqList,prevfreqList[1:len(prevfreqList)])
    # output freq list if candidate pair support is >= min support given by user
    prevfreqList = freqPairs(candPair,b_list)
