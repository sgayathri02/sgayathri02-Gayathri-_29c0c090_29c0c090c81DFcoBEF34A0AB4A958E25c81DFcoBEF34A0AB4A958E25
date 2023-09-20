#Leap year

def isLeapyear(year):
 if year%4 == 0 and year%100 != 0 or year    %400 == 0: 
  return True
 else:
  return False

year=2012

if isLeapyear(year):
   print("{} is  a  Leap  year.". format(year))
else:
   print("{}us a not Leap year.".format(year))  