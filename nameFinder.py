import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')



def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]

def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

def ie_preprocess(document):
    document = ' '.join([i for i in document.split() if i not in stop])
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def extract_names(document):
    names = []
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    return names

string = """
Bitcoin is low-priced right now
Shortly after confirmation that Jack has made contact with the freighter, Jin watches and listens as Desmond delivers Charlie's warning, and ventures into the jungle to meet up with the rest of the camp. After reuniting with Sun, Jin decides to return to the beach with Jack rather than join Locke (Terry O'Quinn) at the barracks. Jin and Sun discuss what they will name their baby, and Jin suggest Ji Yeon. Sun insists it's too early. After a conversation with Kate, Sun decides to head to Locke's camp. In hopes of stopping this Juliet reveals Sun's medical condition, and the affair she had to Jin. Although angry at first, Jin realizes that he was not supportive of Sun and that he pushed her away, so he forgives her and promises that he will never leave her. Later, Sayid returns with the speedboat to take people to the boat. Jin and Sun go with the first group, taking Aaron with them. On the boat, they encounter Michael for the first time since he left the island. Upon discovering a bomb on the boat, Jin, Michael and Desmond attempt to disarm it. While their attempts manage to stall the bomb's detonation, Jin is left on the boat during the bomb's detonation. The freighter explodes and sinks beneath the ocean leading to Sun and the rest of the Oceanic 6 believing him to have died in the explosion.

At the Oceanic 6 conference when a Korean reporter asks Sun if Jin survived the crash, Sun looks very somber and pauses for a minute before replying that he did not. Sun later buys a controlling share of her father's company as retribution for, in her view, his hand in Jin's death. Sun names her daughter Ji Yeon as Jin had asked.

"""
print(set(extract_names(string)))
