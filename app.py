from matplotlib import image
from sklearn.model_selection import train_test_split
import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle
from PIL import Image
from sympy import im
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


data=pd.read_csv('HousePrices_HalfMil.csv')
data.rename(columns={'White Marble':'white_marble','Black Marble':'black_marble',
       'Indian Marble':'indian_marble','Glass Doors':'glass_door', 'Swiming Pool':'swiming_pool'},inplace=True)
X=data.drop(['Prices'],axis=1)
y=data['Prices']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)
model=LinearRegression()
model.fit(X_train,y_train)



image=Image.open('istockphoto.jpg')

def main():
    st.title("House price predicton ")

    html_temp = """
    <div style ="background-color:Purple;padding:13px">
    <h1 style ="color:MediumSeaGreen;text-align:center;"> Check the house price prediction the below  ML App </h1>
    </div>
   
    
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    st.image(image,caption="Check the house price")



    Area=st.slider("Enter body mass index",1,249,1)
    Garage=st.selectbox("your Garage",["1","2","3"])
    FirePlace=st.selectbox("your FirePlace",["0","1","2","3","4"])
    Baths=st.selectbox("your Baths",["1","2","3","4","5"])
    white_marble=st.selectbox("your white_marble yes=1,or no=0",["1","0"])
    black_marble=st.selectbox("your black_marble yes=1,or no=0",["1","0"])
    indian_marble=st.selectbox("your indian_marble yes=1,or no=0",["1","0"])
    Floors=st.selectbox("Enter Floors ",["1","0"])
    City=st.selectbox("Enter city bangelore=3,hyd=2,dehli=1",["1","2","3"])
    Solar=st.selectbox("Enter Solar ",["1","0"])
    Electric=st.selectbox("Enter Electric ",["1","0"])
    Fiber=st.selectbox("Enter Fiber ",["1","0"])
    glass_door=st.selectbox("Enter glass_door ",["1","0"])
    swiming_pool=st.selectbox("Enter swiming_pool ",["1","0"])
    Garden=st.selectbox("Enter Garden ",["1","0"])
    result=' '
    
    
    
    if st.button("Predict"):
        result=model.predict([[Area,Garage,FirePlace,Baths,white_marble,black_marble,indian_marble,Floors,City,Solar,Electric,Fiber,glass_door,swiming_pool,Garden]])
    
    st.success('The house price is{}'.format(result[0],2))

     
    



if __name__=='__main__':
    main()
