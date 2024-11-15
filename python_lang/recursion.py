def sumOfArray(array):
   if array == []:
       return 0
   return array[0] + sum(array[1:])
myArr = [7,3,3,1]
print(sumOfArray(myArr))