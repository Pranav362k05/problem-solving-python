# Input example: 2.45 pm
time = input("Enter time (e.g., 2.45 pm): ")

# Split time and period
t, period = time.split()
hour, minute = map(int, t.split("."))
#t → stores the time part ("2.45")
#period → stores "am" or "pm"
#t is just a variable name.You could have called it clock, time_part, or anything else.

# Convert to 24-hour format
if period.lower() == "pm" and hour != 12:
    hour += 12
elif period.lower() == "am" and hour == 12:
    hour = 0
#lower() converts text to lowercase.This lets the user type PM, pm, or Pm and the program still works.

# Print result
print(f"{hour:02d}.{minute:02d}")
#f is a string that inserts variable values into the string