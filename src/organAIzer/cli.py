import argparse
from gmail import get_messages
from gcalendar import get_cal_events


def main(list_messages, list_events):
    if list_messages:
        messages = get_messages()
        for message in messages:
            print(message)
    elif list_events:
        get_cal_events()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple CLI that lists Gmail messages.')
    parser.add_argument('--list', dest='list_messages', action='store_true', help='List Gmail messages')
    parser.add_argument("--cal", dest="list_events", action="store_true", help="List Google Calendar events")
    args = parser.parse_args()
    main(args.list_messages, args.list_events)
