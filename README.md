# DA36_mini2_4 project
# 🐻 K3J1 🐻

### AI 미니 프로젝트 산출물
  - 사용한 Datasets
  - 소스코드 (쥬피터 노트북 / stremlit 파일)
  - Github issue 할일 관리 (아주 중요)
  - Github README.md
  - PPT
  - 시연영상 5분

### AI 프로젝트 PPT 구성 내용
1. 프로젝트 제목
2. 프로젝트 개요
  - 개발배경 (주제 선정 이유)
  - 시장분석
3. 목차
4. 구성원 소개
5. 프로젝트 산출물
  - 데이터 취득
  - 데이터 전처리
  - 모델 훈련
  - 결론 및 기대효과
6. 시연 (유투브 5분 영상 업로드 링크)
7. Q&A

**Product Data (제품 데이터)**
1. product_id: 사이트에서 제품을 고유하게 식별하는 ID.
2. product_name: 제품의 전체 이름.
3. brand_id: 제품 브랜드의 고유 식별자.
4. brand_name: 제품 브랜드의 전체 이름.
5. loves_count: 이 제품을 좋아요로 표시한 사람들의 수.
6. rating: 사용자 리뷰를 바탕으로 한 제품의 평균 평점.
7. reviews: 해당 제품에 대한 사용자 리뷰 수. 
8. size: 제품의 크기 (예: oz, ml, g, 팩 등).
9. variation_type: 제품의 변형 유형 (예: 크기, 색상).
10. variation_value: 변형 유형에 대한 구체적인 값 (예: 100 mL, 골든 샌드).
11. variation_desc: 변형 유형에 대한 설명 (예: 피부 톤을 고려한 색상 등).
12. ingredients: 제품에 포함된 성분 목록. 변형이 있는 경우 각 변형에 대한 성분 리스트가 따로 있을 수 있음.
13. price_usd: 제품의 정가 (미국 달러 기준).
14. value_price_usd: 제품의 잠재적인 가격 절감액, 정가 옆에 표시되는 할인 정보.
15. sale_price_usd: 제품의 할인된 가격 (미국 달러 기준).
16. limited_edition: 제품이 한정판인지 여부 (1: 한정판, 0: 비한정판).
17. new: 제품이 새로 출시된 것인지 여부 (1: 새로 출시된 제품, 0: 새로 출시되지 않은 제품).
18. online_only: 해당 제품이 오직 온라인에서만 판매되는지 여부 (1: 온라인 전용, 0: 오프라인에서도 판매).
19. out_of_stock: 제품이 재고가 없는 상태인지 여부 (1: 품절, 0: 품절 아님).
20. sephora_exclusive: 제품이 Sephora에서만 독점적으로 판매되는지 여부 (1: 독점, 0: 독점 아님).
21. highlights: 제품의 특징이나 주요 속성에 대한 태그 목록 (예: "비건", "매트 피니시").
22. primary_category: 제품이 속한 첫 번째 카테고리.
23. secondary_category: 제품이 속한 두 번째 카테고리.
24. tertiary_category: 제품이 속한 세 번째 카테고리.
25. child_count: 해당 제품의 변형(사이즈, 색상 등) 수.
26. child_max_price: 해당 제품의 변형 중 가장 높은 가격.
27. child_min_price: 해당 제품의 변형 중 가장 낮은 가격.

**Reviews Data (리뷰 데이터)**
1. author_id: 리뷰 작성자의 고유 식별자.
2. rating: 리뷰 작성자가 부여한 제품의 평점 (1~5).
3. is_recommended: 리뷰 작성자가 이 제품을 추천하는지 여부 (1: 추천, 0: 추천하지 않음).
4. helpfulness: 리뷰의 유용성 지표, 긍정적인 피드백 수 / 전체 피드백 수.
5. total_feedback_count: 해당 리뷰에 대한 총 피드백 수 (긍정적 및 부정적 피드백을 모두 포함).
6. total_neg_feedback_count: 해당 리뷰에 대해 부정적인 피드백을 남긴 사용자 수.
7. total_pos_feedback_count: 해당 리뷰에 대해 긍정적인 피드백을 남긴 사용자 수.
8. submission_time: 리뷰가 작성된 날짜 (yyyy-mm-dd 형식).
9. review_text: 리뷰의 본문 텍스트.
10. review_title: 리뷰의 제목.
11. skin_tone: 리뷰 작성자의 피부 톤 (예: fair, tan 등).
12. eye_color: 리뷰 작성자의 눈 색깔 (예: brown, green 등).
13. skin_type: 리뷰 작성자의 피부 타입 (예: combination, oily 등).
14. hair_color: 리뷰 작성자의 머리 색깔 (예: brown, auburn 등).
15. product_id: 리뷰가 작성된 제품의 고유 ID.

