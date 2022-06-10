# create a script that will find out current times in Portland, NYC & London
# use current time to determine if branch is open or closed
# print to screen all three branches and open/closed status

# import datetime module
import datetime
import pytz

# create a branch class
class Branch:
  # initialize branch with name and time zone (pytz string)
  def __init__(self, name, tz):
    self.name = name
    self.tz = pytz.timezone(tz)
    # set open and closing times
    self.open = datetime.time(hour=9)
    self.close = datetime.time(hour=17)

  # set local time to time zone
  def local_time(self):
    time = datetime.datetime.now()
    local_time = time.astimezone(self.tz)
    return local_time
  
  # return boolean if closed or not
  def is_closed(self):
    current_time = self.local_time()
    return (current_time.hour > self.close.hour) or (current_time.hour < self.open.hour)

  # return boolean if open or not
  def is_open(self):
    return not self.is_closed()
  
  # print branch current time and open/closed status to console
  def display_branch_status(self):
    status = 'Closed' if self.is_closed() else 'Open'
    time_str = self.local_time().strftime('%H:%M')
    print('\nBranch: {}\nCurrent Time: {}\nStatus: {}'.format(self.name, time_str, status))

if __name__ == "__main__":
  # instantiate three branches
  london = Branch('London', 'Europe/London')
  portland = Branch('Portland', 'America/Los_Angeles')
  nyc = Branch('New York City', 'America/New_York')

  # display branches to console
  london.display_branch_status()
  portland.display_branch_status()
  nyc.display_branch_status()
