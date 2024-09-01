from fastapi import FastAPI, HTTPException
import subprocess
import os

app = FastAPI()

# Define the directory where the script files are located
SCRIPT_DIR = r"C:\Users\alric\backend\procomm"
SCRIPT_NAME = "aiztest.py"  # The specific script to execute

@app.post("/execute/")
async def execute_script():
    # Construct the path to the script file
    script_path = os.path.join(SCRIPT_DIR, SCRIPT_NAME)

    # Ensure the file exists and is a Python file
    if not os.path.isfile(script_path) or not script_path.endswith(".py"):
        raise HTTPException(status_code=404, detail="Script not found")

    try:
        # Run the Python script
        result = subprocess.run(
            ["python", script_path],  # Run the script with Python
            capture_output=True,
            text=True,
            check=True
        )
        return {"stdout": result.stdout, "stderr": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"stdout": e.stdout, "stderr": e.stderr}

@app.get("/")
def read_root():
    return {"Hello": "World"}
