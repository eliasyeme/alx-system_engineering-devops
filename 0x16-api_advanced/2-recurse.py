#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Get the titles of the first 10 hot posts for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
        subreddit, after
    )
    headers = {"User-Agent": "My User Agent 1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    for post in response.json().get("data").get("children"):
        hot_list.append(post.get("data").get("title"))
    after = response.json().get("data").get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
