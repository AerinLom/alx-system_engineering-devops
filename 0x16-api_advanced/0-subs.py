#!/usr/bin/python3
"""
Script that queries number of subscribers on subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on subreddit."""

    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Python Reddit Subscriber checker"}
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
