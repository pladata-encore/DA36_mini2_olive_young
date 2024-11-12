import streamlit as st
import functions as fun
from sklearn.model_selection import train_test_split
from catboost import Pool
from catboost import CatBoostRegressor

st.header('RECOMMENDATION 1')
st.subheader('based on selected options')

secondary_category = st.selectbox(
    '카테고리를 골라주세요.',
    options=['Treatments', 'Moisturizers', 'Cleansers ', 'Mini Size ', 'Masks', 'Eye Care', 'Sunscreen', 'Lip Balms & Treatments', 'Self Tanners',
    'Value & Gift Sets', 'Wellness', 'High Tech Tools'],
    # index = 4 # 초기값 설정
)

brand_name = st.selectbox(
    '원하는 브랜드를 골라주세요',
    options = ['The Ordinary', 'Tetcha', 'Glow Recipe', 'LANEIGE', 'Dr. Jart+', 'Farmacy',"Kiehl's Since 1851", 'Caudalie', 'Biossance', 'Murad', 'CLINIQUE', 'Fenty Skin', 'SK-II', 'Shiseido', 'Estée Laude', 'innisfree', 'Lancôme', 'Lancôme', 'Dior', 'Bobbi Brown', 'CAY SKIN', 'belif']
)

# secondary_category = st.text_input('원하는 화장품을 입력해주세요.')
skin_type = st.selectbox(
    '피부타입을 골라주세요.',
    options = ['dry', 'normal' 'combination', 'oily'])


sephora_df = fun.pickle_load()
# sephora_df = fun.load_data()
product_name_x = sephora_df['product_name_x']

if brand_name and secondary_category and skin_type:
    recommend_product = fun.regression_recommend(sephora_df, product_name_x, brand_name, secondary_category, skin_type)
    st.write(recommend_product)