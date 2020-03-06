import random
import os
import subprocess
from forex_python.bitcoin import BtcConverter
bitcoin = BtcConverter()
random.seed(bitcoin.get_latest_price('EUR'))


def read_cards():
    # User input
    print('Enter the amount of cards')
    n_cards = int(input())
    print('Enter the card numbers speareted by spaces')
    card_number = input().replace(" ", "")
    
    card_number_list = list(card_number)
    if len(card_number_list) > n_cards:
        print("ERROR: More numbers than cards")
    else:
        print(card_number_list)
   
    # Start with clean files
    if os.path.exists("gather_cards.txt"):
        os.remove('gather_cards.txt')
    
    if os.path.exists("fortune.txt"):
        os.remove('fortune.txt')

    # Shuffle process
    selected_cards = []
    with open('gather_cards.txt', 'w+') as text_file:
        for i in range(n_cards):
            selected_cards.append(open('epavarmuus_cards/epavarmuus_' + str(card_number_list[i]) + '.txt', 'r'))
            text_file.write(selected_cards[i].read())
            selected_cards[i].close()
        # go back to the beginning of the file
        text_file.seek(0)
        text_as_lines = text_file.readlines()
        for i in range(len(text_as_lines)):
            text_as_lines[i] = text_as_lines[i].strip('\n')
        random.shuffle(text_as_lines)
        print(bitcoin.get_latest_price('EUR'))
        print(text_as_lines)
        with open('fortune.txt', 'w') as text_file:
            text_file.write(str(text_as_lines))

    subprocess.run(['open', 'fortune.txt'], check=True)
    
read_cards()


    


