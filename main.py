import pymorphy3
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud
from matplotlib import pyplot as plt

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

text = 'Какой то текст'

def summarization(text, sent_number=3):
    sentences = sent_tokenize(text, language='russian')
    stop_words = set(stopwords.words('russian'))
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    words = [word for word in words if word not in stop_words]
    morph = pymorphy3.MorphAnalyzer()
    words = [morph.parse(word)[0].normal_form for word in words]
    freq_dist = FreqDist(words)
    sentence_scores = {}

    for i, sentence in enumerate(sentences):
        sentence_words = word_tokenize(sentence.lower())
        sentence_score = sum([freq_dist[word] for word in sentence_words if word in freq_dist])

        sentence_scores[i] = sentence_score
    sorted_scores = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    selected_sentences = sorted_scores[:1]
    selected_sentences = sorted(selected_sentences)

    # Формируем суммаризацию
    summary = ' '.join([sentences[i] for i, _ in selected_sentences])
    return summary

summarization(text)
