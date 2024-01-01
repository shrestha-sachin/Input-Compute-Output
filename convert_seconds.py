seconds = int(input("Enter a number of seconds and I'll tell you the equivalent whole years, days, hours, minutes, and seconds: "))

years = seconds//(365*24*60*60)    #31536000
remaining_years = seconds%31536000
days = remaining_years//86400
remaining_days = seconds%86400
hours = remaining_days//3600
remaining_hours = seconds%3600
minutes = remaining_hours//60
remaining_minutes = seconds%60
seconds = seconds%60

print(f"{years} years")
print(f"{days} days")
print(f"{hours} hours")
print(f"{minutes} minutes")
print(f"{seconds} seconds")
