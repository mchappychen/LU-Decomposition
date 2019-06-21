def multiply(a,b): #returns: [] of a x b[]
    if(a == 0):
        exit("Error in multiply(): You can't multiply matrix by 0")
    result = []
    for element in b:
        result.append(round(element * a,1))
    return result

def add(a,b): #returns [] of a[]+b[]
    result = []
    if(len(a) != len(b)):
        exit("Error in add(a,b): length of a[] not equal to length of b[]")
    for i in range(len(a)):
        result.append(round(a[i]+b[i],1))
    return result

def printMatrix(a): #prints a matrix
    for x in a:
        string = "|\t"
        for y in x:
            string += str(round(y,1)+0)+"\t"
        string += "|"
        print(string)
