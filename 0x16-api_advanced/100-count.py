#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=""):
    """
    Get the titles of the first 100 hot posts for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
        subreddit, after
    )
    headers = {"User-Agent": "My User Agent 1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    for post in response.json().get("data").get("children"):
        hot_list.append(post.get("data").get("title"))
    after = response.json().get("data").get("after")
    if after is None:
        word_dict = {}
        for word in word_list:
            word_dict[word] = 0
        for title in hot_list:
            for word in title.split():
                if word.lower() in word_dict:
                    word_dict[word.lower()] += 1
        for key, value in sorted(
            word_dict.items(), key=lambda x: x[1], reverse=True
        ):
            if value > 0:
                print("{}: {}".format(key, value))
        return
    return count_words(subreddit, word_list, hot_list, after)
