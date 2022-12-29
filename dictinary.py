#Dictionary-unordered collection of items.It has key-value pair
dic_a={
    "name": "Teja",
     "age": 15
}

#Keys are immutable

dic_a={
    "name": "Teja",
     "age": 15,
     "ro_no": 15
}
print(dic_a['name'])

#member check
dic_a={
    "name": 'USHA',
    "age":   28
}
result="name" in dic_a
print(result)

#OPERATIONS ON DICTIONARY
#ADD KEY VALUE PAIR
dic_a={"name":"Usha","age":21}
dic_a['city']="guntur"
dic_a['country']="india"
print(dic_a)
#updation age
dic_a['age']=24
print(dic_a)
#delete age
del dic_a['age']
print(dic_a)

#dict.keys # dic.values #dic.items
dic_a={
    "name": "Teja",
     "age": 15
}
print(dic_a.keys())
print(dic_a.values())
print(dic_a.items())

#loop over dictionary
dic_a={
    "name": "Teja",
     "age": 15
}
for key in dic_a.keys():
    print(dic_a[key])
    print(key)


dic_a={
    "name": "Teja",
     "age": 15
}
for value in dic_a.values():
    print(value)

dic_a={
    'name':'Teja',
     'age':22
}
for key,values in dic_a.items():
    pair="{} {}".format(key,value)
    print(pair)

#converting list to dict

list_a=[
    ('name','teja'),
    ('age',15),
    ('roll_no',15)
]
dic_b=dict(list_a)
print(dic_b)

#dict key must be of type immutable
#Referring same dictionary object

dic_c={
    'name':'usha',
    'age':22
}
dic_d=dic_c
dic_d['age']=18
print(dic_d)
print(dic_c)
print(id(dic_d))
print(id(dic_c))


#create a copy of a dictionary

dic_c={
    'name':'usha',
    'age':22
}
dic_d=dic_c.copy()
dic_d['age']=18
print(dic_d)
print(dic_c)
print(id(dic_d))
print(id(dic_c))

#list copy
list_a=['Teja',15]
list_b=list_a.copy()
list_b.extend([20])
print(list_a)
print(list_b)
print(id(list_a))
print(id(list_b))


#membership of dic and clear a dict
dic_c={
    'name':'usha',
    'age':22
}
print(len(dic_c))
if 'name' in dic_c:
    print('true')
dic_c.clear()
print(dic_c)


#cannot add/remove dict keys while iterating the dictionary
dic_a={'name':'teja','age':15}
for k in dic_a.keys():
    if k=='name':
        del dic_a[k]
print(dic_a)

#problems
#update a value of paticular key
dic_a={
    'name':'usha',
     'age':21,
      'id':201
}
print("Before Updating:",dic_a)
dic_a['id']=204
print("After Updating:",dic_a)

#remove a key
dic_a={
    'name':'usha',
     'age':21,
      'id':201
}
print("The keys and values are:",dic_a )
del dic_a['age']
print("After removing:",dic_a)

#write a program that contains keys an numbers from 1 to M and values are squares of keys
d=dict()
for x in range(1,10):
    d[x]=x*2
print(d)

#Determine number of rotations.python,onpyth-Cloud udclo
l_a=input()
l1=list(l_a)
n=int(input())
for i in range(n):
    t=l1[-1]
    l1.remove(t)
    l1.insert(0,t)
    print(l1)

#read 2 numbers m and n print all the perfect squares between M and N


#given M*N matrix write a program to print the matrix after  ordering all the elements of the matrix in increasing order.

M=int(input())
N=int(input())
mat=[]
for i in range(M):
    row=input().split()
    for j in row:
        mat.append(j)
list_a=mat.sort()
print(mat)
k=0
for i in range(M):
    for j in range(N):
        print(mat[k],end='')
        k=k+1
    print()

#write a program to return the sum and average of digits of all numbers that appear in the string
