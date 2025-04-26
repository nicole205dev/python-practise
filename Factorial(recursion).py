def factorial(x):
    if(x==1):
    return 1
return x * factorial(x-1)

number=int(input("Enter the number:"))

result+factorial(number)
print("Factorial of entered number{} is{}".format(number,result) )

