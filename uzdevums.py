"""
#Exercise 1
def numberCombiner(n1, n2):
    if n1 * n2 <= 1000:
        result = n1 * n2
    else :
        result = n1 + n2
    return result

number1 = 40
number2 = 30

print(numberCombiner(number1, number2))



#Exercise 2
PN = 0

for CN in range(10):
    total = PN + CN 
    print("Current Number", CN, "Previous Number", PN, "Sum:", total)
    PN = CN



#Exercise 3
str = "pynative"
length = len(str)

for i in range(0, length, 2):
    print(str[i])



#Exercise 4??????????????????
def remove(string, i):

    
x = "abcdef"
print(remove(x, 3))


   
#Exercise 5
number_x = [10, 20, 30, 40, 10]
number_y = [75, 65, 35, 75, 30]

def firstAndLast(i):
    if i[0] == i[-1]:
        return True
    else:
        return False

print(firstAndLast(number_y))



#Exercise 6
list = [10, 20, 33, 46, 55]
for i in range(len(list)):
    if list[i]/5 % 1 == 0:
        print(list[i])



#Exercise 8
for i in range(6):
    print((str(i)+" ")*i)


#Exercise 9
x = 121
y = 125

def checkIfPalindrome(n):
    if str(n) [::-1] == str(n):
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")

checkIfPalindrome(x)



#Exercise 10
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
resultList = []


for i in range(len(list1)):
    if list1[i]/2 % 1 != 0:
        resultList.append(list1[i])
for e in range(len(list2)):
    if list2[e]/2 % 1 == 0:
        resultList.append(list2[e])            


print(resultList)

"""

#Exercise 14???????????????
for i in range(6):
    print("* "*i)

    
    
