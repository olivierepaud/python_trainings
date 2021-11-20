# imports
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

#
# functions definition
#
def main():
    #using date
    today = date.today()
    print("\n----------------") 
    print("Today's date is", today)
    print("Date components:", "day:"+str(today.day), ", month:"+str(today.month), ", year:"+str(today.year)) 
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturay","Sunday"]
    print("Today's weekday # is", today.weekday(), "which is a", days[today.weekday()]) 

    #using datetime
    print("\n----------------") 
    now = datetime.now()
    print("The current date and time is:", now)
    t = datetime.time(now)
    print("The current time is:", t)

    #date formating
    # %y/%Y year, %a/%A weekday, %b/%B month, %d day of month
    # %c locale's date and time, %x locale's date, %X locale's time
    print("\n----------------") 
    print(now.strftime("The current year is %y (%Y)"))
    print(now.strftime("The current month is %b (%B)"))
    print(now.strftime("The current day is %d"))
    print(now.strftime("The current date is: %A, %B %dth, %Y"))
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))

    #time formating
    # %I/%H 12/24 hour, %M minutes, %S seconds, %p locale's AM/PM
    print(now.strftime("The current time is %H:%M:%S or %I:%M:%S %p"))

    #using timedelta
    print("\n----------------") 
    print(timedelta(days=365, hours=5, minutes=1))
    print("one year from now it will be: " + str(now + timedelta(days=365)))
    print("in 3 weeks and 2 days it will be: " + str(now + timedelta(weeks=3, days=2)))
    t = datetime.now() - timedelta(weeks=2)
    s = t.strftime("%A %B %d, %Y")
    print("Two weeks ago it was:",s)

    # How many days until April Fool's Day ? 
    print("\n----------------") 
    today = date.today()
    afd = date(today.year, 4, 1)
    if afd < today:
        print("April Fool's day already went by %d days ago" % (today-afd).days)
        afd = afd.replace(year = today.year+1)
    time_to_afd = afd-today
    print("It's just", time_to_afd.days, "days until next April Fool's Day")


    # How many days until I leave to Paris ?
    print("\n----------------") 
    leaving_day = date(2021,12,23)
    if (today < leaving_day):
        print("I will leave to Paris in %d days" % (leaving_day-today).days)
    elif (today == leaving_day):
        print("I'm leaving to Paris today")
    else:
        print("I left for Paris %d days ago" % (today-leaving_day).days)





#
# execution
#
if __name__ == "__main__":
    main()

