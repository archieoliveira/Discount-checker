#this code is made to manage the employee's data in a enterprise

employee_list = [] #creating an empty list to receive the dictionary's data
id_global = 0 #iterative variable for the employee's id

def register_employee(id): #function to register an employee
  name = input('Enter your name: ')
  department = input('Enter the department you work: ')
  wage = float(input('Enter your wage: '))
  print()
  employee =     {'ID'        : id_global, #defining each key/value
                 'Name'      : name,
                 'Department'     : department,
                 'Wage' : wage}
  employee_list.append(employee.copy()) #creating a dictionary copy and adding to the empty list
  print("Employee succesfully registered!")

def consult_employee(): #function to consult the employees
  while True:
    secondary_option = input('\nYou chose the option "Consult employee", now chose the method \n'+ #para o usuario dar entrada em qual forma de consulta ele deseja
                              '  1 - Consult all \n' + #vai mostrar todos os colaboradores cadastrados
                              '  2 - Consult by ID \n' + #vai mostrar o colaborador de acordo com o id que sera inserido logo após
                              '  3 - Consult by department \n'+ #vai mostrar o colaborador pelo setor que foi inserido referente a ele no cadastro
                              '  4 - Return to menu \n')
    if secondary_option == '1':
      print('You chose the option "Consult all" \n')
      for employee in employee_list: #loop to go through all the dictionaries in list
        print()
        for key, value in employee.items(): #loop to go through each key/value in the dictionary
          print(f'{key} : {value}') #on each key/value it goes, it will print on the screen
      print()
    elif secondary_option == '2':
      wanted_id = int(input('You chose the option "Consult by ID", now enter the ID: \n'))
      for employee in employee_list:
        if employee['ID'] == wanted_id: #after go through all the dictionaries, it compares the id entered by the user with the one in list and if its equal, goes to condition
          for key, value in employee.items(): #prints every key/value where the id matches with the input
            print('{} : {}'.format(key, value))
      print()
    elif secondary_option == '3':
      wanted_department = input('You chose the option "Consult by department", now enter the department: \n')
      for employee in employee_list:
        if employee['Department'] == wanted_department: #goes through each key/value and searches for the department that matches with the input, if it does, continues the condition
          for key, value in employee.items(): #prints all key/values in the right dictionary
            print(f'{key} : {value}')
        print()
    elif secondary_option == '4':
      print('\nYou chose to return to the main menu')
      break #breaks this loop if the user wants to return to the main menu, and goes to the main loop
    else:
      print('Opção inválida, tente novamente') #in case the user enters an invalid option, returns to this loop


def remove_employee(): #function to define removing employee
  print()
  print('You chose to remove an mployee\n')
  wanted_id = int(input('Enter the ID you want to remove: '))
  for employee in employee_list:
      if employee['ID'] == wanted_id: #identifies the employee with a id that matches the input
        employee_list.remove(employee) #after identifying, removes the employee 
        print('You succesfully removed this employee') #just a message to communicate that the removing was succesfull

print('----------- WELCOME! -----------')

while True:
  main_option = input('\n Select an option: \n' + #menu de opções principal
                          '1 - Register employee \n' +
                          '2 - Consult employee \n' +
                            '  1 - Consult all \n' +
                            '  2 - Consult by ID \n' +
                            '  3 - Consult by department \n' +
                            '  4 - Return to the main menu \n' +
                          '3 - Remove employee \n' +
                          '4 - End application \n' +
                          '>>  ')
  if main_option == '1':
    print(f"\nEmployee's ID is  {id_global}")
    register_employee(id_global) #if the user chooses register, calls this function
    id_global += 1 #for each employee registered, increases 1 in the id global value
  elif main_option == '2':
    consult_employee() #calls the function consult employee
  elif main_option == '3':
    id_global -= 1 #when an employee is removed, id is subtracted
    remove_employee() #calls the function remove employee
  elif main_option == '4':
    print('Ending application...')
    break #ends the application if the user wants to
  else:
    print('Invalid option, try again!')
    continue #if the user enters an invalid option, it goes back to the main loop