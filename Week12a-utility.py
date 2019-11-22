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

#4
def FindWordCount(x, y):
    a = LoadFile(x)
    i = 0
    m = []
    for k in a:
        m += k.split()
    #print(m)
    for p in m:
        if p == y:
            i += 1
    return (i)

#5
def ScoreFinder(x, y):
    
    
    return PrintOutput

#6
def Union(x, y):
    k = []
    k = x + y
    return PrintOutput(k)

#7
def Intersection(x, y):
    k = []
    for n in x:
        for m in y:
            if n == m:
                k.append(n)
                #print(k)
    return (k)

#8
def NotIn(x, y):
    k = []
    for n in x:
        if n not in y:
            k.append(n)
            #print(k)
    return (k)
