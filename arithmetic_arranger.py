def arithmetic_arranger(problems, solve = False):
  first = ''
  operator = ''
  third = ''
  lines = ''
  string = ''
  arranged_problems = []
  
  for problem in problems:
    if len(problems) > 5:
      return "Error: Too many problems."
      break

    problem1 = problem.split()

    
    if (operator == '*' or operator == '/'):
      print("Error: Operator must be '+' or '-'.")
  
    first = problem1[0]
    operator = problem1[1]
    third = problem1[2]

    if not first.isdigit():
      return "Error: Numbers must only contain digits."
    elif not third.isdigit():
      return "Error: Numbers must only contain digits."
    else:
      print("There are digits")


    if len(problem1[0]) > 4 or len(problem1[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
      break

    if (len(problem1[0])+2 > len(problem1[2])+2):
      sizew = len(problem1[0])+2
    else:
      sizew = len(problem1[0])+2

      
    if(operator == "+"):
      soma = str(int(first) + int(third))
    elif(operator == "-"):
      soma = str(int(first) - int(third))

    
    
    
    head = str(first.rjust(sizew))
    tummy = f"{operator}".rjust(sizew - 1)
    lines = ""*sizew

    


    return arranged_problems