import datetime

dateNow = datetime.datetime.now()
# print(dateNow)
# print(dateNow.year)
# print(dateNow.month)
# print(dateNow.strftime("%a"))

'''
%a	Weekday, short version
%A	Weekday, full version
%w	Weekday as a number 0-6, 0 is Sunday
%d	Day of month 01-31
%b	Month name, short version
%B	Month name, full version
%m	Month as a number 01-12
%y	Year, short version, without century
%Y	Year, full version
%H	Hour 00-23
%I	Hour 00-12
%p	AM/PM
%M	Minute 00-59
%S	Second 00-59
%f	Microsecond 000000-999999
%z	UTC offset
%Z	Timezone
%j	Day number of year 001-366
%U	Week number of year, Sunday as the first day of week, 00-53
%W	Week number of year, Monday as the first day of week, 00-53
%c	Local version of date and time - e.g. Mon Dec 31 17:41:00 2018
%C	Century
%x	Local version of date - e.g. 12/31/18
%X	Local version of time - e.g. 17:41:00
%%	A % character
%G	ISO 8601 year
%u	ISO 8601 weekday (1-7)
%V	ISO 8601 weeknumber (01-53)
'''

createDate = datetime.datetime(2019, 5, 20, 12, 12, 12, 123456)
#print(createDate)
