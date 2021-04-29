# Finding The Recursion of 15
def fact(number_1):
    if number_1 == 1 or number_1 == 0:
        return 1
    else:
        return number_1 * (fact(number_1 - 1))
# this calls the function because
# it is not in the function itself
print(fact(15))
