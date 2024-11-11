import streamlit as st
import functions as fun
from sklearn.model_selection import train_test_split
from catboost import Pool
from catboost import CatBoostRegressor
from PIL import Image


img = Image.open('./data/Logo_big.png')
# img = img.resize((128, 128))
st.image(img)

st.header('💄화장품 추천💄')
st.markdown('추천 받고 싶은 화장품 피부타입, 카테고리, 브랜드를 선택하면 세포라 화장품 추천해드립니다.')

skin_type = st.selectbox(
    '피부타입을 선택해주세요.',
    options = ['dry', 'normal', 'combination', 'oily'],
    index=False
)


secondary_category = st.selectbox(
    '카테고리를 선택해주세요.',
    options=['Treatments', 'Moisturizers', 'Cleansers ', 'Mini Size ', 'Masks', 'Eye Care', 'Sunscreen', 'Lip Balms & Treatments', 'Self Tanners',
    'Value & Gift Sets', 'Wellness', 'High Tech Tools'],
    index = False # 초기값 설정
)

brand_name = st.selectbox(
    '원하는 브랜드를 선택해주세요.',
    options = ['The Ordinary', 'Tetcha', 'Glow Recipe', 'LANEIGE', 'Dr. Jart+', 'Farmacy',"Kiehl's Since 1851", 'Caudalie', 'Biossance', 'Murad', 'CLINIQUE', 'Fenty Skin', 'SK-II', 'Shiseido', 'Estée Laude', 'innisfree', 'Lancôme', 'Lancôme', 'Dior', 'Bobbi Brown', 'CAY SKIN', 'belif']
)

# secondary_category = st.text_input('원하는 화장품을 입력해주세요.')



sephora_df = fun.pickle_load()
# sephora_df = fun.load_data()
product_name_x = sephora_df['product_name_x']

if brand_name and secondary_category and skin_type:
    recommend_product = fun.regression_recommend(sephora_df, product_name_x, brand_name, secondary_category, skin_type)
    st.write(recommend_product)