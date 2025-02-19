import os
from dotenv import load_dotenv
from ollama import AsyncClient

def logo():
    print(r"""
____________________________            .____    .____       _____   
\______   \__    ___\_____  \           |    |   |    |     /     \  
 |       _/ |    |   /   |   \   ______ |    |   |    |    /  \ /  \ 
 |    |   \ |    |  /    |    \ /_____/ |    |___|    |___/    Y    \
 |____|_  / |____|  \_______  /         |_______ |_______ \____|__  /
        \/                  \/                  \/       \/       \/ """)
    print("\n")

def set_env():
    load_dotenv()
    ipaddress = os.getenv('IPADDRESS')
    port = os.getenv('PORT')
    return ipaddress, port

def set_client(ipaddress, port):
    client = (AsyncClient(
            host=f"http://{ipaddress}:{port}"))
    return client

def get_message():
    operator_message = input(
        "[i] Please enter you message: ")
    return operator_message

async def chat(client, user_message):
    message = {
        'role':'user',
        'content':user_message,
    }
    print('\n')
    async for part in await client.chat(
        model='qwen2.5:latest',
        messages=[message],
        stream=True):
            print(
                part['message']['content'],
                end='',
                flush=True
            )