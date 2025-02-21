#Return the year and name of weekday
import datetime
x=datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
print(x.strftime("%d"))
print(x.strftime("%B"))

#%A:Full weekday name (e.g., 'Wednesday')
#%B: Full month name (e.g., "january'')
#%d:Day of the month as a zero -padded decimal number (e.g., "01",to"31")
#%Y: Year with centuary as a decimal number (e.g., "2024")

