#!/usr/bin/python3
"""
This function queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """
    Function to query Reddit API and prints the titles
    of the initial 10 hot posts for the subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'advanced-api/0.0.1 by Mendy'}
    req = requests.get(url=url, headers=headers, allow_redirects=False)
    if req.status_code == 200:
        response = req.json()
        titles = [child['data']['title']
                  for child in response['data']['children'][:10]]
        for title in titles:
            print(title)
    else:
        print(None)
