def get_num_words(book):
    words = book.split()
    num_words = len(words)
    
    return num_words


def get_char_num(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items["num"]

def get_sorted_list(dic):
    sort_list = []
    count = 0
    for c in dic:
        sort_list.append({"char": c, "num": dic[c]})
       
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list

        

        

    