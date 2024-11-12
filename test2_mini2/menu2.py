import streamlit as st
import functions as fun

st.title('Top 3 Brand🛻')


st.write("**브랜드별** 평점 상위 3개 제품")
fun.top3_brand_count()