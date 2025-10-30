# https://docs.python.org/3/library/datetime.html#format-codes

from datetime import datetime, timedelta

now = datetime.now()

print(f"The time now is {now.hour}:{now.minute}")

print(f"The current year is {now.year}")

# default format (no format specified)
print(f'{now}')

# Friendly format
print(f'{now:%B %d, %Y, %H:%M}')

# ISO 8601 date-only format
print(f'{now:%Y-%m-%d}')

# 12-hour clock
print(f'{now:%I:%M %p}')

print(f"Today is {now:%d/%m/%Y} and the time is {now:%H:%M}")

# subtract 2 hours from now
date = now - timedelta(hours = 48)

# find the difference between the two datetime objects
delta = now - date
seconds = delta.total_seconds()



print(f'{date:%B %d, %Y, %H:%M:%S}')
print(f'Difference of {seconds} seconds')


# adding a timedelta to a timedelta
print(delta + delta)

# adding a datetime to a datetime
print(now + now)

# adding a datetime to a timedelta
print(now + delta)