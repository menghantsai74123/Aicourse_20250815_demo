import numpy as np
import pandas as pd
import streamlit as st

st.title("DEMO PAGE")
st.write("123")
st.write("## 123")

arr1=np.array([1,2,3,4,5,6])
st.write(arr1)

df1=pd.DataFrame([[11,22,33,44],[50,60,70,80]])
st.write(df1)
st.table(df1)

st.write("## 核取方塊")
r1 = st.checkbox("外帶")
if r1:
    st.info("外帶")
else:
    st.info("內用")

checks = st.columns(2)
txt = ''
with checks[0]:
    r11=st.checkbox("A")
    if r11:
        txt += " A "
with checks[1]:
    r12=st.checkbox("B")
    if r12:
        txt += " B "
st.info(txt)

st.write("## 選項按鈕")
b1 = st.radio("選項", ("甲", "乙", "丙"))
st.info(b1)

b2 = st.radio("選項", ("甲", "乙", "丙"),key="b2")
st.info(b2)

st.write("## 滑桿")
num = st.slider("請選擇數量", 1.0, 5.0, 2.5)  #起點,終點,起始位置
st.info(num) 

st.sidebar.write("## 下拉選單")
city = st.sidebar.selectbox("請選擇城市", ("台北", "台中", "高雄"))
if city == "台北":
    st.sidebar.info("您選擇的城市是台北")
elif city == "台中":
    st.sidebar.info("您選擇的城市是台中")
else:
    st.sidebar.info("您選擇的城市是高雄")   

st.write("## 按鈕")
a = st.number_input("num...")
b = st.number_input("num...", key='b')
if st.button("相加"):
    st.write("### 相加結果:", a + b)