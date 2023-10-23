#!/usr/bin/python3
'''Returns information about his/her TODO list progress.
'''
import requests
import sys
if __name__ == "__main__":
    todo = requests.get('https://jsonplaceholder.typicode.com/todos/1',
                        params={'userId': sys.argv[1]}).json()
    user = requests.get('https://jsonplaceholder.typicode.com/todos/1{}'
                        .format(sys.argv[1])).json()
    completed = [task.get('title')
                 for task in todo if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completed), len(todo)))
    [print("\t {}".format(title)) for title in completed]
