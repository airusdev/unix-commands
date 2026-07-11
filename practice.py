
def count_words(string: str) -> int:
    string = string.strip().split(" ")
    word_count = len(string)
    
    return word_count


string = " hello hii airus"
count = count_words(string)
print(count)
