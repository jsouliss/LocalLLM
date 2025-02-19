import os
from dotenv import load_dotenv
import asyncio
from ollama import AsyncClient

def set_env():
    load_dotenv()
    ipaddress = os.getenv('IPADDRESS')
    port = os.getenv('PORT')
    return ipaddress, port

def set_client():
    client = (AsyncClient(
            host=f"http://{ipaddress}:{port}"))
    return client

async def chat(client, user_message):
    message = {
        'role':'user',
        'content':user_message,
    }
    async for part in await client.chat(
        model='qwen2.5:latest',
        messages=[message],
        stream=True):
            print(
                part['message']['content'],
                end='',
                flush=True
            )

def main():
    global ipaddress, port
    ipaddress, port = set_env()
    client = set_client()
    asyncio.run(chat(client, "Hello"))

if __name__ == "__main__":
    main()
