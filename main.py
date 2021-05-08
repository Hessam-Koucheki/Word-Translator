import gather

existing_words = []

# ReLoad All Existing words in file to prevent ReTranslate
with open('WordLists.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if not line.startswith('|'):
            existing_words.append(line[:-3].strip())

# Main Loop to input Words to be translated
with open('WordLists.txt', 'a+') as file:    
    while True:
        # Input WORD
        word_input = input('Enter A Word To Translate: ').strip()
        if word_input == '/exit':
            break
        elif word_input in existing_words:
            print(word_input.upper() + ' exists!!')
            continue
        # Request To TRANSLATE Word
        tmp_meanings = gather.Translate(word_input)
        # Store In a FILE
        file.writelines(word_input.capitalize() + ' :' + '\n') # Write WORD
        for this_mean in tmp_meanings: # Write MEANINGS
            file.writelines('||\t' + this_mean + '\n')
        file.writelines('|-------------------------------\n')
        existing_words.append(word_input.strip().capitalize()) # Add to Existing List to avoid duplication


file.close()
