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
