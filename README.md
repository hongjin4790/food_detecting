<h1>🍽️ 식품 카테고리 분류 프로젝트</h1> 

# 1. 프로젝트 개요

식품 이미지를 분석하여 개별 식품을 자동으로 감지하는 기술은 컴퓨터 비전 분야에서 중요한 연구 주제로 부상하고 있습니다. 이는 식품의 품질 관리, 영양 정보 추출, 맛 평가 등 다양한 분야에서 활용 가능성이 큽니다.

본 프로젝트는 YOLOv5-Seg 모델을 활용하여 식품 이미지를 자동으로 분류하는것을 목표로 합니다. 기존의 Object Detection 모델들과 달리 각 픽셀 단위로 분리하는 Segmentation 기법을 적용하여 정밀한 카테고리 분류를 수행합니다.

# 2. 데이터 전처리 및 변환

#### 데이터 다운로드: https://www.aicrowd.com/challenges/food-recognition-benchmark-2022/participation_terms/2 

### 2.1. 데이터셋 형식 변환
![image](https://github.com/user-attachments/assets/e121d183-0ca6-4a26-abaf-b2362280e1da)

프로젝트에 사용된 데이터는 **COCO Dataset Format**에서 **YOLOv5 Segmentation Dataset Format**으로 변환하였습니다. COCO Dataset은 객체 검출, Segmentation, 키 포인트 탐지 등 다양한 작업에 사용되는 데이터 포맷으로, 이미지 정보, 레이블 정보 등이 포함된 JSON 형식입니다.

반면 YOLOv5는 객체 검출에 주로 사용되며, 훈련 데이터는 **이미지 파일**과 **텍스트 형식의 레이블 정보**로 구성됩니다. 이러한 차이로 인해, **COCO Dataset Format**을 **YOLOv5 Segmentation Dataset Format**으로 변환하는 과정이 필요했습니다.

### 2.2. 변환 과정

1. **COCO JSON 파일 분석**: COCO 데이터셋의 JSON 파일에서 각 이미지에 대한 레이블 정보를 추출합니다.
2. **YOLOv5 형식으로 변환**: 추출된 레이블 정보를 YOLOv5 Segmentation 형식에 맞게 변환합니다. YOLOv5는 각 이미지에 대해 **클래스 ID**와 **마스크 정보**를 포함하는 텍스트 파일을 요구하므로, 이를 정확하게 변환해야 합니다.
3. **Segmentation 마스크 생성**: 각 이미지에서 **객체의 마스크**를 추출하여 YOLOv5가 요구하는 포맷에 맞게 저장합니다.

![image](https://github.com/user-attachments/assets/4c30d651-68a4-4b74-9c1d-579955567c1b)

<img src="https://github.com/user-attachments/assets/1e138f51-ab02-42e7-bc81-0711503bcbdd" width="500" height="500"/>

****Yaml 파일****

![image](https://github.com/user-attachments/assets/f184fd28-a12a-4050-b1e5-dcb5a8602263)


위의 코드들로 Json 파일에 있는 정보를 각 이미지당 텍스트 파일을 생성하여 image_id, bbox, segmentation를 저장하고 Dataset의 경로, 클래스의 이름 등을 포함하는 Yaml 파일을 따로 생성하여 저장하였습니다.

위와 같은 과정을 통해 **COCO Dataset**을 **YOLOv5 Segmentation Dataset Format**으로 변환하여 모델 학습에 활용할 수 있었습니다.

 # 3. YOLOv5-seg 모델 학습
### 3.1 YOLOv5 설치 및 사전학습 모델 다운로드

먼저 YOLOv5를 클론한 후 사전 학습된 YOLOv5-seg 모델을 다운로드 합니다.
```
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
```

### 3.2 yolov5 폴더 구조 ###

미리 준비한 데이터셋, Yaml 파일, 사전 학습된 모델을 아래와 같은 경로로 설정합니다.

<img src="https://github.com/user-attachments/assets/8c305c05-cf3c-4638-bbb0-9f64e053c653" width="300" height="300"/>

### 3.3 모델 학습 ###

학습을 시작하려면 ```train.py```를 실행합니다.

아래 명령어를 통해 학습을 시작합니다:
```
python C:\Users\asiclab\Desktop\YOLO5\yolov5\segment\train.py \
--data C:\Users\asiclab\Desktop\YOLO5\yolo_data\dataSeg.yaml \
--batch-size 16 \
--imgsz 416 \
--weights C:\Users\asiclab\Desktop\YOLO5\yolov5\yolov5s-seg.pt \
--epoch 100
```
batch size는 16, 이미지 사이즈는 416x416, 에폭 수는 100으로 설정하였습니다.

학습이 완료되면 학습된 모델은 ```runs/train-seg/exp/weights/best.pt```에 저장됩니다.

# 4. 실험 결과

 아래의 그래프는 epoch에 따른 각 손실 함수값과 모델 학습과 검증 과정에서의 성능지표 결과를 보여줍니다.
 
 ![그림1](https://github.com/user-attachments/assets/267490aa-fb57-4c3a-8122-fb174c6318e2)

- 모델의 box loss와 segmentation loss는 훈련과 검증 데이터에서 비슷한 값을 보이고 상대적으로 낮은 값을 나타내어 객체 감지 성능이 잘 최적화되었음을 알 수 있습니다.
- mAP (Mean Average Precision) 값은 0.5의 IoU에서 0.50279의 정확도를 보이고 mAP_0.5:0.95는 0.37144로 IoU 값이 높아질수록 정확도가 떨어짐을 보여줍니다.
- Precision과 Recall 값은 각각 0.58274와 0.45689로 모델이 예측한 객체의 정확도와 예측할 수 있는 객체의 비율이 중간정도로 개선이 필요해 보입니다.

# 5. 추론(Inference)
```predict.py```를 실행하여 새로운 이미지에서 테스트할 수 있습니다.

아래 명령어를 통해 테스트를 시작합니다:
```
python C:\Users\asiclab\Desktop\YOLO5\yolov5\segment\predict.py \
--weights C:\Users\asiclab\Desktop\YOLO5\yolov5\runs\train-seg\exp\weights\best.pt \
--img 416 \
--conf 0.25 \
--source C:\Users\asiclab\Desktop\YOLO5\yolo_data\test\images
```

![image](https://github.com/user-attachments/assets/2b0a4cd1-7369-4d26-8398-1ad010f635fa)

![image](https://github.com/user-attachments/assets/fbe0aad2-7e6a-4051-84f5-c4a154cc8bf9)

![image](https://github.com/user-attachments/assets/308d57f7-abdd-44d6-a768-244cf6c7c567)

![image](https://github.com/user-attachments/assets/306b9425-3e6c-4cdc-b0c1-b6fdf8fa7049)

