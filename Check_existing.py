from addresses import *


# ReLoad All Existing words in file to prevent ReTranslate
existing_words = []
def check_existing():
    try:
        with open(wordlist_address_windows, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if not line.startswith('|'):
                    existing_words.append(line[:-3].strip().lower())
        file.close()
    except:
        print('No File Already Exists, Creating...')
        open(wordlist_address_windows, 'w+', encoding='utf-8').close()
    return existing_words