from typing import Union

from fastapi import FastAPI

app= FastAPI()

@app.get(r"C:\Users\alric\Documents\work\Ultimate\Appfiles\aiztest.py")
def read_root():
    return {"message": "skibidi"}
