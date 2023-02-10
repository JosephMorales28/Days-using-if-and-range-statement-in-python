input1=int(input("Enter number of day:\n"))

day=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

if input1 in range(0,8):
   if input1 == 1:
      print(day[0])
     
   elif input1 ==2:
      print(day[1])
      
   elif input1 == 3:
      print(day[2])
      
   elif input1 == 4:
      print(day[3])
      
   elif input1 == 5:
      print(day[4])
      
   elif input1 == 6:
      print(day[5])
      
   elif input1 == 7:
      print(day[6])
      
else:
    print("invalid")