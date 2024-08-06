ban_words = ["не", "плохой", "ban"]
def words_filter(words):
    for ban_word in ban_words:
        if ban_word in words:
            words.remove(ban_word)
    return words
    #
    #
print(words_filter(["Иосиф", "не", "хороший", "учитель"]))
