import random
import os
from for_game import common_letters, description, attempts


while True:
    print(f"""Привет, дорогой друг! Это игра "{common_letters("5БУКВ", "5БУКВ")}"!""")
    menu_item = input("Выбери действие снизу:\n1.Играть!\n2.Посмотреть правила.\n3.Выход.\nТвой выбор --> ")
    os.system("cls")
    if menu_item == "1":
        counter = 0
        all_words = ""
        with open("words.txt", encoding="utf-8") as f:
            hidden_word = random.choice(f.read().split("\n"))
        print("Итак, отгадывайте: ")
        while counter <= 6:
            word = input("Ваше слово: ").upper().strip()
            if word == "СДАЮСЬ":
                os.system("cls")
                print(f"""Эээх, вы! Ну ладно, это было слово - "{hidden_word}" """)
                break
            if len(set(word)) >= 3:
                if len(word) == 5:
                    if len(set(hidden_word) & set(word)) != 0:
                        if hidden_word == word:
                            os.system("cls")
                            print(f"""Поздравляю тебя, дружище! Ты выиграл, это дейсвительно слово  "{common_letters(hidden_word, word)}" """)
                            break
                        else:
                            counter += 1
                            all_words += f"{common_letters(hidden_word, word)}\n"
                    os.system("cls")
                    print(all_words)
                    print(f"Осталось попыток: {attempts(6 - counter)}")
                else:
                    print("Ваше слово должно состоять из 5 букв! Попробуйте ещё раз.")
                if counter == 6:
                    print(f"""К сожалению, вы проиграли это было слово - "{hidden_word}" """)
                    break
            else:
                print("Слово из 5 букв не может состоять из 1-2 букв, попробуйте написать другое слово!")
    elif menu_item == "2":
        print(description)
    elif menu_item == "3":
        print("Эх, уже уходишь? ")
        print("Мы будем тебя ждать!")
        break
    else:
        print("Пожалуйста, выбирайте между (1-3)!")