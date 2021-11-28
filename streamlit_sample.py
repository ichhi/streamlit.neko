# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:02:26 2021

@author: ichioka
"""

import streamlit as st
import time

st.title("やることリスト")

st.sidebar.write('プログレスバーの表示') 
'Start!' 

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100): 
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1) 
'Done!!!'
    
import datetime
from dateutil.relativedelta import relativedelta
from datetime import date

left_column,right_column = st.columns(2)  


def main():
    homework1 = st.date_input('課題1の提出期限を書いてください。',
                             min_value=date.today(),
                             value=date.today(),
                             )
    left_column.write(homework1)   
    
    

    kyou1 = datetime.date.today()            
    if homework1 <= kyou1 + relativedelta(days=+1):
        right_column.write('急いで課題1に取り組みましょう!!!')
    elif homework1 <= kyou1 + relativedelta(weeks=+1):
        right_column.write('そろそろ課題1に取り組みましょう!!')
    else :
        right_column.write('計画的に課題1を勧めましょう！')
           
if __name__ == '__main__':
    main() 
    
@st.cache(allow_output_mutation=True)
def cache_lst1():
    lst1 = []
    return lst1
lst1 = cache_lst1()

input = st.text_input('課題1の内容')


if st.checkbox('delete1'):
    delete1 = st.selectbox('課題1の削除する要素を選択して下さい', options=lst1)
    if st.button('Delete1'):
        lst1.remove(delete1)
        st.success(f'Delete1 : {delete1}')

if st.checkbox('change1'):
    change1_from = st.selectbox('課題1の変更する要素を選択して下さい', options=lst1)
    change1_index = lst1.index(change1_from)
    change1_to = st.text_input('どのように課題1を変更しますか')
    if st.button('Change1'):
        lst1.remove(change1_from)
        lst1.insert(change1_index, change1_to)
        st.success(f'Change1 {change1_from} to {change1_to}')
        
st.table(lst1)



progress1 = st.slider('課題1の進捗は？',0, 100, 50)
'課題1進捗：',progress1


left_column,right_column = st.columns(2)  


def main():
    homework2 = st.date_input('課題2の提出期限を書いてください。',
                             min_value=date.today(),
                             value=date.today(),
                             )
    left_column.write(homework2)   
    
    

    kyou2 = datetime.date.today()            
    if homework2 <= kyou2 + relativedelta(days=+1):
        right_column.write('急いで課題2に取り組みましょう!!!')
    elif homework2 <= kyou2 + relativedelta(weeks=+1):
        right_column.write('そろそろ課題2に取り組みましょう!!')
    else :
        right_column.write('計画的に課題2を勧めましょう！')
           
if __name__ == '__main__':
    main() 
    
@st.cache(allow_output_mutation=True)
def cache_lst2():
    lst2 = []
    return lst2
lst2 = cache_lst2()

input = st.text_input('課題2の内容')


if st.checkbox('delete2'):
    delete2 = st.selectbox('課題2で削除する要素を選択して下さい', options=lst2)
    if st.button('Delete2'):
        lst2.remove(delete2)
        st.success(f'Delete2 : {delete2}')

if st.checkbox('change2'):
    change2_from = st.selectbox('変更する課題2の要素を選択して下さい', options=lst2)
    change2_index = lst2.index(change2_from)
    change2_to = st.text_input('課題2をどのように変更しますか')
    if st.button('Change2'):
        lst2.remove(change2_from)
        lst2.insert(change2_index, change2_to)
        st.success(f' {change2_from} to {change2_to}')
        
st.table(lst2)



progress2 = st.slider('課題2の進捗は？',0, 100, 50)
'課題2進捗：',progress2


left_column,right_column = st.columns(2)  


def main():
    homework3 = st.date_input('課題3の提出期限を書いてください。',
                             min_value=date.today(),
                             value=date.today(),
                             )
    left_column.write(homework3)   
    
    

    kyou3 = datetime.date.today()            
    if homework3 <= kyou3 + relativedelta(days=+1):
        right_column.write('急いで課題3に取り組みましょう!!!')
    elif homework3 <= kyou3 + relativedelta(weeks=+1):
        right_column.write('そろそろ課題3に取り組みましょう!!')
    else :
        right_column.write('計画的に課題3を勧めましょう！')
           
if __name__ == '__main__':
    main() 
    
@st.cache(allow_output_mutation=True)
def cache_lst3():
    lst3 = []
    return lst3
lst3 = cache_lst3()

input = st.text_input('課題3の内容')


if st.checkbox('delete3'):
    delete3 = st.selectbox('削除する課題3の要素を選択して下さい', options=lst3)
    if st.button('Delete3'):
        lst3.remove(delete3)
        st.success(f'Delete3 : {delete3}')

if st.checkbox('change3'):
    change3_from = st.selectbox('変更する課題3の要素を選択して下さい', options=lst3)
    change3_index = lst3.index(change3_from)
    change3_to = st.text_input('課題3をどのように変更しますか')
    if st.button('Change'):
        lst3.remove(change3_from)
        lst3.insert(change3_index, change3_to)
        st.success(f'Change {change3_from} to {change3_to}')
        
st.table(lst3)



progress = st.slider('課題3の進捗は？',0, 100, 50)
'課題3進捗：',progress
