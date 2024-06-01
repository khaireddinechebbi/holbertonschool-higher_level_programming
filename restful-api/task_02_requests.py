#!/usr/bin/python3
"""
Module for fetching and processing data from JSONPlaceholder API.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints their titles.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"status code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            dic1 = {'id': post['id']}
            dic2 = {'title': post['title']}
            dic3 = {'body': post['body']}
        list = [dic1, dic2, dic3]
        with open('posts.csv', mode='w', newline='') as f:
            csv_writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            csv_writer.writeheader()
            csv_writer.writerows(list)
