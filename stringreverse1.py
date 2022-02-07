#string_reversal_using_slicing
def reverseString(input):

   input1 = input[::-1]

   return input1

input = input("String to be reversed : ")

print("String before reversal is: ", input)

print("String after reversal is: ", reverseString(input))