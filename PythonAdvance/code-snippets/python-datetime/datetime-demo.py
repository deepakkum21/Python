import datetime
import pytz

# to craete a date with particular date
# AVOID TRAILING ZERO
# date(year, month=None, day=None)
print(datetime.date(2018,day=7, month=5))

# to find todys date
today = datetime.date.today()
print(today)

# weekday  mon=0, sun=6
# isoweekday mon=1, sun=7
print('weekday ',today.weekday())
print('isoweekday ',today.isoweekday())

# timedelta for adding or subtracting specific days or time  
# timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
tdelta = datetime.timedelta(days=5)
print('5 days before today: ',today - tdelta)

# two date operatio like add, subtract gives timedelta
nextbirthdate = datetime.date(2019, day=18, month=10)
till_birth = nextbirthdate - today
print(till_birth.total_seconds())


# datetime.date gives all things regarding date

# datetime.time gives all things regarding time
# time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
print('datetime.time ',datetime.time(hour=6, minute=15, second=50, microsecond=5010, tzinfo=None))

# datetime.datetime gives all things regarding both date and time
# datetime.datetime(year, month=None, day=None, hour=0, minute=0, second=0,microsecond=0, tzinfo=None)
date_time = datetime.datetime(2014, month=5, day=30, hour=12, minute=10, second=40,microsecond=1040, tzinfo=None)
print('datetime.datetime ',date_time)
print('date ', date_time.date())
print('time ', date_time.time())
print('year ', date_time.year)
print('month ', date_time.month)
print('minute ', date_time.minute)
print('day ', date_time.day)

# timedelta for adding or subtracting specific days or time  
# timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
tdelta = datetime.timedelta(hours=5)
print('5 hours before today: ',date_time - tdelta)

# here timezone is none
dt_today = datetime.datetime.today()

# here we have the option to pass timezone but if not passed timezone is none
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)

# using pytz
date_tm = datetime.datetime(2014, month=5, day=30, hour=12, minute=10, second=40, tzinfo=pytz.UTC)
print(date_tm)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print('date using now by ptz UTC ',dt_now)       # 2019-01-10 08:27:20.946783+00:00
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print('date using utcnow by ptz UTC ',dt_now)    # 2019-01-10 08:27:20.946783+00:00


# list of timezone present in pytz
# for tz in pytz.all_timezones:
#    print(tz)

# to get time of your current timezone
dt_ind_cal = dt_now.astimezone(pytz.timezone('Asia/Calcutta'))
print('India/cal ',dt_ind_cal)

print(dt_ind_cal.isoformat())

# format for datetime with tz
print(dt_ind_cal.strftime('%B %d, %Y'))

# to get current timezone aware datetime
print(datetime.datetime.now(tz=pytz.timezone('Asia/Calcutta')))

# To print the datetime from the string format
date_str = 'January 10, 2019'
da_tm = datetime.datetime.strptime(date_str, '%B %d, %Y')
print(da_tm)


# strftime -> converts datetime to string
# strptime -. converts string to datetime

# better datetime package for python https://arrow.readthedocs.io/en/latest/
