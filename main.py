import asyncio
from decimal import FloatOperation

import backend.connect as backend

def set_settings():
    backend.logo()
    ipaddress, port = backend.set_env()
    client = backend.set_client(ipaddress, port)
    return client
    
def llm_com(client):
    while True:
        operator_message = backend.get_message()
        asyncio.run(backend.chat(client, operator_message))

        choice = input("\n\n[i] Are there more questions you would like to ask? (y/n): ")
        if choice.lower() == 'n':
            
            break
        asyncio.new_event_loop()

def main():
    client = set_settings()
    print("\n[+] Hello operator!")
    llm_com(client)
    
if __name__ == "__main__":
    main()