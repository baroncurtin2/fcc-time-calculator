def add_time(start, duration, start_day=None):
  start_hours, start_mins = start.split(':')
  start_mins, start_tod = start_mins.split(' ')
  duration_hours, duration_mins = duration.split(':')

  # calculate days later
  days_later = int(duration_hours) // 24

  # augment hours
  new_hours, passed_time = time_augment(start_hours, duration_hours, 12)
  new_mins, _ = time_augment(start_mins, duration_mins, 60)
  new_tod = 'PM' if (start_tod == 'AM') & (passed_time) else 'AM'

  new_time = f'{new_hours}:{new_mins:02d} {new_tod}'

  # if the new time is days later
  if days_later > 0:
    suffix = days_later_switch(days_later)
    return f'{new_time} {suffix}'

  return new_time

def days_later_switch(days_later):
  switcher = {
    0: lambda: '',
    1: lambda: '(next day)'
  }

  def default():
    return f'({days_later} days later)'

  return switcher.get(days_later, default)()

def time_augment(start, duration, time_cap):
  start = int(start)
  duration = int(duration)
  passed_time_cap = False

  for _ in range(0, duration + 1):
    start += 1

    if start > time_cap:
      start = 1 if time_cap == 12 else 0
      passed_time_cap = True
  return start, passed_time_cap