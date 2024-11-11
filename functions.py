import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from catboost import Pool
from catboost import CatBoostRegressor
import pickle

product_info = None
sephora_df = None
product_review_rate_df = None

@st.cache_data
def data_load():

    global product_info, sephora_df

    product_info = pd.read_csv('./data/product_info.csv', encoding='latin1')
    product_info['rating_average'] = product_info['rating']
    product_info[['rating', 'rating_average']]
    product_info = product_info.drop('rating', axis=1)
    product_info['rating_average']

    review_1 = pd.read_csv('./data/reviews_0-250.csv', dtype=str)
    review_2 = pd.read_csv('./data/reviews_250-500.csv', dtype=str)
    review_3 = pd.read_csv('./data/reviews_500-750.csv', dtype=str)
    review_4 = pd.read_csv('./data/reviews_750-1250.csv', dtype=str)
    review_5 = pd.read_csv('./data/reviews_1250-end.csv', dtype=str)

    review_df = pd.concat([review_1, review_2, review_3, review_4, review_5])
    review_df['product_name'].value_counts()
    df = pd.merge(review_df, product_info, how='outer', on='product_id')
    sk_df = df[df['primary_category'] == 'Skincare']
    seph_df = sk_df[['author_id', 'rating', 'rating_average', 'is_recommended', 'helpfulness',
                     'total_feedback_count', 'total_neg_feedback_count',
                     'total_pos_feedback_count', 'submission_time', 'review_text',
                     'review_title', 'skin_tone', 'eye_color', 'skin_type', 'hair_color',
                     'product_name_x', 'brand_name_x', 'price_usd_x',
                     'loves_count', 'reviews',
                     'ingredients', 'highlights', 'primary_category',
                     'secondary_category']]
    sephora_df = seph_df.dropna()
    sephora_df = sephora_df.sample(n=100000, random_state=0)
    sephora_df.reset_index(drop=True, inplace=True)

def load_data():

    global product_info, sephora_df

    product_info = pd.read_csv('./data/product_info.csv', encoding='latin1')
    product_info['rating_average'] = product_info['rating']
    product_info[['rating', 'rating_average']]
    product_info = product_info.drop('rating', axis=1)
    product_info['rating_average']

    review_1 = pd.read_csv('./data/reviews_0-250.csv', dtype=str)
    review_2 = pd.read_csv('./data/reviews_250-500.csv', dtype=str)
    review_3 = pd.read_csv('./data/reviews_500-750.csv', dtype=str)
    review_4 = pd.read_csv('./data/reviews_750-1250.csv', dtype=str)
    review_5 = pd.read_csv('./data/reviews_1250-end.csv', dtype=str)

    review_df = pd.concat([review_1, review_2, review_3, review_4, review_5])
    review_df['product_name'].value_counts()
    df = pd.merge(review_df, product_info, how='outer', on='product_id')
    sk_df = df[df['primary_category'] == 'Skincare']
    seph_df = sk_df[['author_id', 'rating', 'rating_average', 'is_recommended', 'helpfulness',
                     'total_feedback_count', 'total_neg_feedback_count',
                     'total_pos_feedback_count', 'submission_time', 'review_text',
                     'review_title', 'skin_tone', 'eye_color', 'skin_type', 'hair_color',
                     'product_name_x', 'brand_name_x', 'price_usd_x',
                     'loves_count', 'reviews',
                     'ingredients', 'highlights', 'primary_category',
                     'secondary_category']]
    sephora_df = seph_df.dropna()
    sephora_df = sephora_df.sample(n=100000, random_state=0)
    sephora_df.reset_index(drop=True, inplace=True)
    return sephora_df

#     with open("data.pickle", "wb") as fw:
#         pickle.dump(sephora_df, fw)
#
#     return sephora_df
#
# @st.cache_data
def pickle_load():

    global sephora_df

    with open("./data/sephora_df.pickle", "rb") as fr:
        sephora_df = pickle.load(fr)
        # print('피클 로드 완료')
        # print(sephora_df.columns)

        return sephora_df

#----------------------------------------------------------------------------------------------------#



#----------------------------------------------------------------------------------------------------#

