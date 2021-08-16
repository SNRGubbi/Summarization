import math
import nltk
import re
import networkx as nx
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.corpus import brown, stopwords
from nltk.cluster.util import cosine_distance
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

class Summary:
	
	def extractive(self, content, n):
		content = re.sub(r'[^\x00-\x7f]',r'', content)
		document = ' '.join(content.strip().split('\n'))
		sentence_tokenizer = PunktSentenceTokenizer()
		sentences = sentence_tokenizer.tokenize(document)
		text_sentence_count = len(sentences)
		summary_length = math.ceil(float(text_sentence_count))
		sentence_count = float(n)*0.01
		number_of_sentences_in_summary = math.ceil(text_sentence_count*sentence_count)
		c = CountVectorizer()
#		bow_array = c.fit_transform([sentences[0]])
#		bow_array.toarray()
		c = CountVectorizer()
		bow_matrix = c.fit_transform(sentences)
		normalized_matrix = TfidfTransformer().fit_transform(bow_matrix)
        
		similarity_graph = normalized_matrix * normalized_matrix.T
		similarity_graph.toarray()
		nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
		scores = nx.pagerank(nx_graph)
        
		ranked = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
		i = 0
		extracted_sentences = []
		while i < number_of_sentences_in_summary:
			extracted_sentences.append(ranked[i][1])
			i = i + 1
		extracted_summary = ''.join(extracted_sentences)
			#print("Extracted Summary")
		print(extracted_summary)
		return extracted_summary
    
	def tokenize_sentences(self, content):
		document = ' '.join(content.strip().split('\n'))
		return document
	def bag_of_words(self, sentence):
		return Counter(word.lower().strip('.,') for word in sentence.split(' '))

# Content = """Rory McIlroy is off to a good start at the Scottish Open. He's hoping for a good finish, too, after missing the cut at the Irish Open.

# McIlroy shot a course record 7-under-par 64 at Royal Aberdeen on Thursday, and he was actually the second player to better the old mark -- Sweden's Kristoffer Broberg had earlier fired a 65.

# McIlroy carded eight birdies and one bogey in windy, chilly conditions.

# "Going out this morning in these conditions I thought anything in the 60s would be a good score, so to shoot something better than that is pleasing," McIlroy was quoted as saying by the European Tour's website.

# A win Sunday would be the perfect way for former No. 1 McIlroy to prepare for the British Open, which starts next week at Royal Liverpool. He won the last of his two majors in 2012.

# "Everything was pretty much on," McIlroy said. "I controlled my ball flight really well, which is the key to me playing well in these conditions and on these courses.

# "I've been working the last 10 days on keeping the ball down, hitting easy shots and taking spin off it, and I went out there today and really trusted what I practiced."

# Last year Phil Mickelson used the Scottish Open at Castle Stuart as the springboard to his British Open title and his 68 leaves him well within touching distance of McIlroy.

# Mickelson needs a jolt of confidence given that 'Lefty' has slipped outside the top 10 in the rankings and hasn't finished in the top 10 on the PGA Tour this season.

# "I thought it was tough conditions," Mickelson said in an audio interview posted on the European Tour's website. "I was surprised to see some low scores out there because it didn't seem like it was playing easy, and the wind was pretty strong.

# "I felt like I played well and had a good putting day. It was a good day."

# Last year's U.S. Open champion, Justin Rose, was tied for 13th with a 69 but Jonas Blixt -- who tied for second at the Masters -- was well adrift following a 74."""

# model = Summary()
# a = model.extractive(Content,5)
# print(a)
