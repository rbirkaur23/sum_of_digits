n=int(input("Enter a number: "))
total=0
while n!=0:
    last_digit=n%10
    total=total+last_digit
    n=n//10
print("Sum of digits of entered number: ",total)    

