#python 3.7.1
print(''' ________________
|  pandas lite   |
 ————————————————''')
Index = [] #empty list Index
s1 = [] #empty list s1
n = int(input("number of data:"))
for i in range(1,n+1):
    a = input("element: ")
    s1.append(a)
for i in range(1,n+1):
    a = input("Index: ")
    Index.append(a)
print (s1,Index)
a = 0
for i in range(1,n+1):
    print (Index[a],s1[a],end = '\n')
    a = a + 1

print ('dtype: object')
