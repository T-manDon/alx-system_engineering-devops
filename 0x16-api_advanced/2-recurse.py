#!/usr/bin/python3
"""
This function queries Reddit API
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Ths function will quesry Reddit API and list all the
    the titles of hot articles for the subreddit.
    Args:
        subreddit (str): name of a subreddit
    Return:
        titles (list): a list of hot subreddit titles
        None: if subreddit is not valid
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after, 'limit': 100}
    headers = {'User-Agent': 'advanced-api/0.0.1 by Mendy'}
    req = requests.get(url, params=params,
                       headers=headers, allow_redirects=False)
    if req.status_code == 200:
        response = req.json()
        hot_list = [child['data']['title']
                    for child in response['data']['children']]
        after = response['data']['after']
        if after is not None:
            hot_list += recurse(subreddit, after=after)
        return hot_list
    return None
