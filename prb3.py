salary=float(input("Please enter your salary in Germany: "))
country=input("Enter the country you want to migrate to: ")

def convertsalary(country,salary):
  if(country=="ca"):
    final_salary=salary*1.55
    if(final_salary >64000):
     print("you will be rich in canada with the salary" 
  ,final_salary, " cad")
    else:
     print("you will be poor in canadawith the salary of" ,final_salary, " cad")
    
  elif(country=="us"):
    final_salary=salary * 2.5
    if(final_salary >56,516  and country=="us"):
      print("you will be rich in us with the salary of" ,final_salary, " us dollar")
    else:
      print("you will be poor in us with the salary of" ,final_salary, " us dollar")
 
  elif(country=="cm"):
    final_salary=salary*4555
    if(final_salary > 5,649,856 and country=="cm"):
      print("you will be rich in cm with the salary of" ,final_salary, " Riel")
    else:
      print("you will be poor in cm with the salary of" ,final_salary, " Riel")

     
  elif(country=="uk"):
    final_salary=salary*1.2
    if(final_salary >35,423 and country=="uk"):
      print("you will be rich in uk with the salary of" ,final_salary, " pounds")
    else:
     print("you will be poor in  uk with the salary of" ,final_salary, " pounds")
  else:
    print("invalid salary")
    
convertsalary(country,salary)
  
    
    
  
  





