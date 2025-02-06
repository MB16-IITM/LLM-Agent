from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import os

app = FastAPI()

# Define request model
class TaskRequest(BaseModel):
    task: str

# Function registry (maps task commands to functions)
FUNCTION_REGISTRY = {
    "format_file": lambda path, tool, version: format_file(path, tool, version),
}

# Example function to format a file using a tool like Prettier
def format_file(path: str, tool: str, version: str):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
        
        # Example command: prettier --write file.md
        cmd = [tool, "--write", path]
        subprocess.run(cmd, check=True)

        return {"status": "success", "formatted_file": path, "tool": tool, "version": version}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/run")
def run_task(request: TaskRequest):
    task = request.task.lower()  # Convert to lowercase for uniformity

    # Simple rule-based parsing (replace with LLM processing later)
    if "format" in task and "prettier" in task:
        # Extract parameters (in a real case, you’d use NLP/LLM parsing)
        parts = task.split()
        path = parts[1]  # Assume the file path is always second
        tool = parts[-2]  # Assume tool name is always second-last
        version = parts[-1]  # Assume version is last

        # Call the appropriate function
        if "format_file" in FUNCTION_REGISTRY:
            return FUNCTION_REGISTRY["format_file"](path, tool, version)
    
    return {"status": "error", "message": "Task not recognized"}

@app.get("/read")
def read_task(path: str):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
        
        with open(path, "r") as file:
            content = file.read()
        
        return {"path": path, "content": content}
    
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/")
def root():
    return {"message": "FastAPI App Running"}
