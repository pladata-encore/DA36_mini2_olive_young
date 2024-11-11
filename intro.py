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

if st.subheader('ABOUT MENU'):
    con1, con2, con3 = st.columns([1, 1, 1])
    with con1:
        like = st.button('RANKING',
                  icon = '👑',
                  use_container_width=True,
                  )
        if like:
            st.checkbox('category by ❤️')
            st.checkbox('brand')

    with con2 :
        check = st.button('CHECK',
                          icon = '✔️',
                          use_container_width=True,)
        if check:
            st.checkbox('review & rating')

    with con3:
        recommendation = st.button('RECOMMENDATION',
                                   icon = '👍',
                                   use_container_width=True,)
        if recommendation:
            st.checkbox('By brand & category')
            st.checkbox('By ingredient')

st.subheader('MORE')
st.markdown('* SEPHORA HOMPAGE')

st.link_button('SEPHORA', url='https://www.sephora.com/',
               use_container_width=True)
