# todo list
# 1. add a todo
# 2. remove a todo
# 3. list all todos
# 4. mark a todo as complete
# 5. mark a todo as incomplete
# 6. quit

todos = []
def welcome_message():
    print("Welcome to the todo list")
    print("1. Add a todo")
    print("2. Remove a todo")
    print("3. List all todos")
    print("4. Mark a todo as complete")
    print("5. Mark a todo as incomplete")
    print("6. Quit")

def add_todo():
    todo = input("Enter a todo: ")
    todos.append({
        'content': todo,
        'completed': False
    })
    print(f"Todo '{todo}' added successfully")

def remove_todo():
    todo = input("Enter a todo: ")
    for _todo in todos:
        if _todo['content'] == todo:
            todos.remove(_todo)
            print(f"Todo '{todo}' removed successfully")
            break
    else:
        print(f"Todo '{todo}' not found")
        remove_todo()

def list_todos_with_status():
    print("All todos:")
    for todo in todos:
        print(f"{todo['content']} - {'Completed' if todo['completed'] else 'Incomplete'}")

def mark_todo_as_complete():
    todo = input("Enter a todo: ")
    for _todo in todos:
        if _todo['content'] == todo:
            _todo['completed'] = True
            print(f"Todo '{todo}' marked as complete")
            break
    else:
        print(f"Todo '{todo}' not found")
        mark_todo_as_complete()

def mark_todo_as_incomplete():
    todo = input("Enter a todo: ")
    for _todo in todos:
        if _todo['content'] == todo:
            _todo['completed'] = False
            print(f"Todo '{todo}' marked as incomplete")
            break
    else:
        print(f"Todo '{todo}' not found")
        mark_todo_as_incomplete()


def main():
    welcome_message()
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            add_todo()
        elif choice == "2":
            remove_todo()
        elif choice == "3":
            list_todos_with_status()
        elif choice == "4":
            mark_todo_as_complete()
        elif choice == "5": 
            mark_todo_as_incomplete()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()