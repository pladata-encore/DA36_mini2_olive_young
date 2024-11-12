from operator import index

import streamlit as st
import functions as fun

from PIL import Image
import pickle


# df = fun.load_data()

sephora_df = fun.pickle_load()

st.subheader('기존 화장품 기반으로 비슷한 성분 화장품 추천')


col1,col2 = st.columns(2)
with col1:
    # fun.get_img()
    img = Image.open('pics/img.png')
    st.image(img)
    st.subheader(' ')
    st.text(' ')


    clicked = st.button('CV로 비슷한 제품 찾기',use_container_width=True)
    clicked2 = st.button('TF-IDF로 비슷한 제품 찾기',use_container_width=True)

with col2:
    name = st.selectbox('**화장품이름**을 입력하세요',sephora_df['product_name_x'].sort_values(ascending=True).unique(),
                        )
    idx = sephora_df[sephora_df['product_name_x']==name].index[0]
    print(idx)
    st.write(f':red[**{name}**]','의 주요 기능입니다!')
    temp_list1 = [temp.strip() for temp in sephora_df['highlights'][idx].split(',') if temp]
    temp_list2 = [temp.strip() for temp in sephora_df['ingredients'][idx].split(',') if temp]
    temp_list3 = [temp.strip() for temp in sephora_df['secondary_category'][idx].split(',') if temp]
    temp_list4 = [temp.strip() for temp in sephora_df['primary_category'][idx].split(',') if temp]

    # print(temp_list)
    st.dataframe({
        '주요기능 (Good for)' : temp_list1,
    }, width=1000,height=int(4*35+3))

    st.dataframe({
        '주요 성분' : temp_list2,
    }, width=1000, height=int(4*35+3))



if clicked:
    # df = fun.pickle_load()
    st.dataframe(fun.ingre_predict(sephora_df,temp_list1+temp_list2+temp_list3+temp_list4),hide_index=True)
if clicked2:
    # df = fun.pickle_load()
    st.dataframe(fun.ingre_predict2(sephora_df,temp_list1+temp_list2+temp_list3+temp_list4),hide_index=True)
