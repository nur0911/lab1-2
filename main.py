print(4, 8, 15, 16, 23, 42)

print(4)
print(8)
print(15)
print(16)
print(23)
print(42)

a=int(input())
print(a)
print(a+1)
print(a+2)

a=int(input())
b=int(input())
c=int(input())
print(a+b+c)

a=int(input())
print('Volume =',a*a*a)
print('Total surface area =',a*a*6)

N=int(input())
K=int(input())
print(K//N)
print(K%N)

a=int(input())
print('The digit in the thousands position is', a//1000)
print('The number in the hundreds position is', ((a%1000)-(a%100))//100)
print('The digit in the tens position is', ((a%100)-(a%10))//10)
print('The digit in the position of units is', a%10)

a=int(input())
if a%2==0:
  print(a//2)
else:
  print((a//2)+1)

a=int(input())
if a==0:
  print("Erorr")
else:
  print("The result of << is 2")

print("Please enter the first number:")
a=int(input())
print("Please enter the second number:")
b=int(input())
print("Please choose the operation (+, -, *, /) ")
c=input()
if c=="+":
    print(a+b)
elif c=="-":
    print(a - b)
elif c=="*":
    print(a * b)
elif c=="/":
    print(a / b)