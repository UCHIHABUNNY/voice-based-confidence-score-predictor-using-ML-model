#Project Description / Methodology  :

This project analyzes speaker confidence by converting speech into text and applying sentiment analysis using TextBlob.  
 The sentiment polarity is mapped to a confidence score.

#Limitations  :

The system estimates confidence based only on sentiment polarity of spoken text.
 It does not consider vocal tone, pitch, pauses, or speech rate, which may affect accuracy.

 Component	Type
Google Speech Recognition	---   Pre-trained model
TextBlob Sentiment	        ---   Pre-trained model
Confidence logic	        ---   Rule-based

This project uses Google’s pre-trained Speech Recognition model to convert speech into text and TextBlob’s pre-trained sentiment analysis model to determine sentiment polarity. These are combined with rule-based logic to estimate the speaker’s confidence level.

 #################################### Applying Logistic Regrresion  #################################################

 Initially, the system used rule-based confidence scoring. This was later enhanced using a Logistic Regression classifier trained on labeled speech text, enabling data-driven confidence prediction.”
                              Also our Your project does NOT need a dataset to run.
                                But it DOES need a dataset to learn
###Supervised ML###
#Binary classification#
1  →  Confident
0  →  Not confident
