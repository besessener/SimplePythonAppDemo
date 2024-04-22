from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/hello")
async def hello(sleep: int = 0, size_kb: int = 0):
    await asyncio.sleep(sleep)
    
    # Generate a random string of the requested size in KB
    response = os.urandom(size_kb * 1024).hex()  # os.urandom returns random bytes, which are then converted to a hex string

    return {"message": response}
