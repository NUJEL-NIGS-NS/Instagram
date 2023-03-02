#Import library
import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import *
import matplotlib.pyplot as plt
import datetime as dt


#Data import
url=https://raw.githubusercontent.com/NUJEL-NIGS-NS/Instagram/master/files/dfbiotique.csv
df = pd.read_csv(url,index_col=0)
#hash tag list
hlist=[]
def edit(x):
    return x[2:(len(x)-1)]
for i in df['Hashtags']:
    j=list(map(edit,i.strip("[]").split(",")))
    hlist.extend(j)
hstr=""
for i in hlist:
    hstr+=" "+i









with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

st.title("biotique_world Instagram Analysis")
st.set_option('deprecation.showPyplotGlobalUse', False)
#first column
lf,rt=st.columns((4,2))

with lf:
    #world cloud
    st.header("_Top Hashtags Used_")
    wordcloud = WordCloud(max_font_size=100, max_words=100,colormap='Dark2', background_color='white').generate(hstr)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot()
with rt:
    # hashtag count
    hlists = list(set(i for i in hlist))
    hashn = []
    for i in hlists:
        c = hlist.count(i)
        hashn.append([i, c])
    hashn = sorted(hashn, key=lambda x: x[1], reverse=True)
    dfh = pd.DataFrame(hashn, columns=["HashTag", "Count"])
    st.dataframe(dfh)



#date time formating
#bar chart

st.title("_Like distribution according to Year_")

df["date"]=pd.to_datetime(df["date"],infer_datetime_format=True)
df["timestamp"]=pd.to_datetime(df["timestamp"],infer_datetime_format=True)


df.sort_values(by='date', inplace = True)
df['year']=df['date'].dt.year
df['month']=df['date'].dt.month
fig = px.bar(df, x="month", y="likesCount",color="year",barmode="group", title='Likes',facet_col="year")
st.plotly_chart(fig,use_container_width=True)




#time  plot according to date

lf,rt=st.columns((2,2))
with lf:
    sd=st.date_input("Starting Date",value=dt.date(2014, 4, 16),min_value=dt.date(2014, 4, 7),max_value=dt.date(2023, 2, 28))
    st.write(sd)
with rt:
    ed=st.date_input("End Date",value=dt.date(2023, 2, 28),min_value=sd,max_value=dt.date(2023, 2, 28))
    st.write(ed)

mask = (df['date'].dt.date >= sd) & (df['date'].dt.date <= ed)
df2 = df.loc[mask]
#for dataframe
lf,rt=st.columns((4,2))
with lf:
    df2["day"]=df2["timestamp"].dt.strftime("%A")
    st.dataframe(df2[["Hashtags","url","commentsCount","likesCount","timestamp","day"]])#dataframe according to the period
with rt:
    l, r = st.columns((2, 2))
    with l:
        d_l=[]
        like = round(df2["likesCount"].mean(), 2)
        comment = round(df2["commentsCount"].mean(), 2)
        st.metric(label="Average Likes ", value=like, delta="{} comments".format(comment))
        # for monday

        df21 = df2.loc[df2['day'] == "Monday"]
        like = round(df21["likesCount"].mean(), 2)
        comment = round(df21["commentsCount"].mean(), 2)
        st.metric(label="Monday", value=like, delta="{} comments".format(comment))
        d_l.append(["Monday",like,len(df21)])
        # for tuesday
        df22 = df2.loc[df2['day'] == "Tuesday"]
        like = round(df22["likesCount"].mean(), 2)
        comment = round(df22["commentsCount"].mean(), 2)
        st.metric(label="Tuesday", value=like, delta="{} comments".format(comment))
        d_l.append(["Tuesday", like,len(df22)])
        # for Wednesday
        df23 = df2.loc[df2['day'] == "Wednesday"]
        like = round(df23["likesCount"].mean(), 2)
        comment = round(df23["commentsCount"].mean(), 2)
        st.metric(label="Wednesday", value=like, delta="{} comments".format(comment))
        d_l.append(["Wednesday", like,len(df23)])
    with r:
       # for Thrusday
       df24 = df2.loc[df2['day'] == "Thursday"]
       like = round(df24["likesCount"].mean(), 2)
       comment = round(df24["commentsCount"].mean(), 2)
       st.metric(label="Thursday", value=like, delta="{} comments".format(comment))
       d_l.append(["Thursday", like,len(df24)])
       # for friday
       df25 = df2.loc[df2['day'] == "Friday"]
       like = round(df25["likesCount"].mean(), 2)
       comment = round(df25["commentsCount"].mean(), 2)
       st.metric(label="Friday", value=like, delta="{} comments".format(comment))
       d_l.append(["Friday", like,len(df25)])
       # for satarday
       df26 = df2.loc[df2['day'] == "Saturday"]
       like = round(df26["likesCount"].mean(), 2)
       comment = round(df26["commentsCount"].mean(), 2)
       st.metric(label="Saturday", value=like, delta="{} comments".format(comment))
       d_l.append(["Saturday", like,len(df26)])
       # for Sunday
       df27 = df2.loc[df2['day'] == "Sunday"]
       like = round(df27["likesCount"].mean(), 2)
       comment = round(df27["commentsCount"].mean(), 2)
       st.metric(label="Sunday", value=like, delta="{} comments".format(comment))
       d_l.append(["Sunday", like,len(df27)])
l,r=st.columns((2,2))
with l:
    # bar plot
    d_l = pd.DataFrame(d_l, columns=["day", "Like","Count"])

    fig = px.bar(d_l, x="day", y="Like", color="day",text="Count")
    st.plotly_chart(fig,use_container_width=True)
with r:
    # hash tag list
    hlist = []


    def edit(x):
        return x[2:(len(x) - 1)]


    for i in df2['Hashtags']:
        j = list(map(edit, i.strip("[]").split(",")))
        hlist.extend(j)
    hstr = ""
    for i in hlist:
        hstr += i
    # hashtag count
    hlists = list(set(i for i in hlist))
    hashn = []
    for i in hlists:
        c = hlist.count(i)
        hashn.append([i, c])
    hashn = sorted(hashn, key=lambda x: x[1], reverse=True)
    dfh = pd.DataFrame(hashn, columns=["HashTag", "Count"])
    df_pie = dfh.nlargest(10,"Count")
    fig_pie=px.pie(df_pie,names="HashTag",values="Count")
    st.plotly_chart(fig_pie,use_container_width=True)















