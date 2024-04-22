from fastapi import FastAPI
import asyncio
import os

app = FastAPI()

@app.get("/")
async def root(sleep: int = 0, size_kb: int = 0):
    await asyncio.sleep(sleep / 1000)  # Sleep for the requested amount of time (in milliseconds)
    
    # Generate a random string of the requested size in KB
    response = os.urandom(size_kb * 1024).hex()  # os.urandom returns random bytes, which are then converted to a hex string

    return {"message": response}
