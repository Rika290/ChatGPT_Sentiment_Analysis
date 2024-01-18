Sentiment Analysis on ChatGPT tweets

ABOUT:
This project is based on Sentiment Analysis which is utilised by many companies around the world through reviews,feedbacks etc in order to gain insights and improve their business
- (1) VADER Sentiment Analysis :-
- VADER stands for Valence Aware Dictionary and Sentiment Reasoner, a sentiment analysis tool which helps in analysing texts and obtaining sentiment scores
-  Mainly used for analysing social media sentiment texts
- Can easily handle different texts

- (2) Data Source :- The data used for this analysis :- https://www.kaggle.com/datasets/charunisa/chatgpt-sentiment-analysis

STEPS:
- The dataset from the Kaggle page is loaded
- Number of rows are observed
- The module called SentimentIntensityAnalyzer is imported, make sure vaderSentiment is installed
- When the compound part of the polarity scores in the column containing tweets:
(a) is lesser than -0.5, then, it is considered as 'Negative';
(b) if it is greater than 0.5, then it is 'Positive';
(c) else, it is 'Neutral'
- Columns with tweets and sentiments are merged to one dataframe, and visualized using Seaborn
- From the graph plotted, it is observed that, neutral sentiment is more than others.

CONCLUSION:
- According to this analysis, we can infer that only few are against or does not support ChatGPT, whereas most of them are neutral.
