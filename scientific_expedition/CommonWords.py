def checkio(first, second):
    
    all_text = first + "," + second
    words_list = all_text.split(",")
    words_set = set(words_list)
    max_count = 1
    max_word = []
    
    for w in words_set:
        c = words_list.count(w)
        if c > max_count:
            max_word.append(w)
            
    max_word.sort()
    return ",".join(max_word)
