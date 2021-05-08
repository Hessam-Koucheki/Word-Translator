import gather

class Word:
    def __init__(self, word, meanings_list):
        self.word = word
        self.meanings =meanings_list

list_of_words = []

while True:
    word_input = input('Enter A Word To Translate: ')
    if word_input == '/exit':
        break
    tmp_meanings = gather.Translate(word_input)
    tmp_word = Word(word_input, tmp_meanings)
    list_of_words.append(tmp_word)


with open('WordLists.txt', 'a+') as file:    
    for this_word in list_of_words:
        file.writelines(this_word.word + ' :' + '\n')
        for this_mean in this_word.meanings:
            file.writelines('||\t' + this_mean + '\n')
        file.writelines('-------------------------------\n')
    file.close()
