# NLP Extractive Text Summarizer with PyMorphy3 & NLTK

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![NLTK](https://img.shields.io/badge/NLTK-3.8%2B-green.svg)](https://www.nltk.org/)
[![PyMorphy3](https://img.shields.io/badge/PyMorphy3-2.0%2B-orange.svg)](https://github.com/no-life-studio/pymorphy3)

An extractive text summarization and Natural Language Processing (NLP) pipeline designed for morphological analysis, lemmatization, and word frequency scoring on Russian natural language texts.

---

## 🚀 Key Features

* **Morphological Lemmatization**: Integrates `pymorphy3` for accurate grammatical normalization and inflection reduction.
* **Stopword Removal & Tokenization**: Language-aware tokenization using `NLTK` word and sentence tokenizers.
* **Frequency-Based Sentence Scoring**: Uses `FreqDist` probability distributions to calculate sentence significance vectors.
* **Chronological Reconstruction**: Preserves original narrative sequence when outputting top-ranked sentences.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **NLP Frameworks**: NLTK, PyMorphy3
* **Data Mining**: WordCloud, Matplotlib

---

## ⚙️ Configuration & Setup

### 1. Clone the repository
git clone https://github.com/DrRafael/nlp-text-summarizer-pymorphy.git
cd nlp-text-summarizer-pymorphy

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the summarizer
python main.py

---

**Author**: QA Automation Engineer & Python Developer
