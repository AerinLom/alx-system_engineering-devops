#!/usr/bin/python3
"""
Script that queries the titles of the first 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """
    Return the titles of the first 10 hot posts
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(None)
