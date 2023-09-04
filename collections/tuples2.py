weekdays_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekdays_tuple = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
def modify_weekdays(weekdays):
    weekdays[2] = 'Wedday' # this is going to modify the original list!
    print(weekdays)

modify_weekdays(weekdays_list)
# cannot modify tuple items
# weeekdays_tuple[2] = "Wedday"
print(weekdays_list) 
print(weekdays_tuple)

