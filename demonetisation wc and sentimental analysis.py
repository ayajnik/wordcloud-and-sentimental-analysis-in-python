print " \n Run by Ayush Yajnik."




#Import all the necessary libraries
from nltk.tokenize import RegexpTokenizer
import nltk
from nltk.corpus import sentiwordnet as swn
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Importing the pros, cons and stopwords file.
file1 = open("demonetization tweets.csv", "r")


#Using regular expressions form nltk
tokenizer = RegexpTokenizer(r'\w+')

#Reading the input files and converting them to lower case

conslower = file1.read().lower()


#Replacing the new line command with space ("\n" to " ")

consreplace = conslower.replace("\n", " ")


#Removing Punctuations and tokenizing

cons_read = tokenizer.tokenize(consreplace)



#Removing numerial data
numberspro = []
numberscon = []


for j in cons_read:
	if j.isdigit() == False:
		numberscon.append(j)

#Removing stopwords
cleanpro = []
cleancon = []

 
#Creating bigrams       
bigrammed_pro = list(nltk.bigrams(cleanpro))
bigrammed_cons = list(nltk.bigrams(cleancon))

#Creating a string of all the cleaned text
pro_data = " ".join(cleanpro)
con_data = " ".join(cleancon)

#Plotting a WordCloud of all the Cleaned Pro text
plt.figure()
wc = WordCloud(background_color="white", max_words=100)
wc.generate(pro_data)
wc.to_file('Pro.png')
plt.title("Pros Data - WordCloud")
plt.imshow(wc)
plt.axis('off')
plt.show()

#Plotting a WordCloud of all the Cleaned Cons text
plt.figure()
wc = WordCloud(background_color="white", max_words=100)
wc.generate(con_data)
wc.to_file('Pro.png')
plt.title("Cons Data - WordCloud")
plt.imshow(wc)
plt.axis('off')
plt.show()

#Sentiment Calculation
PosScore_Pro = 0
Negscore_Con = 0
PosScore_Con = 0
Negscore_Pro = 0

for i in cleanpro:
    try:
        sentiment_pos = swn.senti_synset(i + '.n.01').pos_score()
        PosScore_Pro += sentiment_pos
        sentiment_con = swn.senti_synset(i + '.n.01').neg_score()
        Negscore_Pro += sentiment_con
    except:
        try:
            sentiment_pos = swn.senti_synset(i + '.v.01').pos_score()
            PosScore_Pro += sentiment_pos
            sentiment_con = swn.senti_synset(i + '.v.01').neg_score()
            Negscore_Pro += sentiment_con
        except:
            try:
                sentiment_pos = swn.senti_synset(i + '.a.01').pos_score()
                PosScore_Pro += sentiment_pos
                sentiment_con = swn.senti_synset(i + '.a.01').neg_score()
                Negscore_Pro += sentiment_con
            except:
                try:
                    sentiment_pos = swn.senti_synset(i + '.s.01').pos_score()
                    PosScore_Pro += sentiment_pos
                    sentiment_con = swn.senti_synset(i + '.s.01').neg_score()
                    Negscore_Pro += sentiment_con
                except:
                    try:
                        sentiment_pos = swn.senti_synset(i + '.r.01').pos_score()
                        PosScore_Pro += sentiment_pos
                        sentiment_con = swn.senti_synset(i + '.r.01').neg_score()
                        Negscore_Pro += sentiment_con
                    except:
                        continue
                        
for j in cleancon:
    try:
        sentiment_pos = swn.senti_synset(j + '.n.05').pos_score()
        PosScore_Con += sentiment_pos
        sentiment_con = swn.senti_synset(j + '.n.05').neg_score()
        Negscore_Con += sentiment_con
    except:
        try:
            sentiment_pos = swn.senti_synset(j + '.v.05').pos_score()
            PosScore_Con += sentiment_pos
            sentiment_con = swn.senti_synset(j + '.v.05').neg_score()
            Negscore_Con += sentiment_con
        except:
            try:
                sentiment_pos = swn.senti_synset(j + '.a.05').pos_score()
                PosScore_Pro += sentiment_pos
                sentiment_con = swn.senti_synset(j + '.a.05').neg_score()
                Negscore_Con += sentiment_con
            except:
                try:
                    sentiment_pos = swn.senti_synset(j + '.s.05').pos_score()
                    PosScore_Con += sentiment_pos
                    sentiment_con = swn.senti_synset(j + '.s.05').neg_score()
                    Negscore_Con += sentiment_con
                except:
                    try:
                        sentiment_pos = swn.senti_synset(j + '.r.05').pos_score()
                        PosScore_Con += sentiment_pos
                        sentiment_con = swn.senti_synset(j + '.r.05').neg_score()
                        Negscore_Con += sentiment_con
                    except:
                        continue

print "---------------------------"
print "Total of Positive Score of all the Pros are:", PosScore_Pro
print "Total of Negative Score of all the Pros are:", Negscore_Pro
print "---------------------------"
print "Total of Positive Score of all the Cons are:", PosScore_Con
print "Total of Negative Score of all the Cons are:", Negscore_Con
print "---------------------------"