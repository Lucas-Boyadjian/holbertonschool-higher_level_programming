#!/usr/bin/python3
"""
Module for interacting with JSONPlaceholder API.

This module provides functions to fetch posts from the JSONPlaceholder API
and either display them to console or save them to a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from the JSONPlaceholder API and prints their
    titles to console.

    Makes a GET request to retrieve all posts and displays the status code.
    If successful (status code 200), prints each post title.
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    r_status = r.status_code
    print("Status Code: {}".format(r_status))

    if r_status == 200:
        posts = r.json()

        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches posts from the JSONPlaceholder API and saves them to a CSV file.

    Makes a GET request to retrieve all posts.
    If successful (status code 200), extracts id, title, and body of each post
    and writes them to a CSV file named 'posts.csv'.
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    r_status = r.status_code

    if r_status == 200:
        posts = r.json()
        list_posts = [{"id": post["id"], "title": post["title"],
                       "body": post["body"]} for post in posts]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as file:
            field = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=field)
            writer.writeheader()
            writer.writerows(list_posts)
