import pytz
import datetime

from django.utils import timezone

from djbook.settings import TIME_ZONE

# data = []
# tz = pytz.timezone(timezone.get_current_timezone_name())
# today = tz.localize(datetime.today())
# start = today.replace(hour=data['start_time'].hour, minute=data['start_time'].minute, second=0, microsecond=0)
# end = today.replace(hour=data['end_time'].hour, minute=data['end_time'].minute, second=0, microsecond=0)
# data['start_time'] = start.astimezone(pytz.utc).time()
# data['end_time'] = end.astimezone(pytz.utc).time()



import Skype4Py

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Connect the Skype object to the Skype client.
skype.Attach()

# Obtain some information from the client and print it out.
print 'Your full name:', skype.CurrentUser.FullName
print 'Your contacts:'
for user in skype.Friends:
    print '    ', user.FullName