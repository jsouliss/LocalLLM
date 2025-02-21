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
            \/                  \/                  \/       \/       \/""")
    print("\n")

class Model:
    def __init__(self, llm_name):
        self.llm_name = llm_name
    
    @staticmethod
    def set_env():
        load_dotenv()
        port = os.getenv('PORT')
        ipaddress = os.getenv('IPADDRESS')
        return ipaddress, port

    @staticmethod
    def set_client(ipaddress, port):
        client = (AsyncClient(
                host=f"http://{ipaddress}:{port}"))
        return client

    def get_message(self):
        operator_message = input(
            "[i] Please enter you message: ")
        return operator_message

    async def chat(self,client, user_message):
        message = {
            'role':'user',
            'content':user_message,
        }
        print('\n')
        async for part in await client.chat(
            model=f'{self.llm_name}',
                messages=[message],
            stream=True):
                print(
                    part['message']['content'],
                    end='',
                    flush=True
                )
