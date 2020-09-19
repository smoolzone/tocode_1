from collections import defaultdict

#with open('/Users/smool/Documents/alan wats.rtf') as wordsfile:
    #words = [line.strip().lower() for line in wordsfile]

words = ['dad', 'add', 'rome', 'bye']


anagrams = defaultdict(list)

for word in words:
    key = ''.join(sorted(word))
    anagrams[key].append(word)


#for key, value in anagrams.items():
    #if len(value) > 1:
     #   print(value)

print(anagrams)