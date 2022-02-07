#string_reversal_using_reversed()_functon

def reverseString(inst):
    rev = "".join(reversed(inst))

    return rev


inst = input("String to be reversed : ")

print("String before reversal is: ", inst)

print("String after reversal is: ", reverseString(inst))
