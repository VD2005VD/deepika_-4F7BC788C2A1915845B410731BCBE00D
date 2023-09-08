def Check_Leap(Year):
if((year%400==0)or
   (year%100!=0)and
   (year%4==0)):
print("Given year is a leap year");
else:
print("Given year is not a leap year");
Year=int(input("Enter the number:"))
Check_leap(Year)