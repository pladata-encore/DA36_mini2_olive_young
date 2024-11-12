import streamlit as st
import pandas as pd
import numpy as np
from pyparsing import empty
from tkinter.tix import COLUMN

import functions as fun
from PIL import Image

img = Image.open('./data/Logo_big.png')
# img = img.resize((128, 128))
st.image(img)

st.subheader(' ')
st.empty()

st.video('./data/sephora_vi.mp4')
st.text(' ')

st.subheader('ABOUT THIS HOMEPAGE')
st.markdown('세포라 화장품을 이용했던 여러 고객님들의 데이터를 활용하여 세포라 화장품에 다양한 정보를 제공해주고 있습니다.')
st.empty()

con1, con2 = st.columns([1, 1])

if st.subheader('ABOUT MENU'):
    con1, con2 = st.columns([1, 1])
    with con1:
        best = st.button('BEST SELLER',
                  icon = '🎖️',
                  use_container_width=True,
                  )
        if best:
            st.checkbox('category')
            st.checkbox('review&rating')
            st.checkbox('brand')

    with con2:
        recommendation = st.button('RECOMMENDATION',
                                   icon = '👍',
                                   use_container_width=True,)
        if recommendation:
            st.checkbox('내가 설정한 화장품')
            st.checkbox('성분별 추천 화장품')

st.subheader('MORE')
st.markdown('* SEPHORA HOMPAGE')

st.link_button('SEPHORA', url='https://www.sephora.com/',
               use_container_width=True)
# with col1:
#     crown = Image.open('data/crown.jpeg')
#     st.image(crown)
#     img = img.resize((10, 10))
#     st.write('세포라 인기 제품을 확인해보세요.')
