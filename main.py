import gather
from os import system
wordlist_address = '/mnt/c/Users/Hessam/Desktop/WordLists.txt' # wsl format
notepad_command = 'notepad.exe ' + r'C:\\Users\\Hessam\\Desktop\\WordLists.txt' # windows format

# ReLoad All Existing words in file to prevent ReTranslate
existing_words = []
try:
    with open(wordlist_address, 'r+') as file:
        lines = file.readlines()
        for line in lines:
            if not line.startswith('|'):
                existing_words.append(line[:-3].strip())
    file.close()
except:
    print('No File Already Exists, Creating...')
    open(wordlist_address, 'w+').close()


# Main Loop to input Words to be translated
with open(wordlist_address, 'a+') as file:
    while True:
        # Input WORD
        print('|----------------------------------------')
        word_input = input('Enter A Word To Translate: ').strip()
        if word_input == '/exit':
            break
        elif word_input == '/clear':
            open(wordlist_address, 'w+').close()
            system('clear || cls')
            existing_words = []
            print('All file contents have been erased!!')
        elif word_input == '/open':
            system(notepad_command)
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
