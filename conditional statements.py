a=int(input())
if a>0:
    print("positive")
else:
    print("not negative")
print("end")


#nested conditional blocks
matches_won=int(input())
goals=int(input())
if matches_won>8:
    if goals>20:
        print("hurray")
    print("winner")

#nested condition in else block
a=2
b=3
c=1
is_a_greatest=(a>b)and(a>c)
if is_a_greatest:
    print(a)
else:
    is_b_greatest=(b>c)
    if is_b_greatest:
        print(b)
    else:
        print(c)

#absolute difference b/w 2 numbers
a=int(input())
b=int(input())
diff=a-b
print(abs(diff))

#write a program to print the digit in ones place
