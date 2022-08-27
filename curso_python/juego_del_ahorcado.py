import random
import os


def read_data(filepath="./archivos/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words


def run():
    data = read_data(filepath="./archivos/data.txt")
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
    
    while True:
        os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
        print("¡Adivina la palabra!")
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        
        if "_" not in chosen_word_list_underscores:
            os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
            print("¡Ganaste! La palabra era", chosen_word)
            break

if __name__ == '__main__':
    run()



# from random import random

# def get_word():
#     words= []
#     word= ""
#     position= 0

#     with open("./archivos/data.txt", "r", encoding="utf-8") as f:
#         for each in f:
#             words.append(each)
#     position= round(round(random()*1000)/(1000/171))
#     word= words[position]
#     return word

# def run():
#     selected_word= get_word()

#     ahorcado= ""
#     for each in selected_word:
#         ahorcado= ahorcado + "_"

#     print("JUEGO DEL AHORCADO")
#     print(ahorcado)
#     print(len(ahorcado))
#     word= input("Ingrese letra (vocales pueden llevar acento): ")

    

# if __name__ == '__main__':
#     run()