#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'


def retrieve_events(url):
    """Retrieve GitHub events from the given URL."""
    data = requests.get(url).text
    events = json.loads(data)
    return events


def print_events(events, n=5):
    """Print the first n GitHub events."""
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)


def main():
    """Retrieve and print recent GitHub events for the user."""
    print(GHUSER)
    print(url)
    events = retrieve_events(url)
    print_events(events)


if __name__ == "__main__":
    main()

