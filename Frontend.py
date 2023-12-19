import pandas as pd
import streamlit as st
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import plotly.express as px
st.set_page_config(page_icon='https://www.memind.eu/wp-content/uploads/2022/01/sentiment-analysis-emotion-detection.jpg',page_title='Sentiment analysis')
st.title('Welcome to Sentiment Analysis \n 😄😥😏')
st.sidebar.image('https://thecxlead.b-cdn.net/wp-content/uploads/sites/5/2023/02/social-media-sentiment-analysis-featured-image-1280x720.png')
choice=st.sidebar.selectbox('Menu',('Home','Analysis'))
if(choice=='Home'):
    st.image('https://cdn-www.oktopost.com/blog/wp-content/uploads/2022/03/social-media-sentiment-analysis-blog-cover.png')
elif(choice=='Analysis'):
    a=st.text_input('Enter the link address')
    df=pd.read_csv(a)
    st.dataframe(df)
    b=st.text_input('Enter the column name')
    c=st.button('Analyze')
    if c:
        model= SentimentIntensityAnalyzer()
        df=pd.read_csv(a)
        df.dropna(inplace=True)
        t=df.loc[0:,b]
        list_t=[]
        for i in t:
            pred=model.polarity_scores(i)
            if(pred['compound']>0.5):
                list_t.append('Sentiment is positive')
            elif(pred['compound']<0.5):
                list_t.append('Sentiment is negative')
            else:
                list_t.append('Sentiment is neutral')
        data=pd.DataFrame()
        data['Column for analysis']=t
        data['Sentiment']=list_t
        st.header('Analysed  Successfully')
        st.dataframe(data)        
        chi=st.selectbox('Choose',('Pie Chart'))
        if(chi=='Pie Chart'):
            positive=(len(data[data['Sentiment']=='Sentiment is positive'])/len(data))*100
            negative=(len(data[data['Sentiment']=='Sentiment is negative'])/len(data))*100
            neutral=(len(data[data['Sentiment']=='Sentiment is neutral'])/len(data))*100
            fig=px.pie(values=[positive,negative,neutral],names=['positive','negative','neutral'])
            st.plotly_chart(fig)
        
            
        
        
