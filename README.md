Text Summarization

Text Summarization is one of application of Natural Language Processing. The intention is to create a coherent and fluent summary having only the main points outlined in the document.


Automatic text summarization
•	Extractive text summarization
•	Abstractive text summarization


Extractive Text Summarization - The extractive text summarization technique involves pulling keyphrases from the source document and combining them to make a summary. All sentences in the summary are from the actual paragraphs itself. Only important sentences are included in the summary.


•	Genism Summarization

Gensim python package helps in getting the extractive summarization.

from gensim.summarization.summarizer import summarize

text = “””Rory McIlroy is off to a good start at the Scottish Open. He's hoping for a good finish, too, after missing the cut at the Irish Open.McIlroy shot a course record 7-under-par 64 at Royal Aberdeen on Thursday, and he was actually the second player to better the old mark -- Sweden's Kristoffer Broberg had earlier fired a 65.McIlroy carded eight birdies and one bogey in windy, chilly conditions."Going out this morning in these conditions I thought anything in the 60s would be a good score, so to shoot something better than that is pleasing," McIlroy was quoted as saying by the European Tour's website.A win Sunday would be the perfect way for former No. 1 McIlroy to prepare for the British Open, which starts next week at Royal Liverpool. He won the last of his two majors in 2012."Everything was pretty much on," McIlroy said. "I controlled my ball flight really well, which is the key to me playing well in these conditions and on these courses."I've been working the last 10 days on keeping the ball down, hitting easy shots and taking spin off it, and I went out there today and really trusted what I practiced."Last year Phil Mickelson used the Scottish Open at Castle Stuart as the springboard to his British Open title and his 68 leaves him well within touching distance of McIlroy.Mickelson needs a jolt of confidence given that 'Lefty' has slipped outside the top 10 in the rankings and hasn't finished in the top 10 on the PGA Tour this season."I thought it was tough conditions," Mickelson said in an audio interview posted on the European Tour's website. "I was surprised to see some low scores out there because it didn't seem like it was playing easy, and the wind was pretty strong."I felt like I played well and had a good putting day. It was a good day."Last year's U.S. Open champion, Justin Rose, was tied for 13th with a 69 but Jonas Blixt -- who tied for second at the Masters -- was well adrift following a 74.”””

print(summarize(text))
{This is not included as part of the code}



Fuzzy Logic

{Attached pdf paper is used for building fuzzy model}

Fuzzy logic has eight – Nine features calculated in fsummary.py file. Fuzzy rules are captures in rules.py and defuzzification steps are captured in defuzzification.py.


Input – Content, Title, n
Content  summarization paragraph
Title  Title for the paragraph
N  What percentage of the total paragraph’s len is expected in summary (Default = 0.2 (20%))
        
Content = """Rory McIlroy is off to a good start at the Scottish Open. He's hoping for a good finish, too, after missing the cut at the Irish Open.McIlroy shot a course record 7-under-par 64 at Royal Aberdeen on Thursday, and he was actually the second player to better the old mark -- Sweden's Kristoffer Broberg had earlier fired a 65.McIlroy carded eight birdies and one bogey in windy, chilly conditions."Going out this morning in these conditions I thought anything in the 60s would be a good score, so to shoot something better than that is pleasing," McIlroy was quoted as saying by the European Tour's website.A win Sunday would be the perfect way for former No. 1 McIlroy to prepare for the British Open, which starts next week at Royal Liverpool. He won the last of his two majors in 2012."Everything was pretty much on," McIlroy said. "I controlled my ball flight really well, which is the key to me playing well in these conditions and on these courses."I've been working the last 10 days on keeping the ball down, hitting easy shots and taking spin off it, and I went out there today and really trusted what I practiced."Last year Phil Mickelson used the Scottish Open at Castle Stuart as the springboard to his British Open title and his 68 leaves him well within touching distance of McIlroy.Mickelson needs a jolt of confidence given that 'Lefty' has slipped outside the top 10 in the rankings and hasn't finished in the top 10 on the PGA Tour this season."I thought it was tough conditions," Mickelson said in an audio interview posted on the European Tour's website. "I was surprised to see some low scores out there because it didn't seem like it was playing easy, and the wind was pretty strong."I felt like I played well and had a good putting day. It was a good day."Last year's U.S. Open champion, Justin Rose, was tied for 13th with a 69 but Jonas Blixt -- who tied for second at the Masters -- was well adrift following a 74."""

title = " Rory McIlroy Journey Story"

fuzzy = fuzzySummarization(Content,title,0.002)

fuzzy.execute()

print(fuzzy.summary)

TextRank


It is similar to webpage ranking. Top ranked sentences are included in the summary. Ranking to the sentences are given based on the node graph.
{Same content}


model = Summary()
Summarized = model.extractive(Content,n)
n  percentage value
print(Summarized)


Flask.
Python files are invoked from flask application (run.py). It has rough Upload html file to upload content and it responds with summarization along with the technique name.

Steps to run the code.
•	Python run.py
•	Html file opens up
•	Paste the content Text
•	Submit
•	A json with different techniques summarizations are displayed



Abstractive text summarization


The abstraction technique entails paraphrasing and shortening parts of the source document. When abstraction is applied for text summarization in deep learning problems, it can overcome the grammar inconsistencies of the extractive method.


Transformers pipeline is used for abstractive text summarization. 
from transformers import pipeline
summarization = pipeline("summarization")


summary_text = summarization(original_text)[0]['summary_text']

Original_text is the content here



The pre-trained T5 Model can also be used for abstractive text summarization. T5-base is used (t5-base is used, there is t5-large as well). It’s a torch text-to-text transformer.
Article is the content here

inputs = tokenizer.encode("summarize: " + article, return_tensors="pt", max_length=512, truncation=True)

print(tokenizer.decode(outputs[0]))





