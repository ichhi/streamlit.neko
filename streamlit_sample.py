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

if input:
    lst1.append(input)
if st.checkbox('delete1'):
    delete = st.selectbox('課題1の削除する要素を選択して下さい', options=lst1)
    if st.button('Delete1'):
        lst1.remove(delete)
        st.success(f'Delete1 : {delete}')

if st.checkbox('change1'):
    change_from = st.selectbox('課題1の変更する要素を選択して下さい', options=lst1)
    change_index = lst1.index(change_from)
    change_to = st.text_input('どのように課題1を変更しますか')
    if st.button('Change1'):
        lst1.remove(change_from)
        lst1.insert(change_index, change_to)
        st.success(f'Change1 {change_from} to {change_to}')
        
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

if input:
    lst2.append(input)
if st.checkbox('delete2'):
    delete = st.selectbox('課題2の削除する要素を選択して下さい', options=lst2)
    if st.button('Delete2'):
        lst2.remove(delete)
        st.success(f'Delete2 : {delete}')

if st.checkbox('change2'):
    change_from = st.selectbox('課題2の変更する要素を選択して下さい', options=lst2)
    change_index = lst2.index(change_from)
    change_to = st.text_input('どのように課題2を変更しますか')
    if st.button('Change2'):
        lst2.remove(change_from)
        lst2.insert(change_index, change_to)
        st.success(f'Change2 {change_from} to {change_to}')
        
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

if input:
    lst3.append(input)
if st.checkbox('delete3'):
    delete = st.selectbox('課題3の削除する要素を選択して下さい', options=lst3)
    if st.button('Delete3'):
        lst3.remove(delete)
        st.success(f'Delete3 : {delete}')

if st.checkbox('change3'):
    change_from = st.selectbox('課題3の変更する要素を選択して下さい', options=lst3)
    change_index = lst3.index(change_from)
    change_to = st.text_input('どのように課題3を変更しますか')
    if st.button('Change3'):
        lst3.remove(change_from)
        lst3.insert(change_index, change_to)
        st.success(f'Change3 {change_from} to {change_to}')
        
st.table(lst3)



progress3 = st.slider('課題3の進捗は？',0, 100, 50)
'課題3進捗：',progress3







