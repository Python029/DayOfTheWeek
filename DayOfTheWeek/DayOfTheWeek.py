import math
import time

day = []
weekday = ["Sunday", "Monday", "Tuesday","Wednesday", "Thursay", "Friday","Saturday"]
#Day in Month
k=0
#Month
m=0
#Century(First 2 digits of Year - Ex. 19 in 1971)
C=0
#Year (Last two digits of Year)
Y=0
#Day of the Week
W=0
date = input("Please input a date in MM/DD/YYYY format:\n") 
#While Loops to ensure correct format
while True:
    while(len(date)!=10):
        date = input("\nDate must be 8 digits. Slashes must be included. Please input a date in MM/DD/YYYY format:\n")
    #Only checks other 2 conditions once length with slashes is 10
    if(date.__contains__("/")==False):
        date = input("\nDate must be 8 digits. Slashes must be included. Please input a date in MM/DD/YYYY format:\n")
        continue
    elif(date.__contains__("/") and date.count("/")!=2):
        date = input("\nDate must be 8 digits. Slashes must be included. Do not use more or less than 2 slashes.\nPlease input a date in MM/DD/YYYY format:\n")
        continue
    break
#Seperate Date by slashes    
day = date.split("/")
#Seperate date into variables
m = int(day[0])
k = int(day[1])
#Find the Century by dividing by 100
C = math.floor(int(day[2])/100)
#Find the year by taking the mod of 100. Year is what's left over.
Y = int(day[2])%100
#March is month 1 in formula, so input must be adjusted to account for this
if(m == 1 or m == 2):
    m=m+10
    if(Y==0):
        Y=99
        C=C-1
    else:
        Y=Y-1
elif(m>=3 and m<=12):
    m=m-2
if(m<1 or m>12 or k < 1 or k > 31):
    print("Invalid Values Detected.")
    time.sleep(2)
    print("Terminating Program Execution.")
    time.sleep(2)
    quit()

#Formula given in assignment
W = int(k + math.floor(2.6*m - 0.2) - 2*C + Y + math.floor(Y/4.0) + math.floor(C/4.0)) % 7

print(f"Day of the Week: {weekday[W]}")