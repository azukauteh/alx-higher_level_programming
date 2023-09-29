#!/usr/bin/python3
# Define the GitHub API endpoint to retrieve user information
import sys
import requests

def display_github_user_id(username, password):
    api_endpoint = 'https://api.github.com/user'

    # Make a GET request to the GitHub API using Basic Authentication
    response = requests.get(api_endpoint, auth=(username, password))

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Extract and display the user ID from the API response
        user_id = response.json().get('id')
        print('Your GitHub user ID is:', user_id)
    else:
        print('Failed to retrieve GitHub user ID. Status code:', response.status_code)

if __name__ == "__main__":
    # Check if both username and password (personal access token) are provided as arguments
    if len(sys.argv) != 3:
        print('Usage: python script.py <username> <personal_access_token>')
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    display_github_user_id(username, password)

