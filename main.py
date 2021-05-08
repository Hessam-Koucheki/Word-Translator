import gather

class Word:
    def __init__(self, word, meanings_list):
        self.word = word
        self.meanings =meanings_list

existing_words = []
list_of_words = []

# ReLoad All Existing words in file to prevent ReTranslate
with open('WordLists.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if not line.startswith('|'):
            existing_words.append(line[:-3])

# Main Loop to input Words to be translated
while True:
    # Input WORD
    word_input = input('Enter A Word To Translate: ')
    if word_input == '/exit':
        break
    # Request To TRANSLATE Word
    tmp_meanings = gather.Translate(word_input)
    # Store In a CLASS 
    tmp_word = Word(word_input, tmp_meanings)
    # Append Class To the LIST
    list_of_words.append(tmp_word)


with open('WordLists.txt', 'a+') as file:    
    for this_word in list_of_words:
        file.writelines(this_word.word + ' :' + '\n')
        for this_mean in this_word.meanings:
            file.writelines('||\t' + this_mean + '\n')
        file.writelines('|-------------------------------\n')
file.close()
