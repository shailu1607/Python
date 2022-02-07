def factorial(num):
    if num <= 1 :
        fact = 1
        return fact
    else:
        fact = num * factorial(num-1)
        return fact

num = int(input("Enter the number : "))
print("The factorial of",num,"is",factorial(num))