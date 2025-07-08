def valid_word_abbreviation(word, abbr):
    #  a valid abbr replaces the characters with an integer 
    #  signifying the count of characters replaced
    #  examples - leading digits in the abbreviation? 
    #  apple -> 3le ? is this valid? 
    """
    calendar, c4dar => true
    
    Pseudocode
    starting from index 0, check that characters are the same for each str
    if the next character in abbr is an int
    save that number and start counting the letters in word until the next character matches 
    the character after abbr
    continue checking that the characters match at each position
    
    """
    i = 0
    j = 0
    while i < len(word) and j < len(abbr):
        if word[i] == abbr[j]:
            i += 1
            j += 1
        elif abbr[j].isdigit():
            count = 0
            while j < len(abbr) and abbr[j].isdigit():
                count = count * 10 + int(abbr[j])
                j += 1
            i += count
        else:
            return False

result = valid_word_abbreviation('calendar', 'c4dar')
print(result)