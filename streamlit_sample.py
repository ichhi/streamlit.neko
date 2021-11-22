# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:02:26 2021

@author: ichioka
"""

import streamlit as st
import time

st.title("初めてのstreamlit")
st.write("これから作品を作っていきます。")

text = st.text_input('あなたの名前を教えてください') 
'あなたの名前は，',text, 'です, '

condition = st.slider('あなたの今の調子は？',0, 100, 50)
'コンディション：',condition

option = st.selectbox( '好きな数字を教えてください', list(['1番','2番','3番','4番']) )
'あなたが選択したのは，',option,'です'

st.sidebar.write('プログレスバーの表示') 
'Start!' 

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100): 
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1) 
'Done!!!'

left_column, right_column = st.columns(2) 
button = left_column.button('右カラムに文字を表示') 
if button: 
    right_column.write('ここは右カラムです')

from PIL import Image
img=Image.open('7125.jpg')
st.image(img,caption='私の作品',use_column_width=True)