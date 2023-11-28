Assignment No 6
Name - Satyam Borude
Batch - B1
Roll No - 11
Assignment Title : Implement and visualize Dependency Parsing of Textual Input using Standford CoreNLP and Spacy library
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
multiline_text = """
Satyam is very rich person
He loves to drive Lambo
multiline_doc = nlp(multiline_text)
for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")
TOKEN: 
=====
token.tag_ = '_SP'
token.head.text = 'Satyam'
token.dep_ = 'dep'
TOKEN: Satyam
=====
token.tag_ = 'NNP'
token.head.text = 'is'
token.dep_ = 'nsubj'
TOKEN: is
=====
token.tag_ = 'VBZ'
token.head.text = 'is'
token.dep_ = 'ROOT'
TOKEN: very
=====
token.tag_ = 'RB'
token.head.text = 'rich'
token.dep_ = 'advmod'
TOKEN: rich
=====
token.tag_ = 'JJ'
token.head.text = 'person'
token.dep_ = 'amod'
TOKEN: person
=====
token.tag_ = 'NN'
token.head.text = 'is'
token.dep_ = 'attr'
TOKEN:
=====
token.tag_ = '_SP'
token.head.text = 'person'
token.dep_ = 'dep'
TOKEN: He
=====
token.tag_ = 'PRP'
token.head.text = 'loves'
token.dep_ = 'nsubj'
TOKEN: loves
=====
token.tag_ = 'VBZ'
token.head.text = 'person'
token.dep_ = 'relcl'
TOKEN: to
=====
token.tag_ = 'TO'
token.head.text = 'drive'
token.dep_ = 'aux'
TOKEN: drive
=====
token.tag_ = 'VB'
token.head.text = 'loves'
token.dep_ = 'xcomp'
TOKEN: Lambo
=====
token.tag_ = 'NNP'
token.head.text = 'drive'
token.dep_ = 'dobj'
TOKEN:
=====
token.tag_ = '_SP'
token.head.text = 'Lambo'
token.dep_ = 'dep'
Using the 'dep' visualizer
Serving on http://0.0.0.0:5000 ...
 
