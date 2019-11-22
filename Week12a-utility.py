 #   incremental build model 
#   kimberly mielke
 #  ​CSCI 102 – Section A 
#   Week 12 - Part A 



#1
def PrintOutput(x):
    print('OUTPUT', x)

#2
def LoadFile(x):
    lis = []
    txt = open(x, 'r')
    #print(txt)
    doc = txt.readlines()
    #print(doc)
    for n in doc:
        lis.append(n.strip())
    return (lis)

#3
def UpdateString(x, y, z):
    k = ''
    for i in range(len(x)):
        if i != z:
            k += x[i]
        else:
            k += y
    return (k)
    #print(k)
