import datetime

my_time = 'Jan/15/23 12 hours, 05 mins, 33 secs'
python_time = datetime.datetime.strptime(my_time, '%b/%d/%y %H hours, %M mins, %S secs')
print(python_time)
human_date = python_time.strftime('%B')
print(human_date)
new_date = python_time.strftime('%d.%m.%Y, %H:%M ')
print(new_date)
