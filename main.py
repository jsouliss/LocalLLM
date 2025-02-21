import asyncio
import backend.connect as backend

def set_settings():
    backend.logo()
    ipaddress, port = backend.Model.set_env()
    client = backend.Model.set_client(ipaddress, port)
    return client

def set_Model():
    print(
        """
    Available models: \n
        [+] deepseek-r1-abliterated:8b
        [+] deepseek-r1:8b
        [+] qwen2.5:latest
        [+] llama2-uncensored:latest
        [+] dolphin-mistral:latest
        """)
    model_name = input("[+] Please enter the model name: ")
    return model_name

async def main():
    model_name = set_Model()
    client = set_settings()
    try:
        rtoModel = backend.Model(model_name)
        print("[+] Connection successful!")
        print("\n[+] Hello operator!")
        while True:
            operator_message = rtoModel.get_message()
            await rtoModel.chat(client, operator_message)
            choice = input("\n\n[i] Are there more questions you would like to ask? (y/n): ")
            if choice.lower() == 'n':
                break
    except Exception as e: 
        print("[!] An error has occurred", e)
        
if __name__ == "__main__":
    asyncio.run(main())
