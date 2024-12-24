from AI import AI
import asyncio
from colorama import init, Fore, Style, Back


init(autoreset=True)


async def main():
    print("\nYou:", end=" ")
    question = input()
    print("")
    if question == "EXIT":
        exit(0)
    print(Back.BLACK + Style.DIM + "Please wait...", end="\n\n")
    ai = AI()
    await ai.ask(question)
    print("  " + Back.BLACK + Style.BRIGHT + Fore.LIGHTGREEN_EX + ai.ans)


if __name__ == "__main__":
    while True:
        asyncio.run(main())
