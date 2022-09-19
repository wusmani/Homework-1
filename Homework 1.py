print('Birthday Calculator')
print('Current Day')
current_month = int(input('Month: '))
current_day = int(input('Day: '))
current_year = int(input('Year: '))
print('Real Birthday')
birthday_month = int(input('Month: '))
birthday_day = int(input('Day: '))
birthday_year = int(input('Year: '))
years = current_year - birthday_year - 1
if (birthday_month<current_month):
    years +=1
elif current_month==birthday_month:
    if (birthday_day<current_day):
        years +=1
if (current_month==birthday_month and current_day==birthday_day):
    print ('Happy Birthday')
print('Your age is ' + str(years))