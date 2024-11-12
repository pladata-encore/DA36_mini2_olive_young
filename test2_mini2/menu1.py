# 은비님
import streamlit as st
import functions as fun

# fun.pickle_load()

st.title("Top3 Category Love Count")

st.write("카테고리별 좋아요 수 상위 3개 제품:")
fun.top3_love_count()
# print(temp['product_name_x'])
# st.bar_chart(y= temp['loves_count'].astype(int))