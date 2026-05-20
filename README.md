# ai-learning

个人 AI / Python 学习仓库。

## 第一周（week-01）

目录：[week-01](week-01)

| 文件 | 说明 |
|------|------|
| [week-01/helloworld.py](week-01/helloworld.py) | 最小示例：打印 `Hello, World!` |
| [week-01/todo.py](week-01/todo.py) | 命令行待办（英文菜单），数据仅在内存中，退出即清空 |
| [week-01/todo-file.py](week-01/todo-file.py) | 同上交互与菜单，数据写入 [week-01/todos.json](week-01/todos.json)，重启后保留 |

### 运行方式

在项目根目录执行：

```bash
python3 week-01/helloworld.py
```

```bash
python3 week-01/todo.py
```

```bash
python3 week-01/todo-file.py
```

### `todo.py` / `todo-file.py` 菜单（一致）

1. Add a todo — 输入内容添加一条待办  
2. Remove a todo — 按内容删除（找不到会提示并让重新输入）  
3. List all todos — 列出所有待办及完成状态  
4. Mark a todo as complete — 按内容标记为已完成  
5. Mark a todo as incomplete — 按内容标记为未完成  
6. Quit — 退出  

**数据模型**

- `todo.py`：字典字段 `content`、`completed`。  
- `todo-file.py`：在写入文件时额外带 `created_at`（ISO 时间字符串）；`todos.json` 与脚本同目录，首次运行若文件不存在会自动创建空数组 `[]`。  
