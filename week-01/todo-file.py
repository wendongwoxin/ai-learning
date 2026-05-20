import json
from datetime import datetime
from pathlib import Path

# 与脚本同目录的 todos.json（无论从仓库根目录还是 week-01 目录运行都能找到）
DATA_PATH = Path(__file__).resolve().parent / "todos.json"


def create_todos_file():
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as file:
        json.dump([], file, ensure_ascii=False, indent=4)


def read_todos_from_file():
    """读取 JSON；文件不存在则创建空文件并返回 []。"""
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        create_todos_file()
        return []
    except json.JSONDecodeError:
        print(f"警告：{DATA_PATH.name} 内容不是合法 JSON，将按空列表处理。")
        return []
    except OSError as e:
        print(f"读取失败：{e}")
        return []


def save_todos_to_file(todos):
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(todos, file, ensure_ascii=False, indent=4)

# add a todo to the json file
def add_todo_to_file(todo):
    todos = read_todos_from_file()
    todos.append({
        'content': todo,
        'completed': False,
        'created_at': datetime.now().isoformat()
    })
    save_todos_to_file(todos)
    print(f"Todo '{todo}' added successfully")

# remove a todo from the json file
def remove_todo_from_file():
    todo = input("Enter a todo: ")
    todos = read_todos_from_file()
    for _todo in todos:
        if _todo['content'] == todo:
            todos.remove(_todo)
            save_todos_to_file(todos)
            print(f"Todo '{todo}' removed successfully")
            break
    else:
        print(f"Todo '{todo}' not found")
        remove_todo_from_file()

# list all todos from the json file
def list_todos_from_file():
    todos = read_todos_from_file()
    for todo in todos:
        print(f"{todo['content']} - {'Completed' if todo['completed'] else 'Incomplete'}")

# mark a todo as complete in the json file
def mark_todo_as_complete_in_file():
    todo = input("Enter a todo: ")
    todos = read_todos_from_file()
    for _todo in todos:
        if _todo['content'] == todo:
            _todo['completed'] = True
            save_todos_to_file(todos)
            print(f"Todo '{todo}' marked as complete")
            break
    else:
        print(f"Todo '{todo}' not found")
        mark_todo_as_complete_in_file()

# mark a todo as incomplete in the json file
def mark_todo_as_incomplete_in_file():
    todo = input("Enter a todo: ")
    todos = read_todos_from_file()
    for _todo in todos: 
        if _todo['content'] == todo:
            _todo['completed'] = False
            save_todos_to_file(todos)
            print(f"Todo '{todo}' marked as incomplete")
            break
    else:
        print(f"Todo '{todo}' not found")
        mark_todo_as_incomplete_in_file()

# main function
def main():
    read_todos_from_file()
    while True:
        print("1. Add a todo")
        print("2. Remove a todo")
        print("3. List all todos")
        print("4. Mark a todo as complete")
        print("5. Mark a todo as incomplete")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            todo = input("Enter a todo: ")
            add_todo_to_file(todo)
        elif choice == "2":
            remove_todo_from_file()
        elif choice == "3":
            list_todos_from_file()
        elif choice == "4":
            mark_todo_as_complete_in_file()
        elif choice == "5":
            mark_todo_as_incomplete_in_file()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()