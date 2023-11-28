"""
Assignment No 4
Name - Borude Satyam
Batch - B1
Roll No - 11
Assignment Title : Generating The N Gram Model using NLTK

"""

from nltk import ngrams
from nltk.util import ngrams

#unigram model
n = 1
sentence = 'NLTK is Natural Language Tool Kit. It is used to build python programming. It helps to work with human languages data. It gives a very easy user interface.'
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)

    
#bigram model
n = 2
sentence = 'NLTK is Natural Language Tool Kit. It is used to build python programming. It helps to work with human languages data. It gives a very easy user interface.'
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)


#trigram model
n = 3
sentence = 'NLTK is Natural Language Tool Kit. It is used to build python programming. It helps to work with human languages data. It gives a very easy user interface.'
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)


#using text file input

from nltk import ngrams
file = open("Num.txt")
for i in file.readlines():
    cumulative = i
    sentences = i.split(".")
    counter = 0
    for sentence in sentences:
        print("For sentence", counter + 1, ", trigrams are: ")
        trigrams = ngrams(sentence.split(" "), 3)
        for grams in trigrams:
            print(grams)
        counter += 1
        print()

# OUTPUT -

"""
('NLTK',)
('is',)
('Natural',)
('Language',)
('Tool',)
('Kit.',)
('It',)
('is',)
('used',)
('to',)
('build',)
('python',)
('programming.',)
('It',)
('helps',)
('to',)
('work',)
('with',)
('human',)
('languages',)
('data.',)
('It',)
('gives',)
('a',)
('very',)
('easy',)
('user',)
('interface.',)
('NLTK', 'is')
('is', 'Natural')
('Natural', 'Language')
('Language', 'Tool')
('Tool', 'Kit.')
('Kit.', 'It')
('It', 'is')
('is', 'used')
('used', 'to')
('to', 'build')
('build', 'python')
('python', 'programming.')
('programming.', 'It')
('It', 'helps')
('helps', 'to')
('to', 'work')
('work', 'with')
('with', 'human')
('human', 'languages')
('languages', 'data.')
('data.', 'It')
('It', 'gives')
('gives', 'a')
('a', 'very')
('very', 'easy')
('easy', 'user')
('user', 'interface.')
('NLTK', 'is', 'Natural')
('is', 'Natural', 'Language')
('Natural', 'Language', 'Tool')
('Language', 'Tool', 'Kit.')
('Tool', 'Kit.', 'It')
('Kit.', 'It', 'is')
('It', 'is', 'used')
('is', 'used', 'to')
('used', 'to', 'build')
('to', 'build', 'python')
('build', 'python', 'programming.')
('python', 'programming.', 'It')
('programming.', 'It', 'helps')
('It', 'helps', 'to')
('helps', 'to', 'work')
('to', 'work', 'with')
('work', 'with', 'human')
('with', 'human', 'languages')
('human', 'languages', 'data.')
('languages', 'data.', 'It')
('data.', 'It', 'gives')
('It', 'gives', 'a')
('gives', 'a', 'very')
('a', 'very', 'easy')
('very', 'easy', 'user')
('easy', 'user', 'interface.')
For sentence 1 , trigrams are:

For sentence 1 , trigrams are:
('Your', 'smile', 'makes')
('smile', 'makes', 'me')
('makes', 'me', 'smile')
('me', 'smile', 'Your')
('smile', 'Your', 'laugh')
('Your', 'laugh', 'makes')
('laugh', 'makes', 'me')
('makes', 'me', 'laugh')
('me', 'laugh', 'Your')
('laugh', 'Your', 'eyes')
('Your', 'eyes', 'are')
('eyes', 'are', 'enchanting')
('are', 'enchanting', 'You')
('enchanting', 'You', 'make')
('You', 'make', 'my')
('make', 'my', 'thoughts')
('my', 'thoughts', 'seem')
('thoughts', 'seem', 'daft')
('seem', 'daft', 'Since')
('daft', 'Since', 'the')
('Since', 'the', 'day')
('the', 'day', 'I')
('day', 'I', 'first')
('I', 'first', 'laid')
('first', 'laid', 'eyes')
('laid', 'eyes', 'on')
('eyes', 'on', 'you')
('on', 'you', 'My')
('you', 'My', 'feelings')
('My', 'feelings', 'grew')
('feelings', 'grew', 'and')
('grew', 'and', 'grew')
('and', 'grew', 'In')
('grew', 'In', 'that')
('In', 'that', 'first')
('that', 'first', 'conversation')
('first', 'conversation', 'my')
('conversation', 'my', 'knees')
('my', 'knees', 'clicked')
('knees', 'clicked', 'and')
('clicked', 'and', 'clacked')
('and', 'clacked', 'And')
('clacked', 'And', 'those')
('And', 'those', 'butterflies')
('those', 'butterflies', 'flipped')
('butterflies', 'flipped', 'and')
('flipped', 'and', 'flapped')
('and', 'flapped', 'And')
('flapped', 'And', 'as')
('And', 'as', 'I')
('as', 'I', 'spill')
('I', 'spill', 'these')
('spill', 'these', 'simple')
('these', 'simple', 'rhymes')
('simple', 'rhymes', 'My')
('rhymes', 'My', 'mind')
('My', 'mind', 'goes')
('mind', 'goes', 'over')
('goes', 'over', 'time')
('over', 'time', 'and')
('time', 'and', 'time')
('and', 'time', 'I')
('time', 'I', 'have')
('I', 'have', 'a')
('have', 'a', 'crush,')
('a', 'crush,', 'a')
('crush,', 'a', 'little')
('a', 'little', 'teenage')
('little', 'teenage', 'crush')
('teenage', 'crush', 'I')
('crush', 'I', 'dont')
('I', 'dont', 'know')
('dont', 'know', 'what')
('know', 'what', 'to')
('what', 'to', 'do,')
('to', 'do,', 'about')
('do,', 'about', 'this')
('about', 'this', 'lovely')
('this', 'lovely', 'little')
('lovely', 'little', 'crush')
('little', 'crush', '')
"""