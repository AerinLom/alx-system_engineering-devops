#!/usr/bin/python3
"""
Script that queries the titles of the first 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """
    Return the titles of the first 10 hot posts
    """
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Python Reddit Top Posts checker"}
    params = {"limit": 10}
    response = requests.get(api_url, allow_redirects=False,
                            headers=headers, params=params)
    if response.status_code == 404:
        print("None")
        return
    output = response.json().get("data")
    [print(c.get("data").get("title")) for c in output.get("children")]
