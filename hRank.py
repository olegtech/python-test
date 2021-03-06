

# -------------------------------------

# List Comprehension
x=1
y=1
z=2
n=3

print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ])


# -------------------------------------

L,L4 = [], []
for i in range(int(input())):
    name = input()
    score = float(input())
    L.append([name, score])

L2 = sorted(list(set([m for name, m in L])))[1]

for i in range(len(L)):
    if L2 == (L[i][1]):
        L4.append(L[i][0])

L4.sort()

for i in L4:
    print(i)

# comments  
marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))


# -------------------------------------


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores


    query_name = input()
    print( format( (sum(student_marks[query_name]) / 3 ), ".2f" ) )


# -------------------------------------


L = []
for i in range(int(input())):
    j = input().split()
    if j[0] == 'insert':
        L.insert(int(j[1]), int(j[2]))
    if j[0] == 'print':
        print(L)
    elif j[0] == 'remove':
        L.remove(int(j[1]))
    elif j[0] == 'append':
        L.append(int(j[1]))
    elif j[0] == 'sort':
        L.sort()
    elif j[0] == 'pop':
        L.pop()
    elif j[0] == 'reverse':
        L.reverse()

#coments:
n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print l

eval('arr.{0}{1}'.format(cmd,tuple(map(int,arg))))

#instead of 

cmd += "("+ ",".join(args) +")"
    eval("l."+cmd)
            #and  It works

# -------------------------------------


if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))

# comment
raw_input()
print hash(tuple(map(int, raw_input().strip().split(" "))))


print raw_input() == 0 or hash(tuple(map(int, raw_input().split(' '))))

# -------------------------------------


first_name = input()
last_name = input()
print(f"Hello {first_name} {last_name}! You just delved into python.")

# -------------------------------------

# Mutations

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# -------------------------------------    

# String Validators

if __name__ == '__main__':
    s = input()
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))


# -------------------------------------

# String Formatting:

def print_formatted(number):
    width = len("{0:b}".format(n))
    for i in range(1, n+1):
        print ("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# -------------------------------------


# collections.Counter()


import collections

numShoes = int(raw_input())
shoes = collections.Counter(map(int, raw_input().split()))
numCust = int(raw_input())

income = 0

for i in range(numCust):
    size, price = map(int, raw_input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print income

# -------------------------------------

from collections import Counter
n = int(input())
s = Counter(map(int,input().split()))
x = int(input())
total = []
for i in range(x):
    a,b = map(int,input().split())
    if s[a] > 0:
        total.append(b)
        s.subtract(Counter([a]))
    else:
        pass

print (sum(total))



# -------------------------------------


from collections import Counter

numShoes = int(input())
shoes = Counter(map(int,input().split()))
numCust = int(input())

total = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]: 
        total += price
        shoes[size] -= 1

print (total)

# comment
from collections import Counter
n = int(input())
s = Counter(map(int,input().split()))
x = int(input())
total = []
for i in range(x):
    a,b = map(int,input().split())
    if s[a] > 0:
        total.append(b)
        s.subtract(Counter([a]))
    else:
        pass

print (sum(total))

###
import collections

numShoes = int(raw_input())
shoes = collections.Counter(map(int, raw_input().split()))
numCust = int(raw_input())

income = 0

for i in range(numCust):
    size, price = map(int, raw_input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print income
# in Python 0 == False, so if shoes[size] is 0 this will evaluate to False otherwise it will be True.


# -------------------------------------
# -------------------------------------

#Alphabet Rangoli

import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))



def print_rangoli(size):
    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    
    for i in range(size-1, -size, -1):
        x = abs(i)
        if x >= 0:
            line = myStr[size:x:-1]+myStr[x:size]
            print ("--"*x+ '-'.join(line)+"--"*x)


# -------------------------------------

# Text Alignment

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# -------------------------------------

    