class FormulaError(Exception): pass
def parse_input(user_input):
  input_list = user_input.split()
  if len(input_list) != 3:
    raise FormulaError('Input does not consist of three elements')
  num1, op, num2 = input_list
  try:
    num1 = float(num1)
    num2 = float(num2)
  except ValueError:
    raise FormulaError('The first and third input value must be numbers')
  return num1, op, num2
def cal(num1, op, num2):
  if op == '+':
    return num1 + num2
  if op == '-':
    return num1 - num2
  if op == '*':
    return num1 * num2
  if op == '/':
    return num1 / num2
  raise FormulaError('{0} is not a valid operator'.format(op))


while True:
  user_input = input('>>> ')
  if user_input == 'quit':
    break
  num1, op, num2 = parse_input(user_input)
  result = cal(num1, op, num2)
  print(result)
