"""The program's name:  Plot GitHub Repositories for a New Language
The author: Rajani Baraili
The purpose of the program:  programs uses the GitHub API to find the most-starred Python projects and plots them with plotly.
Any info about starter code (If used, where it came from, link, etc.), and the: none
Date: 5/12/2026
"""
import requests 
import plotly.express as ex


url = "https://api.github.com/search/repositories?q=language:java&sort=stars"

r = requests.get(url)
print(f"Status code: {r.status_code}")

response_dict = r.json()
repo_dicts = response_dict["items"]