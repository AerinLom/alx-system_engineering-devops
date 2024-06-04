#!/usr/bin/python3
"""
Script that queries number of subscribers on subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on subreddit."""

    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Python Reddit Subscriber checker"}
    response = requests.get(api_url, allow_redirects=False, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subreddit_subscribers = data['data']['subscribers']
        return subreddit_subscribers
    else:
        return 0
