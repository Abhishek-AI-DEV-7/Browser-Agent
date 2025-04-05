from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
from browser_use import Agent, Browser, BrowserConfig
load_dotenv()

import asyncio

browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    )
)
llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="""First, visit the website https://secondbrainlabs.com/ to understand what they are building. 
        Go to Y Combinator, reddit pages, and other popular websites to search for companies that are currently working on a similar goal or idea as the Indian startup Second Brain Labs, 
        go to an online notepad website and list down companies you found.""",
        llm=llm,
        browser=browser,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())