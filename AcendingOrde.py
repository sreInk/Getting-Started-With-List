lst = [1,2,3,421,43,653,34,12]
print("Orginal List: ",lst)\

count = 0

for i in lst:
    count += i

avg = count/len(lst)

print("The Total Sum is : ",count)
print("The Total Average is : ",avg)

lst.sort()

print("The smallest number is: ", lst[0])
print("The largest number is: ", lst[-1])