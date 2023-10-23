#!/usr/bin/python3
'''Returns information about his/her list progress.
'''
from requests import get
from sys import argv

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com/todos/1'
    todo_url = main_url + "/user/{}/todos".format(argv[1])
    name_url = main_url + "/users/{}".format(argv[1])
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()

    TOTAL_NUMBER_OF_TASKS = len(todo_result)
    NUMBER_OF_DONE_TASKS = len([todo for todo in todo_result
                         if todo.get("completed")])
    EMPLOYEE_NAME = name_result.get("EMPLOYEE_NAME")
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for todo in todo_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
