word = "объектно-ориентированный"

# Слово "объект"
word_obj = word[:word.index('-')]
print("Слово 'объект':", word_obj)

# Слово "ориентир"
start_orientir = word.index('-') + 1
end_orientir = word.rindex('и')
word_orientir = word[start_orientir:end_orientir]
print("Слово 'ориентир':", word_orientir)

# Слово "тир"
word_tir = word[word.rindex('и') + 1:]
print("Слово 'тир':", word_tir)

# Слово "кот"
letters_kot = ['к', 'о', 'т']
word_kot = ''.join([char for char in letters_kot if char in word])
print("Слово 'кот':", word_kot)

# Слово "рента"
start_renta = word.rindex('о') + 1
word_renta = word[start_renta:]
print("Слово 'рента':", word_renta)