sum =0

def add(num1,num2):
    global sum
    sum = num1 +num2
    print("install sum method sum =", sum)
    return sum

new_sum =add(1,2)

print("Outside method, newsum= ", new_sum)
print("Onside method, sum= ",sum)