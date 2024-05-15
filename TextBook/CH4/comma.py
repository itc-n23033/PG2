def insert_and(spam):
    if len(spam) == 0:
        return ''
    elif len(spam) == 1:
        return spam[0]
    else:
        return ', '.join(spam[:-1]) + ', and ' + spam[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
print(insert_and(spam))
