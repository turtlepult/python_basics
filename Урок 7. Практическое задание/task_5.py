def vinni_mf_puh(str):
    str = str.split()
    syllables = []
    for word in str:
        count_sy = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                count_sy += 1
        syllables.append(count_sy)
    return len(syllables) == syllables.count(syllables[0])

text = input("Введите фразу: ")
if vinni_mf_puh(text):
    print('Парам пам-пам')
else:
    print('Пам парам')
