This function reads one .py file, parses it with the ast module, and returns a list of dictionaries — one for each function and class found.
Here's what it needs to do:
def parse_file(file_path: Path) -> list[dict[str, Any]]:
Read the file — file_path.read_text(encoding="utf-8") into a variable called raw
Parse to AST — tree = ast.parse(raw) — this gives you the full AST tree
Walk the tree — for node in ast.walk(tree): — this visits every single node in the tree
Filter for functions and classes — check isinstance(node, ast.FunctionDef) and isinstance(node, ast.ClassDef)
Build entries — for each match, call _build_entry(node, raw, file_path, kind="function" or "class") and add to a list
Handle errors — wrap the read_text + ast.parse in a try/except for SyntaxError
Return the list


isinstance(object, type) checks if object is an instance of the given type (or one of its subclasses). It returns True or False.
isinstance("hello", str)   # True — "hello" is a string
isinstance(42, str)        # False — 42 is not a string
isinstance(node, ast.FunctionDef)  # True if node is a function definition


<img width="1478" height="856" alt="image" src="https://github.com/user-attachments/assets/c9f6f91f-45d1-44f6-854a-83ca6bc585b8" />
