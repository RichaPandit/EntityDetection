import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from bs4 import BeautifulSoup
import requests
import re
import sys
import os.path
from os import path

ny_bb = str(sys.argv[1])
mFilePath = str(sys.argv[2])

article = nlp(ny_bb)
len(article.ents)

labels = [x.label_ for x in article.ents]
Counter(labels)

items = [x.text for x in article.ents]
Counter(items).most_common(3)

sentences = [x for x in article.sents]

HTMLStr = displacy.render(nlp(str(sentences[0])), minify=True, style='ent')
if path.exists(mFilePath):
    Html_file=open(mFilePath, "a", newline='')
    Html_file.write('\n')
    Html_file.write(HTMLStr)
    Html_file.close()
else:
    Html_file= open(mFilePath,"w")
    Html_file.write(HTMLStr)
    Html_file.close()



