import ast
from pathlib import Path
from typing import Any


''' _build_entry is a helper function. Its single job is to take one AST node (a function or a class from a Python file) and turn it into a neat dictionary that the rest of the tool can work with.
Think of it like repacking. The ast module gives you raw Python objects — _build_entry repacks them into a simple dictionary. Every function and class in the codebase will end up as one of these dictionaries.'''

def _build_entry(
    node: ast.FunctionDef | ast.ClassDef,  #function or class
    raw_source: str,  #entire file is just a big string , ast.get_source_segment needs raw text to extract code of this function or class 
    file_path: Path, 
    kind: str,        #doesnt itself figure out if its function or class , the caller tells it
) -> dict[str, Any]:
    
    doc = ast.get_docstring(node) or ""  
    
     #spilt lines takes the entire text of source and breaks into lines , /n at the end 
    source_code=ast.get_source_segment(raw_source,node)
    
    if source_code is None:
        source_code = ast.unparse(node)   #fallback
    
    return {
        "file_path": str(file_path.resolve()),
        "name": node.name,
        "kind": kind,
        "docstring": doc,
        "source": source_code,
        "line": node.lineno,
    }
    #return bundles everything together ....file_path_resolve will give absolute path


    #ast.unparse() converts ast node back into string of python
    # i think ast.get_source_segment ususally works but returns none in a few edge cases
    # in that case ast.unparse is a fallback , it recreates python code from the ast itself 
    # so youd never end up with none source. 
    # 
    # but the tradeoff is that unparse doesnt preserve origiinal formatting 
    # , comments or whitespace.

def parse_file(file_path: Path) -> list[dict[str, Any]]:
    try:
        raw = file_path.read_text(encoding="utf-8")
        tree = ast.parse(raw)
    except SyntaxError:
        return []

    results=[]

    for node in ast.walk(tree):
        if isinstance(node,ast.FunctionDef):
            results.append(_build_entry(node, raw, file_path, "function"))
        elif isinstance(node,ast.ClassDef):
            results.append(_build_entry(node,raw,file_path,"class"))

    return results 

'''so what did this function do?

i think it read text from path , then parsed it then checked if it is function or classes 

and depending on what it is , it added it to results '''




#Scan Directory will find all py files from the folders and use parse_file on each one of them
    
          
def scan_directory(root: str | Path) -> list[dict[str, Any]]:
    #convert root to a Path and find all .py files. The method is .rglob("*.py") (recursive glob). Write just this:
    root_path = Path(root).resolve()  
    #path(root) turns root lets say './src' into a path object with all methods
    #it can sometimes give unpredictable paths , since it is relative
    # so we use .resolve() to make the path absolute ex: 
        # "./src" becomes /Users/ramster/Shadow Indexer/.../simplyCLI/src
        #root_path = ... — stores it in a variable


    #Create an empty list and a for loop with rglob:
    entries = []
    
    for py_file in sorted(root_path.rglob("*.py")):
        
        
       # sorted() keeps the order consistent across runs. rglob("*.py") recursively finds every .py file under the directory.
       # here rglob is recursive glob to find matches of *.py with files ending in py
       # only glob would only look at top level folder
        entries.extend(parse_file(py_file))

        #we are using extend instead of .append() because we append will give us a list of lists
        # extend: [1,2] with [3,4] is [1,2,3,4]
        # append : [1,2] with [3,4] is [1,2,[3,4]]
        #WE need one list so im taking a .extend 
        
        
        

    return entries
        
