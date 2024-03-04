import argparse
from gmail import get_messages


def main(list_messages):
    if list_messages:
        messages = get_messages()
        for message in messages:
            print(message)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple CLI that lists Gmail messages.')
    parser.add_argument('--list', dest='list_messages', action='store_true', help='List Gmail messages')
    args = parser.parse_args()
    main(args.list_messages)
