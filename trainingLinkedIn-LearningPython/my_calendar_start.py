#
# imports
#
import calendar



#
# classes definition
#


#
# functions definition
#
def main():
    c = calendar.TextCalendar(calendar.MONDAY)
    st = c.formatmonth(2021, 11, 0, 0)
    print(st)

    ch = calendar.HTMLCalendar(calendar.MONDAY)
    st2 = ch.formatmonth(2021, 11)
    print(st2)

    for i in c.itermonthdays(2021,11):
        print(i)

    for month in calendar.month_name:
        print(month)

    for day in calendar.day_name:
        print(day)

    print("team meetings will be on the first Friday of every month: ")
    for m in range(1,13):
        cal = calendar.monthcalendar(2021, m)
        weekone = cal[0]
        weekone = cal[1]

        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY]
        else:
            meetday = weektwo[calendar.FRIDAY]

        print("%10s %2d" % (calendar.month_name[m], meetday))


#
# execution
#
if __name__ == "__main__":
    main()


