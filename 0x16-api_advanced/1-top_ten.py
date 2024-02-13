#!/usr/bin/python3
'''contains a function that queries the Reddit API and prints the titles'''
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Your-App-User-Agent"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
