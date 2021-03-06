import sys
import nltk

from analysis.engine import Engine
from analysis.morpheme import Morpheme

for dep in ["vader_lexicon", "punkt", "brown"]: nltk.download(dep)

class Jint:
  def sentiment(self, data):
    return Engine().analyze_sentiment(data)

  def nouns(self, data):
    return Morpheme(data).noun_phrases
