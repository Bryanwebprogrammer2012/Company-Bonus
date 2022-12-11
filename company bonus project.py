print("COMPANY BONUS")

salary = int(input("\nEnter your salary: "))
years = int(input("\nEnter the years worked for the company: "))



if years>10:
    bonus = (0.12*salary)
    print("Your Bonus is " , bonus )
elif years>=6 and years<=10:
    bonus = (0.10*salary)
    print("Your Bonus is " , bonus )
elif years<6:
    bonus = (0.08*salary)
    print("Your Bonus is " , bonus )
