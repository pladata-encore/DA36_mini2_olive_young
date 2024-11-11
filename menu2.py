import streamlit as st
import functions as fun
from PIL import Image

img = Image.open('./data/Logo_big.png')
# img = img.resize((128, 128))
st.image(img)

st.title('브랜드 TOP3')


st.markdown("원하는 브랜드를 선택하시면 평점 상위 3개의 제품을 보여립니다.")
fun.top3_brand_count()