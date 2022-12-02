
def mors(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        #if product is too high, calculate the sum
        return num1 + num2

result = mors(30,10)
print("The result is ", result)

result = mors(30,50)
print("The result is ", result)
