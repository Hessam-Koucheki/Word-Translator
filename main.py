import gather
from os import system
wordlist_address = '/mnt/g/Codes/Python/Trasnlator/WordLists.txt'

# ReLoad All Existing words in file to prevent ReTranslate
existing_words = []
with open(wordlist_address, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if not line.startswith('|'):
            existing_words.append(line[:-3].strip())
file.close()

# Main Loop to input Words to be translated
with open(wordlist_address, 'a+') as file:
    while True:
        # Input WORD
        print('|----------------------------------------')
        word_input = input('Enter A Word To Translate: ').strip()
        if word_input == '/exit':
            break
        elif word_input == '/clear':
            open(wordlist_address, 'w').close()
            system('clear || cls')
            print('All file contents have been erased!!')

        elif word_input in existing_words:
            print(word_input.upper() + ' exists!!')
            continue
        # Request To TRANSLATE Word
        meanings = gather.Translate(word_input)
        if meanings:
            # Store In a FILE
            file.writelines(word_input.capitalize() + ' :' + '\n') # Write WORD
            for this_mean in meanings: # Write MEANINGS
                file.writelines('||\t' + this_mean + '\n')
            file.writelines('|--------------------------------------------------------------\n\n')
            existing_words.append(word_input.strip().capitalize()) # Add to Existing List to avoid duplication
        file.flush()

file.close()
