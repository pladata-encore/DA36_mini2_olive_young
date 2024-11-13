import streamlit as st
import functions as fun

st.title("Product - review&avg_rating&highlight")



st.write("제품별 리뷰, 평점 :")
fun.review_and_avg_rate()