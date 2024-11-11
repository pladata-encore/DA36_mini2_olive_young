import streamlit as st
import functions as fun
from PIL import Image


img = Image.open('./data/Logo_big.png')
# img = img.resize((128, 128))
st.image(img)

st.title("리뷰 & 평점")



st.markdown("제품을 선택하면 리뷰와 평점을 보여드립니다.")
fun.review_and_avg_rate()