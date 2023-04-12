month=int(input("Enter the month in the numeric form:"))
day=int(input("Enter the day in numeric form:"))
year=int(input("Enter the year as two numerical digits:"))
r=1
if (day>0 and day<=31):
    r=1
else:
     r=0
     print("invalid day")
if (month>0 and month<=12):
  r=1
else:
     r=0
     print("invalid month")
if (year>0 and year<=99):
  r=1
else:
    r=0
    print("invalid year")
if(r==1):
    print("correct")
    print("Date:",day,"/", month,"/",year)
else:
    print("Success: Congratulations! you entered the correct date")