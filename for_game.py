from colorama import init
from colorama import Fore, Style, Back

init(autoreset=True)

def common_letters(word1: str, word2: str) -> str:
    res = ""
    word2 = word2.upper()
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            res += Style.NORMAL + Fore.BLACK + Back.YELLOW + word2[i].upper() + "\033[0m "
        elif word2[i] in word1:
            res += Style.DIM + Fore.BLACK + Back.WHITE + word2[i].upper() + "\033[0m "
        else:
            res += Style.DIM + Fore.BLACK + Back.RED + word2[i].upper() + "\033[0m "
    return res

def attempts(number: int):
    if number > 0:
        if 5 <= number <= 6:
            return f"{Fore.GREEN}{number}\033[0m"
        elif 3 <= number <= 4:
            return f"{Fore.YELLOW}{number}\033[0m"
        else:
            return f"{Fore.RED}{number}\033[0m"
    else:
        return number

description = f"""
Описание:
\tПривет дружище! Это игра "5 букв", в ней тебе предстоит за 6 попыток отгадать загаданное слово! Испугался?
Не переживай! Ниже можно будет прочитать про подсказки, и ты поёмешь, что всё не так уж и тяжело!

Обозначения:

\t"{Style.NORMAL + Fore.BLACK + Back.YELLOW}А\033[0m"- если ты встретил такое обозначение в введённом слове, то это означает, 
что именно эта буква стоит именно на этом месте в загаданном слове.
\t"{Style.DIM + Fore.BLACK + Back.WHITE }Б\033[0m"- если ты встретил такое обозначение в введённом слове, то это означает, что эта буква есть в загаданном слове, 
но стоит она не на этом месте.
\t"{Style.DIM + Fore.BLACK + Back.RED}В\033[0m" - если же твоя буква помечена красным, то её нет в загаданном слове.

Правила: 
\tУ тебя 6 попыток, попытка засчитывается, когда хотя бы одна буква либо совпадает, либо есть в слове.Например,
если загаданное слово "арбуз", а ты ввел слово "фикус", то попытка зачтётся, т.к у слов "арбуз" и "фикус" 
совпадает буква "у". Удачной игры тебе, дружище!
"""