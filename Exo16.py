numbers = [1, 2, 3, 4, 5]
index = int(input("Enter index (-1 to quit): "))
while index != -1 :
   if index > 4 :
      print("Error")
      break 
   value = int (input("Enter new value: "))
   numbers[index] = value 
   print(numbers)
   index = int(input("Enter index (-1 to quit): "))