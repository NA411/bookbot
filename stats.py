def get_num_words(text):
    count = len(text.split())
    return count

def count_chars(text):
    dict = {}
    for c in text:
        c_lower = c.lower()
        if dict.get(c_lower):
            dict[c_lower] =+ dict[c_lower] + 1
        else:
            dict[c_lower] = 1
    return dict

def sort_chars(dict):
    sorted_dict = {}
    sorted_items = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    for item in sorted_items:
        if item[0].isalpha():
            sorted_dict[item[0]] = item[1]
    return sorted_dict