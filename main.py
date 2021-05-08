import gather

class Word:
    def __init__(self, data):
        self.word = data


word_input = input()

gather.Translate(word_input)