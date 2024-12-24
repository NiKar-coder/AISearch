from AI import AI
import asyncio
from colorama import init, Fore, Style, Back


init(autoreset=True)


async def set_answer():
    print("You:", end=" ")
    question = input()
    print(Back.BLACK + Style.DIM + "\nPlease wait...\n")
    ai = AI()
    await ai.ask(question)
    print("  " + Back.BLACK + Style.BRIGHT + Fore.LIGHTGREEN_EX + ai.ans)


if __name__ == "__main__":
    asyncio.run(set_answer())
