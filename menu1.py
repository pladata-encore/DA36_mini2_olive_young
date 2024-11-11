# 은비님
import streamlit as st
from functions import *
import functions as fun
from PIL import Image

img = Image.open('data/Logo_big.png')
# img = img.resize((128, 128))
st.image(img)

# fun.pickle_load()

st.title("좋아요♥️ TOP3:")

st.markdown("카테고리를 선택하면 해당 카테고리의 '좋아요' 상위 3개의 제품을 알려드립니다.")

fun.top3_love_count()

