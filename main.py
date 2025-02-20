import asyncio
import backend.connect as backend

def set_settings():
    backend.logo()
    ipaddress, port = backend.set_env()
    client = backend.set_client(ipaddress, port)
    return client

async def main():
    client = set_settings()
    print("\n[+] Hello operator!")
    while True:
        operator_message = backend.get_message()
        await backend.chat(client, operator_message)

        choice = input("\n\n[i] Are there more questions you would like to ask? (y/n): ")
        if choice.lower() == 'n':
            break
    
if __name__ == "__main__":
    asyncio.run(main())