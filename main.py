from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("Demo")


Notes_File = os.path.join(os.path.dirname(__file__), "notes.txt")

def verify_file():
    if not os.path.exists(Notes_File):
        with open(Notes_File, "w") as f:
            f.write("")   

def get_notes():
    with open(Notes_File, "r") as f:
        notes = f.read().strip()
    return notes if notes else "No notes found"               


# Add an addition tool
@mcp.tool()
def add_note(message : str) -> str:
    verify_file()
    with open(Notes_File, "a") as f:
        f.write(message + "\n")
    return "Note added"    


@mcp.tool()
def read_notes() -> str:
    verify_file()
    get_notes()

@mcp.resource("notes://latest")
def get_latest_note() -> str :
    verify_file()
    with open(Notes_File, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "no lines"   

@mcp.prompt()
def note_summary_prompt() -> str:
    verify_file()
    with open(Notes_File, "r") as f:
        notes = f.read().strip()
    if not notes :
        return "No notes found"
    return f"Summarize the following notes:{notes}"    
    