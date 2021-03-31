import nltk
from nltk.tag.stanford import StanfordNERTagger
#st = StanfordNERTagger('stanford-ner/english.all.3class.distsim.crf.ser.gz',
#                       'stanford-ner/stanford-ner.jar')
st = StanfordNERTagger('/Users/xaviernavarro/PycharmProjects/Speech2Text/assets/english.all.3class.distsim.crf.ser',
                       '/Users/xaviernavarro/PycharmProjects/Speech2Text/assets/stanford-ner-2017-06-09/stanford-ner.jar')
text = """Xavier beat Daniel up and then went to Walmart and paid with BitCoin"""

for sent in nltk.sent_tokenize(text):
    tokens = nltk.tokenize.word_tokenize(sent)
    tags = st.tag(tokens)
    for tag in tags:
        if tag[1]=='PERSON':
            print (tag)
