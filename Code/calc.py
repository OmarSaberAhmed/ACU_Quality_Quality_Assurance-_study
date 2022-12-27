# define a function to perform the calculation
def calculate(num1, operator, num2):
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    return num1 / num2
  else:
    return 'Invalid operator'

# ask the user for input
num1 = float(input('Enter the first number: '))
operator = input('Enter an operator (+, -, *, /): ')
num2 = float(input('Enter the second number: '))

# call the calculate function and print the result
result = calculate(num1, operator, num2)
print(result)
