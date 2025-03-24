num1 = int(input("Number1: "))
num2 = int(input("Number2: "))
operator = input(
    "Enter Mathematical operation(addition, subtraction, multiplication, or division):").strip().lower()
if operator == "addition":
   Result = num1+num2
   print(f"{num1}+{num2} = {Result}")
elif operator == "subtraction":
   Result= num1-num2
   print(f"{num1}-{num2} = {Result}")
elif operator == "multiplication":
   Result = num1*num2
   print(f"{num1}x{num2} = {Result}")
elif num1 == 0 and operator == "division":
   Result = num2/num1
   print("Any number is not divisible by zero")
elif num1 != 0 and operator == "division":
   Result = num2/num1
   print(f"{num1}/{num2} = {Result}")
else:
   print("Please enter the operator in a word")
