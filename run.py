from flask import Flask, render_template, request
from flask import jsonify
from TextRank import summary as summ
from Fuzzy_Logic import fsummary
import pandas as pd
import json

app = Flask(__name__)

#from flask import Flask, request, render_template

#app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def a():
    if request.method == 'GET':
        return render_template('upload.html')
    if request.method == 'POST':
        content=request.form['text']	
        print(content)
        #content = "ArcelorMittal has announced results for the three-month and six-month periods ended June 30, 2018. Commenting, Mr. Lakshmi N. Mittal, ArcelorMittal Chairman and CEO, said \"This is an encouraging set of results reflecting the structural improvements in both the global steel industry due to supply reform dynamics and within ArcelorMittal as a result of Action 2020. The significant improvement in our balance sheet and earnings outlook has been recognised by the main credit agencies and the Company has achieved its stated aim of regaining its investment grade credit rating. The outlook for the second half of the year is encouraging as we anticipate current favourable market conditions continuing and are well positioned to capitalise on this from our leadership position across many key markets. We believe improvements in underlying industry fundamentals are sustainable, although there is still more to be done to thoroughly address the issue of global overcapacity. We will retain a deleveraging bias, whilst also pursuing selective opportunities to strengthen the foundations of sustainable value creation.\" Highlights: Health and safety: LTIF rate of 0.71x in 2Q 2018; 1H 2018 LTIF of 0.67x vs. 0.78x 1H 2017 Operating income of $2.4 billion in 2Q 2018; 1H 2018 operating income of $3.9 billion, 32.5% higher YoY EBITDA of $3.1 billion in 2Q 2018, 22.3% higher vs. 1Q 2018; 1H 2018 EBITDA of $5.6 billion, 28.6% higher YoY Net income of $1.9 billion in 2Q 2018, 56.4% higher vs. 1Q 2018; 1H 2018 net income of $3.1 billion, +31.5% YoY Steel shipments of 21.8Mt in 2Q 2018, +1.8% vs. 1Q 2018; 1H 2018 steel shipments of 43.1Mt, up 1.3% YoY 2Q 2018 iron ore shipments of 14.6Mt, of which 10.0Mt shipped at market prices (+5.4% YoY) Gross debt of $13.5 billion as of June 30, 2018. Net debt decreased to $10.5 billion as of June 30, 2018, as compared to $11.1 billion as of March 31, 2018, despite further $1.2 billion working capital investment Industry leadership: ArcelorMittal's pioneering new installation at Gent, Belgium, to apply LanzaTech carbon capture and utilisation technology to convert carbon-containing gas from blast furnaces into bioethanol reflecting our position as the industry leader as well as the supplier-awards received from Honda, General Motors and Ford during 1H 2018; The Group's ability to leverage its R&D capabilities is exemplified through the launch of Steligence®, ArcelorMittal's new concept for the use of steel in construction, which will facilitate the next generation of high performance buildings and construction techniques and create a more sustainable life-cycle for buildings"
        #Fuzzy Summarization is triggered
        summarize=fsummary.fuzzySummarization(content,"steel India.",0.2)
        summarize.execute()
        Fuzzy_Summ =summarize.summary
        model = summ.Summary()
        #Textrank Algorithm is triggered for extractive summarization
        TextRank_summ = model.extractive(content,5)
        
        
        result = {
            "Extractive Summarization output(fuzzy)": Fuzzy_Summ,
            "Extractive Summarization output(TextRank)": TextRank_summ
            }
        return  json.dumps(result)
    
    else:
        
        return "Exception"
 
if __name__ == '__main__':
   app.run(debug = True)

