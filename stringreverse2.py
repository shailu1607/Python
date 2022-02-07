# string_reversal_using_recursion
def reverseString(String):
    if len(String) == 0:

        return String

    else:

        return reverseString(String[1:]) + String[0]


String = input("enter the string to be reversed : ")

print("String before reversing is: ", String)

print("String after reversing is: ", reverseString(String))
