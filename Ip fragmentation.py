import math


def calculatemtu(iterations):
    for i in range(1, iterations + 1):
        if i == iterations:
            x = data - MtuW * (iterations - 1)
            lst.append(x)
        else:
            lst.append(MtuW)
    return (lst);

def calculatemtuE(lst):

    for i in range(1, iterations + 1):
        if i == iterations:
            x = data - MtuW * (iterations - 1)
            lst.append(x)
        else:
            lst.append(MtuW)
    return (lst);


def calcualateoffset(lst):
    var=0
    offset.append(var)
    for i in range(0, len(lst)):
        var = lst[i] / 8
        offset.append(var)
    return (offset);


def calculatesumoff(offset):
    for i in range(0, len(offset)):

        if i == 0:
            var = 0
            sum1.append(var)
        else:
            var = sum(offset[:i+1])
            sum1.append(var)
    return (sum1);


mf = []


def calculatemf(lst):
    for i in range(0, len(lst)):
        if i == len(lst)-1:
            var = 0
            mf.append(var)
        else:
            var = 1
            mf.append(var)
    return mf


def printlist(names, list1, sum1, mf):
    for i in range(0, len(lst)):
        var = lst[i] + 20
        list1.append(var)
    n = len(lst)
    print(f"There can be {names[n - 1]} fragments send:")
    for (a, f, b, c) in zip(names, list1, sum1, mf):
        print(f"The {a} fragment data size is {f} , offset = {b} ,MF flag = {c}")


def calculatemtuE(lst,Mtu):
    iterations = data / Mtu
    iterations = math.ceil(iterations)
    print(iterations)
    for i in range(0, len(lst)):
        if lst[i]>Mtu:
            var=lst[i]
    for j in range(1, iterations):
        if var<Mtu:
            list2.append(var)
        else:
            list2.append(Mtu)
            var=var-Mtu
    for i in range(0, len(lst)):
        if lst[i]<Mtu:
            list2.append(lst[i])
    return (list2);


data = int(input("Enter The Packet Size:"))
MtuW= int(input("Enter The MTU(WAN) Size:"))
MtuE=int(input("Enter the MTU(Ethernet):"))
header = 20
MtuW= MtuW - header
MtuE=MtuE-header
data = data - header
iterations = data / MtuW
iterations = math.ceil(iterations)
names = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eigth']
offset = []
lst = []
sum1 = []
mf = []
list2=[]
lst = calculatemtu(iterations);
list2=calculatemtuE(lst,MtuE)
offset = calcualateoffset(list2);
sum1=calculatesumoff(offset);
mf=calculatemf(list2);
printlist(names,list2,sum1,mf);


