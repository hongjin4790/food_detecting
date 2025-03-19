🍽️ 식품 카테고리 분류 프로젝트

# 1. 프로젝트 개요

식품 이미지를 분석하여 개별 식품을 자동으로 감지하는 기술은 컴퓨터 비전 분야에서 중요한 연구 주제로 부상하고 있습니다. 이는 식품의 품질 관리, 영양 정보 추출, 맛 평가 등 다양한 분야에서 활용 가능성이 큽니다.
본 프로젝트는 딥러닝 기반의 컴퓨터 비전 모델을 훈련시켜, 식품 이미지 내의 개별 식품을 정확하게 감지하고 분류하는 것을 목표로 합니다. 이를 통해 식품 관련 산업에서의 자동화 및 효율성을 높이고, 소비자들에게 더 나은 서비스를 제공할 수 있는 기반을 마련합니다.

# 2. 데이터 전처리 및 변환

### 2.1. 데이터셋 형식 변환
![image](https://github.com/user-attachments/assets/e121d183-0ca6-4a26-abaf-b2362280e1da)

프로젝트에 사용된 데이터는 **COCO Dataset Format**에서 **YOLOv5 Segmentation Dataset Format**으로 변환하였습니다. COCO Dataset은 객체 검출, Segmentation, 키 포인트 탐지 등 다양한 작업에 사용되는 데이터 포맷으로, 이미지 정보, 레이블 정보 등이 포함된 JSON 형식입니다.

반면 YOLOv5는 객체 검출에 주로 사용되며, 훈련 데이터는 **이미지 파일**과 **텍스트 형식의 레이블 정보**로 구성됩니다. 이러한 차이로 인해, **COCO Dataset Format**을 **YOLOv5 Segmentation Dataset Format**으로 변환하는 과정이 필요했습니다.

### 2.2. 변환 과정

1. **COCO JSON 파일 분석**: COCO 데이터셋의 JSON 파일에서 각 이미지에 대한 레이블 정보를 추출합니다.
2. **YOLOv5 형식으로 변환**: 추출된 레이블 정보를 YOLOv5 Segmentation 형식에 맞게 변환합니다. YOLOv5는 각 이미지에 대해 **클래스 ID**와 **마스크 정보**를 포함하는 텍스트 파일을 요구하므로, 이를 정확하게 변환해야 합니다.
3. **Segmentation 마스크 생성**: 각 이미지에서 **객체의 세그먼트 마스크**를 추출하여 YOLOv5가 요구하는 포맷에 맞게 저장합니다.

이 과정을 통해 **COCO Dataset**을 **YOLOv5 Segmentation Dataset**에 맞는 포맷으로 변환하여 모델 학습에 활용할 수 있었습니다.

 # 3. 모델 아키텍처


# 4. 실험 결과


# 5. 환경 설정

### 필수 라이브러리 설치
```
pip install torch 
```
# 6. 사용 방법