def ingre_predict(date_set, user_input):

    sampled_prod_info = pd.DataFrame({
        'prod_name': date_set['product_name_x'],
        'ingredients': date_set['ingredients'] ,
        'highlights': date_set['highlights'],
        'primary_category': date_set['primary_category'],
        'secondary_category': date_set['secondary_category'],
        'rate': date_set['rating_average'],
    })

    small_sampled_prod_info = sampled_prod_info.drop_duplicates()

    count_vectorizer = CountVectorizer()

    ingredi_vec = count_vectorizer.fit_transform(small_sampled_prod_info['ingredients']+small_sampled_prod_info['highlights']+small_sampled_prod_info['primary_category']+small_sampled_prod_info['secondary_category'])

    # print(ingredi_vec)

    user_input = " ".join(user_input)
    input_vec = count_vectorizer.transform([user_input])
    input_ingredi_sim = cosine_similarity(input_vec, ingredi_vec)
    input_ingredi_sim_idx = input_ingredi_sim.argsort(axis=1)[:, :5:-1]

    temp = input_ingredi_sim_idx[:, 1:5]
    predicted_item = small_sampled_prod_info[['rate','prod_name','highlights',]].iloc[temp.tolist()[0]]

    return predicted_item

def ingre_predict2(date_set, user_input):
    from sklearn.feature_extraction.text import TfidfVectorizer

    sampled_prod_info = pd.DataFrame({
        'prod_name': date_set['product_name_x'],
        'ingredients': date_set['ingredients'] ,
        'highlights': date_set['highlights'],
        'primary_category': date_set['primary_category'],
        'secondary_category': date_set['secondary_category'],
        'rate': date_set['rating_average'],
    })


    tfidf_vectorizer = TfidfVectorizer(

        max_df=0.85,  # DF(df(t)/N)가 85% 이상인 단어 제외 (vocab에 미포함)
        min_df=0.05  # DF(df(t)/N)가 5% 이하인 단어 제외 (vocab에 미포함)
    )


    small_sampled_prod_info = sampled_prod_info.drop_duplicates()

    ingredi_vec = tfidf_vectorizer.fit_transform(
        small_sampled_prod_info['ingredients'] + small_sampled_prod_info['highlights'] + small_sampled_prod_info[
            'primary_category'] + small_sampled_prod_info['secondary_category'])

    # print(ingredi_vec)

    user_input = " ".join(user_input)
    input_vec = tfidf_vectorizer.transform([user_input])
    input_ingredi_sim = cosine_similarity(input_vec, ingredi_vec)
    input_ingredi_sim_idx = input_ingredi_sim.argsort(axis=1)[:, :5:-1]

    temp = input_ingredi_sim_idx[:, 1:5]
    predicted_item = small_sampled_prod_info[['rate','prod_name','highlights',]].iloc[temp.tolist()[0]]

    return predicted_item

#----------------------------------------------------------------------------------------------------#

def top3_love_count():


    cat = st.selectbox(
        '카테고리를 입력하세요',
        ('Moisturizers','Treatments','Sunscreen','Eye Care','Masks','Self Tanners','Lip Balms & Treatments'),
        index=None,
        placeholder="선택해주세요!"
    )
    category_and_love_df = sephora_df[['product_name_x', 'secondary_category', 'loves_count', 'highlights']]


    if cat:
        cat_filtered_df = category_and_love_df[category_and_love_df['secondary_category'] == cat]

        if cat_filtered_df.empty:
            st.write('입력하신 카테고리가 존재하지 않습니다.')
            return None

        top3_category_love = (
            cat_filtered_df.groupby('secondary_category')
            .apply(lambda x: x.sort_values(by='loves_count', ascending=False)
                   .drop_duplicates(subset=['loves_count'])
                   .head(3))
            .reset_index(drop=True)
        )

        st.write(f"{cat} 카테고리의 좋아요♥️ 수 상위 3개 제품:")
        st.dataframe(top3_category_love)
        st.write('')
        st.bar_chart(top3_category_love,x='product_name_x', y='loves_count', use_container_width=True, horizontal=True, height=200)

        return top3_category_love
    else :
        st.write('카테고리별 인기 상품을 확인해 보세요!')
    return None

#----------------------------------------------------------------------------------------------------#

