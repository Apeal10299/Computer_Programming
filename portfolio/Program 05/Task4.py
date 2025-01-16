#Write a program that takes a URL as a command-line argument and reports whether or not there is a working website at that address.
#Hint: You need to get the HTTP response code.
#Another Hint: StackOverflow is your friend.'''

import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Usage: Checking Website")
        return

    url = sys.argv[1]

    try:
        response = requests.head(url, timeout=5)
        if 200 <= response.status_code < 400:
            print(f"The website at {url} is working (Status Code: {response.status_code}).")
        else:
            print(f"The website at {url} is not working (Status Code: {response.status_code}).")
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to {url}. Error: {e}")

main()

