#To check whether number is odd or even without using mod operator
num = int(input("Enter a number : "))
x1 = num//2
x2 = num/2

if(x1!=x2):
    print(num," is a odd number")
else:
    print(num," is a even number")
