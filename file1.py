#def div(self):
try:
    x=int(input("Enter a nuber"))
    y=int(input("enter the nuber"))
    c=x/y
#divible by zero error
except ZeroDivisionError as e:
    print("exception occured",e)
#value error
except ValueError as e:
    print("invalid input")

finally:
    print("hello")
print("bye")
