from O365 import Account

CLIENT_ID = "xxx"
CLIENT_SECRET = "xxx"

credentials = (CLIENT_ID, CLIENT_SECRET)
scopes = ['Calendars.Read']
account = Account(credentials)

if not account.is_authenticated:
    account.authenticate(scopes=scopes)
    print('Authenticated!')

schedule = account.schedule()
calendar = schedule.get_default_calendar()
events = calendar.get_events(include_recurring=False)

for event in events:
    print(event)
