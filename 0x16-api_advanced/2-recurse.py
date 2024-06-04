#!/usr/bin/python3
"""
Script that returns a list containing titles of hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing titles of hot articles
    """

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])

    if not children:
        return None if not hot_list else hot_list

    for child in children:
        hot_list.append(child['data']['title'])

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
