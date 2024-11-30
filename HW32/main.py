import os
import string
import time
import asyncio
import requests
from faker.generator import random as rand

async def get_response(url):
    return requests.get(url)

async def fetch_pic():
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    random_name = ''.join(rand.choices(string.ascii_letters + string.digits, k=5))
    response = await asyncio.create_task(get_response(url))

    if response.status_code == 200:
        with open(f'{path}/{random_name}.jpg', 'wb') as f:
            f.write(response.content)

coroutines=10
start=time.time()
for _ in range(coroutines):
    asyncio.run(fetch_pic())
print(f"Executed in {time.time()-start}s")