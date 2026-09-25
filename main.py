import nltk
import pymorphy3
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize

# Ensure required NLTK resources are available
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)


def summarize_text(text: str, sent_number: int = 3) -> str:
    """Performs extractive text summarization using word frequency distribution and morphological analysis.

    Args:
        text (str): Input raw text.
        sent_number (int): Number of top scored sentences to include in summary.

    Returns:
        str: Extracted key sentences forming the text summary.
    """
    if not text.strip():
        return ""

    sentences = sent_tokenize(text, language='russian')
    if len(sentences) <= sent_number:
        return text

    stop_words = set(stopwords.words('russian'))
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # Lemmatize words to normal form for accurate frequency scoring
    morph = pymorphy3.MorphAnalyzer()
    lemmatized_words = [morph.parse(word)[0].normal_form for word in words]

    freq_dist = FreqDist(lemmatized_words)
    sentence_scores = {}

    for i, sentence in enumerate(sentences):
        sentence_words = word_tokenize(sentence.lower())
        sentence_lemmas = [morph.parse(w)[0].normal_form for w in sentence_words if w.isalpha()]
        score = sum(freq_dist[lemma] for lemma in sentence_lemmas if lemma in freq_dist)
        sentence_scores[i] = score

    # Select top N highest-scoring sentences and sort them chronologically
    sorted_scores = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    selected_indices = sorted([index for index, _ in sorted_scores[:sent_number]])

    summary = ' '.join([sentences[i] for i in selected_indices])
    return summary


if __name__ == "__main__":
    sample_text = (
        "Машинное обучение — это область искусственного интеллекта, которая изучает методы построения алгоритмов, "
        "способных обучаться. Способность обучаться является важнейшим свойством систем искусственного интеллекта. "
        "Алгоритмы машинного обучения используются во множестве сфер, включая распознавание речи, компьютерное зрение и NLP. "
        "Обработка естественного языка позволяет компьютерам понимать тексты на человеческих языках."
    )

    result = summarize_text(sample_text, sent_number=2)
    print("--- Extractive Summary Output ---")
    print(result)
