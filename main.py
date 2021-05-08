import gather

class Word:
    def __init__(self, word, meanings_list):
        self.word = word
        self.meaning =meanings_list

list_of_words = []

while True:
    word_input = input('Enter A Word To Translate: ')
    if word_input == 'exit':
        break
    tmp_meanings = gather.Translate(word_input)
    tmp_word = Word(word_input, tmp_meanings)
    list_of_words.append(tmp_word)


for t in list_of_words:    
    print(t.meaning)