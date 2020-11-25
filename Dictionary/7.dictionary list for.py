favorites = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, lang in favorites.items():
    print(name, 'fav languageis')
    for language in lang:
        print(language)