def add_time(start, duration, start_day=None):
  start_time = Time(start, start_day)
  time_delta = TimeDelta(duration)

  return new_time

class Time(TimeStringParserMixin, DayNameMixin):
  _mins_in_hour = 60
  _hours_in_day = 24
  _days_in_week = 7

  def __init__(self, time_string: str, start_day: str = None):
    self._parse_timestring(time_string)
    self._miltary_time_conv()
    self._handle_day_name(start_day)

  def __add__(self, other):
    if isinstance(other, TimeDelta):
      add_hours, mins_change = divmod(self._minutes + other._minutes, Time._mins_in_hour)
      add_days, add_hours2 = divmod(self._hours + other._hours, Time._hours_in_day)
      total_hours = add_hours + add_hours2

      add_days2, hours_change = divmod(total_hours, Time._hours_in_day)
      days_change = add_days + add_days2

      if self._day_name:
        day_num = (self._day_num + days_change) % Time._days_in_week
        day_name = self._get_day_code('name')[day_num]

      time_string = f''
      return TimeDelta()


class TimeDelta(TimeStringParserMixin):
  def __init__(self, delta_string, day_change=None)
    self._parse_timestring(delta_string)

  def _day_change_str(self):


class TimeStringParserMixin:
  def _parse_timestring(time_string):
    time_string = time_string.replace(' ', ':').split(':')

    if len(time_string) == 3:
      self._tod = time_string[-1]
      self._hours = self._miltary_time_conv(int(time_string[0]), self._tod)
    else:
      self._hours = int(time_string[0])
    self._minutes = int(time_string[1])
  
  def _miltary_time_conv(hours, tod):
    if tod == 'AM':
      if hours == 12:
        return 0
      else:
        return hours
    
    if tod == 'PM':
      hours += 12
      return hours

  @property
  def military_time(self):
    return f'{self._hours}:{self._minutes}'

  @property
  def normal_time(self):
    hours = f'{self._hours}'
    minutes = f'{self._minutes:02d}'
    tod = 
    return f'{hours}:{minutes} '


class DayNameMixin:
  _day_names = (None, 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
  _day_nums = tuple([None, *range(7)])

  def _handle_day_name(self, start_day):
    # ensure start day is valid
    if (start_day) & (start_day.lower() not in DayNameMixin._day_names):
      raise Exception('Not a valid day.')

    if start_day:
      self._day_name = start_day.lower()
      self._day_num = self._get_day_code('num')[self._day_name]

  def _get_day_code(code_type: str = 'num'):
    if code_type == 'num':
      return dict(zip(DayNameMixin._day_names, DayNameMixin._day_nums))
    elif code_type == 'name:
      return dict(zip(DayNameMixin._day_nums, DayNameMixin._day_names))

    

    
    

