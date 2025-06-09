#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    r_status = r.status_code
    print("Status Code: {}".format(r_status))

    if r_status == 200:
        posts = r.json()
        
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    r_status = r.status_code

    if r_status == 200:
        posts = r.json()
        list_posts = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]
    
        with open('posts.csv', 'w', newline='', encoding='utf-8') as file:
            field = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=field)
            writer.writeheader()
            writer.writerows(list_posts)