def top3_brand_count():


    brand_rating_df = pd.DataFrame(
        sephora_df[['product_name_x', 'brand_name_x', 'rating_average', 'highlights']])

    # 브랜드별 상위 3개 제품을 먼저 계산
    top3_brand_rating = (
        brand_rating_df.groupby('brand_name_x')
        .apply(lambda x: x.sort_values(by='rating_average', ascending=False)
               .drop_duplicates(subset=['rating_average'])
               .head(3))
        .reset_index(drop=True)
    )
    brand_list = top3_brand_rating['brand_name_x'].unique()

    bn = st.selectbox(
        '브랜드명을 입력하세요',
        brand_list,
        index=None,
        placeholder="브랜드명을 선택해주세요!"
    )

    if bn:
        # 입력된 브랜드에 대해 필터링
        selected_brand = top3_brand_rating[top3_brand_rating['brand_name_x'] == bn]

        if selected_brand.empty:
            st.write('입력하신 브랜드가 존재하지 않습니다.')
            return None

        st.write(f"브랜드 '{bn}'의 평점 상위 3개 제품")
        st.dataframe(selected_brand,hide_index=True)
        return selected_brand
    else:
        st.write('**전체 브랜드**의 상위 3개 제품')
        st.dataframe(top3_brand_rating,hide_index=True)
    return None

#----------------------------------------------------------------------------------------------------#

def review_and_avg_rate():
    global product_review_rate_df

    # riv = st.text_input(
    #     label = '제품명을 입력하세요',
    #     placeholder = '제품명'
    # )

    riv = st.selectbox(
        '제품명을 입력하세요',
        sephora_df['product_name_x'].sort_values(ascending=True).unique(),
        index=None,
        placeholder="제품명을 선택해주세요"
    )

    product_review_rate_df = pd.DataFrame(sephora_df[['product_name_x', 'review_text', 'rating_average', 'highlights']])

    if riv:
        riv_filtered_df = product_review_rate_df[product_review_rate_df['product_name_x'] == riv]

        if riv_filtered_df.empty:
            st.write('입력하신 제품이 존재하지 않습니다.')
            return None

        st.write(f"'{riv}'의 리뷰, 평균평점, 하이라이트")
        st.dataframe(riv_filtered_df[['review_text', 'rating_average', 'highlights']],hide_index=True)

        return riv_filtered_df[['review_text', 'rating_average', 'highlights']]
    else:
        st.write('제품의 리뷰와 평점을 확인해 보세요!')
    return None

#----------------------------------------------------------------------------------------------------#

def regression_recommend(sephora_df, product_name_x, brand_name, secondary_category, skin_type):
    # sephora_df = sephora_df[['product_name_x', 'brand_name_x', 'skin_type', 'secondary_category', 'rating']]
    #
    # X = sephora_df.drop('rating', axis=1)
    # y = sephora_df['rating']
    #
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    #
    # cat_features = ['product_name_x', 'brand_name_x', 'secondary_category', 'skin_type']
    #
    # X_train_pool = Pool(X_train, y_train, cat_features=cat_features)
    # X_test_pool = Pool(X_test, y_test, cat_features=cat_features)
    #
    # cb_reg = CatBoostRegressor(
    #     n_estimators=50,
    #     depth=5,
    #     learning_rate=0.05,
    #     loss_function='RMSE',
    #     eval_metric='RMSE'
    # )
    #
    # cb_reg.fit(X_train_pool, eval_set=X_test_pool, verbose=100)

    # with open("cb_reg.pickle", "wb") as fw:
    #     pickle.dump(cb_reg, fw)
    with open("cb_reg.pickle", "rb") as fr:
        cb_reg = pickle.load(fr)


    user_category = secondary_category
    brand_name = brand_name

    recommend_product = sephora_df[sephora_df['secondary_category'] == user_category]
    recommend_product = recommend_product[recommend_product['brand_name_x'] == brand_name]['product_name_x'].unique()

    user_input = ['product_name_x', brand_name, 'skin_type', user_category]

    pred_result = []
    for product in recommend_product:
        user_input[0] = product
        pred_rating = cb_reg.predict(user_input)
        pred_result.append(pred_rating)

    result_df = pd.DataFrame({
        'product': recommend_product,
        'rating_pred': pred_result
    })
    result_df = result_df.sort_values('rating_pred', ascending=False)
    print(result_df)
    return result_df

