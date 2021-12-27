import asyncio
from httpx import get

async def request():
  await get('https://jsonplaceholder.typicode.com/todos/1')