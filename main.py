#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#In order to get the tip divide the tip by 100

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#Set your input statements to the data type which best converts the response given.
bill = float(input('How much is the bill? '))
people = int(input('How many people are in your group? '))
tip = float(input('What percenatge of a tip a is the group leaving? '))

#Use the mathematical formula too find the total including the tip each party member should pay.
total = ((((tip / 100) * bill) + bill) / people)

#Print the total rounded two decimal places using the ('{:.2f}'.format) will still give the two decimal places but this will also display the 2 decimal places including the 0.
total = "{:.2f}".format(total)
print(total)