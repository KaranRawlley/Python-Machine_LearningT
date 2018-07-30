import calendar

yy = input('Enter the year want to display calendar of ')
yy = int(yy)
mm = input('Enter the month number ')
mm = int(mm)
print('\n')



print(calendar.month(yy, mm))