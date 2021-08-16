import math
import re
from fuzzywuzzy import fuzz
from collections import Counter
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import spacy
from rake_nltk import Rake
#from text_analysis.common import models
from Fuzzy_Logic import models
#from .defuzzification_step import *
from Fuzzy_Logic import defuzzification_step as defuzz
#import text_analysis.summary.defuzzification_step as defuzz

# nlp = spacy.load("en_core_web_sm")

class fuzzySummarization():
    def __init__(self,content,title,n):
        self.content       = content
        self.n             = n
        self.sentences     = []
        self.words         = []
        self.title_feature = []
        self.slen_feature  = []
        self.sentence_pos  = []
        self.num_feature   = []
        self.similar_feature=[]
        self.nouns_feature = []
        self.term_feature  = []
        self.theme_feature = []
        self.defuzz_dict   = {}
        self.output        = []
        self.summary       = []
        self.Dict_scores   = {}
        self.title         = title
    
    def execute(self):
        #Preprocessing Step
        self.preprocessing()
        #Functions that require sentences at sentence level
        self.sentence_position()
        self.proper_nounsAndNumeric_feature()
        #Total_freq has a term frequency of a content
        total_freq =self.term_frequency(self.content)
        self.term_weight(total_freq)
        self.thematic_feature()
        
        
        #Functions that require sentences at word level 
        for sent in self.words:
            self.title_feature.append(self.title_word(sent))
            self.slen_feature.append(self.sentence_length(sent))
            self.similar_feature.append(self.similarity(sent))
        #Fuzzy logic scoring 
        for i in range(0,len(self.sentences)):
            self.defuzz_dict = {"title_word":self.title_feature[i],"sentence_length":self.slen_feature[i],"numerical_data":self.num_feature[i],"proper_noun":self.nouns_feature[i],"similarity":self.similar_feature[i],"term_weight":self.term_feature[i],"sentence_location":self.sentence_pos[i],"Thematic_feature":self.theme_feature[i]}
            #print(self.defuzz_dict)
        #Fuction is called to score a sentence
            self.output.append(defuzz.get_fuzzy_ranks([[self.defuzz_dict]]))
        #Dict_scores has sentences with it's scores
        for i in range(0,len(self.output)):
            self.Dict_scores.update({self.output[i]:self.sentences[i]})
        #percentage of the summary(Default 20% is considered)
        range_value = math.ceil(float(len(self.Dict_scores)*(self.n)))
        #Sentence selection and Assembly(High scored sentences are selected)
        for i in range(0,range_value):
            max_value =max(self.output)
            self.summary.append(self.Dict_scores[max_value])
            self.output.remove(max_value)
        self.summary=(" ".join(self.summary))
        #print(self.summary)
            
    #Function to preprocess the content
    def preprocessing(self):
        #Preprocessing
        self.content        = re.sub(r'[^\x00-\x7f]',r'',self.content)
        self.content        = ' '.join(self.content.strip().split('\n'))
        
        #Tokenizing the Content
        self.words, self.sentences = self.fuzzy_tokenizer(self.content)
        #Tokenizing the Title
        self.title, _title         = self.fuzzy_tokenizer(self.title)
        #print(self.sentences)
        
        
    #Function to tokenize at word and sentence level
    def fuzzy_tokenizer(self,content):
        sentences = self.sentence_tokenizer(content)
        words     = self.word_tokenizer(sentences)
        return words,sentences

        
    #Tokenize Sentences
    def sentence_tokenizer(self,content):
        #Breakdown of the Content in to sentences
        tokenizer   = PunktSentenceTokenizer()
        result      = tokenizer.tokenize(content)
        return result

    #Tokenize at word level
    def word_tokenizer(self,sentences):
        tokenized   = []
        #Stopwords
        stop_words  = stopwords.words('english')
        #Stemming
        stemmer = PorterStemmer()
        for sentence in sentences:
            words_sentence = []
            #Tokenize at word level
            words_sentence = word_tokenize(sentence)
            #Remove Stopwords and Stemming
            tokenized.append([stemmer.stem(word) for word in words_sentence if word not in stop_words])
        return tokenized

    #Function to compare sentences with title
    def title_word(self,sent):
        #print(sent)
        #print(self.title)
        count=0
        list1=[]
        for item in sent:
            if item in self.title[0] and item not in list1:
                list1.append(item)
                count = count+1
        #print(count)
        res=count/len(self.title[0])
        #print(len(self.title[0]))
        #print(res)
        return res
    
    #Function to find the length of the sentences 
    #(Combined 2 function-->function to find longest sentence and sentence lenghth function)
    def sentence_length(self,sent):
        sen_len=[]
        for i in self.words:
            sen_len.append(len(i))
        max_value = (max(sen_len))
        sent_len  = len(sent)
        res       = sent_len/max_value
        return res
    
    #Function to score according to it's position
    def sentence_position(self):
        for i in range(len(self.sentences),0,-1):
            self.sentence_pos.append(i/len(self.sentences))
            
    #Function for token matching using fuzzy wuzzy
    #(Used fuzzy wuzzy instead of cosine similarity)
    def similarity(self,sent):
            similar = fuzz.ratio(self.content,sent)
           
            return similar/100
        
    #Function to calcluate the frequency of term
    #(Same function used for calculating the term frequency of both content and single sentence )
    def term_frequency(self,string):
            frequency = {} 
            match_pattern = re.findall(r'\b[a-z]{3,15}\b', string)
             
            for word in match_pattern:
                count = frequency.get(word,0)
                frequency[word] = count + 1
                 
            frequency_list = frequency.keys()
            sum1=0 
            for words in frequency_list:
                sum1 = sum1+frequency[words]
            return sum1
        
    #Function to score a sentence with frequency of a term    
    def term_weight(self,total_freq):
        for i in range(len(self.sentences)):
            sent_freq  = self.term_frequency(self.sentences[i])
            res        = sent_freq/total_freq
            self.term_feature.append(res)
        return 
        
    #Function to calculate number of numeric and proper noun in a sentence
    #(I have joined proper_noun feature and numeric feature in one function itself and used spacy instead of using isdigit
    def proper_nounsAndNumeric_feature(self):
        model = models.get_model('en')
        for i in range(len(self.sentences)):
            doc    = model(self.sentences[i])
            count  = 0
            number = 0
            for token in doc:
                #print(token.text,token.pos_)
                if(token.pos_ == 'PROPN'):
                    count = count+1
                elif(token.pos_ == 'NUM'):
                    number = number+1
            self.nouns_feature.append(count/len(self.sentences[i]))
            self.num_feature.append(number/len(self.sentences[i]))
            
        return 
    #Function to calculate number of thematic words in a content and sentence
    def thematic_feature(self):
        r = Rake()
        #Thematic words of content
        r.extract_keywords_from_text(self.content)
        score_list = r.get_ranked_phrases_with_scores()
        doc_score=[]
        for i in range(0, len(score_list)):
            doc_score.append(score_list[i][0])
            thematic_doc=(len(doc_score))
        #Thematic words of each sentence   
        for i in range(len(self.sentences)):
            r.extract_keywords_from_text(self.sentences[i])
            sent_score_list = r.get_ranked_phrases_with_scores()
            res             = len(sent_score_list)/thematic_doc
            self.theme_feature.append(res)
        return 
    
        
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

# title = "Extractive summarization"
# fux = fuzzySummarization(Content,title,0.002)
# a=fux.execute()
# print(fux.summary)
