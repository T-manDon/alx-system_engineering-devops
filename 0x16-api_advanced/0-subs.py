#!/usr/bin/python3
"""Function queries Reddit API
"""
import requests

def number_of_subscribers(subreddit):
    """
    The funtion will query Reddit API and list number of
    subscribers for the given subreddit
    """
    subscribers = 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'advanced-api/0.0.1 by Mendy'}
    req = requests.get(url=url, headers=headers, allow_redirects=False)
    if req.status_code == 200:
        response = req.json()
        subscribers = response['data']['subscribers']
    return subscribers
