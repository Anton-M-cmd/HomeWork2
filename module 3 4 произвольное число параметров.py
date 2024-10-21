def single_root_words(root_word , *other_words):
    same_words=[]
    other_words_lower = [word.lower() for word in other_words]
    if other_words_lower.count(root_word.lower()):
        same_words.append()






result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)