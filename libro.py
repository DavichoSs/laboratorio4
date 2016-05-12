from textblob import TextBlob

archivo=open('texto.txt','r')
contenido=archivo.readline()
text=contenido.replace(" ","")
blob = TextBlob(text)
blob.tags
blob.noun_phrases   

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
