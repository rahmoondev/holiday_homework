#​5. Christmas Countdown Timer 
#​Goal: Write a script that calculates and prints how many days, hours, and minutes are left until a specific date (e.g., New Year's Day or next Christmas).
# ​Concepts: Using the datetime module.
# ​🔐 Text and String Manipulation (Relevant to Encoding/Decoding)
# These problems focus on manipulating text, a key skill in cryptography and log analysis.

from datetime import datetime

def new_years_coundown():
    now= datetime.now()
    current_year = now.year
    new_years_date = datetime(current_year+1,1,1)
    time_difference = new_years_date - now
    days = time_difference.days
    hours= time_difference.seconds //3600
    minutes= time_difference.seconds %3600 //60
    print(f"Time left until New Year's Day is: {days} days, {hours} hours, and {minutes} minutes.")


if __name__=="__main__":
    new_years_coundown()