
import pandas as pd
import json 
from pathlib import Path
import shutil
import numpy as np
MAPPING_CLS = {50: 0, 101246: 1, 100546: 2, 101129: 3, 101243: 4, 100133: 5, 101306: 6, 101126: 7, 101305: 8, 100206: 9, 101178: 10, 101150: 11, 101185: 12, 101166: 13, 100966: 14, 100078: 15, 100107: 16, 101181: 17, 101335: 18, 100523: 19, 101291: 20, 100063: 21, 101219: 22, 101308: 23, 100089: 24, 101183: 25, 101279: 26, 101188: 27, 101311: 28, 101214: 29, 100321: 30, 101275: 31, 100319: 32, 100838: 33, 101302: 34, 101347: 35, 100184: 36, 100182: 37, 101282: 38, 101144: 39, 100175: 40, 100130: 41, 100145: 42, 100083: 43, 101355: 44, 101194: 45, 101284: 46, 101314: 47, 100790: 48, 101165: 49, 100022: 50, 101354: 51, 101172: 52, 100456: 53, 101236: 54, 100710: 55, 101197: 56, 101180: 57, 100180: 58, 101294: 59, 101193: 60, 101138: 61, 100843: 62, 100352: 63, 100082: 64, 101043: 65, 101022: 66, 100486: 67, 100929: 68, 100161: 69, 101265: 70, 101361: 71, 100674: 72, 101260: 73, 100196: 74, 100245: 75, 100318: 76, 101210: 77, 101208: 78, 101148: 79, 100102: 80, 100235: 81, 100093: 82, 101248: 83, 101358: 84, 100249: 85, 101255: 86, 101326: 87, 101215: 88, 101292: 89, 100963: 90, 100077: 91, 100243: 92, 101258: 93, 101027: 94, 100156: 95, 100152: 96, 100080: 97, 100925: 98, 100960: 99, 100072: 100, 100338: 101, 100687: 102, 100495: 103, 100563: 104, 100826: 105, 100172: 106, 100757: 107, 100150: 108, 100752: 109, 100652: 110, 101310: 111, 100962: 112, 101177: 113, 100099: 114, 101176: 115, 101317: 116, 100942: 117, 100176: 118, 100883: 119, 101212: 120, 101262: 121, 100836: 122, 101340: 123, 100993: 124, 100060: 125, 100300: 126, 101254: 127, 101285: 128, 100108: 129, 100949: 130, 101168: 131, 101297: 132, 100974: 133, 100069: 134, 101187: 135, 101322: 136, 100195: 137, 100333: 138, 100325: 139, 101272: 140, 100302: 141, 101268: 142, 100335: 143, 101009: 144, 101182: 145, 101156: 146, 101220: 147, 100355: 148, 100224: 149, 100594: 150, 100264: 151, 100185: 152, 101346: 153, 100142: 154, 100937: 155, 100086: 156, 100111: 157, 101360: 158, 101200: 159, 100978: 160, 101324: 161, 101201: 162, 100442: 163, 100229: 164, 101296: 165, 100067: 166, 100859: 167, 100645: 168, 101363: 169, 101213: 170, 100445: 171, 100421: 172, 100070: 173, 101190: 174, 100537: 175, 100183: 176, 101141: 177, 101338: 178, 100115: 179, 101298: 180, 100234: 181, 100301: 182, 100171: 183, 100607: 184, 101114: 185, 101247: 186, 101256: 187, 100064: 188, 100157: 189, 101325: 190, 101199: 191, 100477: 192, 101135: 193, 100916: 194, 101349: 195, 100131: 196, 101147: 197, 101329: 198, 100951: 199, 100192: 200, 101123: 201, 101149: 202, 101328: 203, 101341: 204, 100911: 205, 101295: 206, 101121: 207, 100360: 208, 101331: 209, 101273: 210, 100141: 211, 101229: 212, 100982: 213, 100084: 214, 101257: 215, 100092: 216, 100658: 217, 100123: 218, 100101: 219, 101343: 220, 100059: 221, 100834: 222, 100324: 223, 101309: 224, 100725: 225, 101012: 226, 100334: 227, 101304: 228, 101038: 229, 101218: 230, 101238: 231, 100332: 232, 100105: 233, 100140: 234, 100190: 235, 100250: 236, 101244: 237, 100073: 238, 101307: 239, 100143: 240, 101303: 241, 100842: 242, 100475: 243, 101189: 244, 100314: 245, 100200: 246, 101209: 247, 101170: 248, 101014: 249, 100164: 250, 101173: 251, 100129: 252, 100177: 253, 100349: 254, 101237: 255, 100068: 256, 100057: 257, 100423: 258, 101159: 259, 100958: 260, 101271: 261, 100719: 262, 100178: 263, 100076: 264, 101327: 265, 101231: 266, 100348: 267, 100907: 268, 100049: 269, 100467: 270, 100895: 271, 100135: 272, 101153: 273, 100158: 274, 100181: 275, 100840: 276, 101323: 277, 100957: 278, 100173: 279, 100742: 280, 100992: 281, 100681: 282, 100179: 283, 101029: 284, 101240: 285, 100310: 286, 101164: 287, 101290: 288, 100146: 289, 100346: 290, 100649: 291, 100315: 292, 101249: 293, 101118: 294, 100844: 295, 100926: 296, 100909: 297, 101283: 298, 101196: 299, 100437: 300, 100781: 301, 100104: 302, 100282: 303, 100132: 304, 100936: 305, 100337: 306, 101032: 307, 100848: 308, 101006: 309, 101228: 310, 100364: 311, 101266: 312, 100322: 313, 100174: 314, 100114: 315, 100186: 316, 101077: 317, 101274: 318, 100031: 319, 100113: 320, 100151: 321, 100160: 322}


def read_coco_labels(json_pth):
  with open(str(json_pth)) as f:
    coco_annotations = json.load(f)
  return coco_annotations

def return_ann_list(image_id,coco_ann_df):
  temp_df = coco_ann_df.loc[coco_ann_df['image_id']==image_id].copy()
  l=[]
  for i,row in temp_df.iterrows():
    temp_dct = {}
    # temp_dct['category_id']=row['category_id']
    temp_dct['category_id'] = MAPPING_CLS[row['category_id']]
    temp_dct['bbox']=row['bbox']
    temp_dct['segmentation']=row['segmentation']
    l.append(temp_dct)
  return l


def saving_for_src_images(src_df,annotations_df,
                          src_root,none_or_not,yolo_root,split,increment_by_one=False):

  valid_splits={'train','valid','test'}
  if split not in valid_splits:
    raise ValueError(f"Split must be in {valid_splits}")
  cnt=0
  for filename in src_df['file_name'].to_list():
    if none_or_not==None:
      true_f_pth = src_root/'data'/filename
    else:
      true_f_pth = src_root/filename
    img_id = src_df.loc[src_df['file_name']==filename,'id'].iloc[0]
    height = src_df.loc[src_df['file_name']==filename,'height'].iloc[0]
    width = src_df.loc[src_df['file_name']==filename,'width'].iloc[0]

    ann_l = return_ann_list(img_id,annotations_df)
    # Checking if exists:
    to_check = yolo_root/split/'labels'
    to_check.mkdir(exist_ok=True, parents=True)
    try:
      dest_name = f"{yolo_root}/{split}/labels/{filename.split('.jpg')[0]}.txt"
    except:
      dest_name = f"{yolo_root}/{split}/labels/{filename.split('.jpeg')[0]}.txt"
    file_obj = open(str(dest_name),'a')
    for ann in ann_l:
      
      if increment_by_one:
        curr_cat = ann['category_id'] - 1
      else:
        curr_cat = ann['category_id']
      file_obj.write(f"{curr_cat} ")
      for cnt,one_seg in enumerate(ann['segmentation'][0]):

        if cnt%2==0:
          one_val = format(one_seg/width,'.6f')
        else:
          one_val = format(one_seg/height,'.6f')
        file_obj.write(f"{one_val} ")
      file_obj.write('\n')
    file_obj.close()
    # For copying images

  # Checking if exists:
    to_check = yolo_root/split/'images'
    to_check.mkdir(exist_ok=True, parents=True)
    try:
        shutil.copy(true_f_pth,str(f"{yolo_root}/{split}/images"))
    except Exception as e:
        print(f'image canot be copied due to:::{e}')
        pass


  print('---------------SUCCESS-------------')
  #print(yolo_root)
    




def convert_to_yolo_seg_labels(coco_labels_pth,
                                yolo_labels_root_pth,
                                images_src_pth=None,
                                train_percent=0.7,
                                val_percent=0.20,
                                increment_by_one=False):

  '''
  
  Takes COCO format Instance segmentation labels, and images, and save YOLO format labels, in Train, Val, and Test splits, at desired folder

  ********
 
  Keyword Arguments:  

  ********
  coco_labels_pth: type= str | pathlib.Path; required.  the labels json file of COCO format instance segmentation labels
  
  yolo_labels_root_pth: type= str | pathlib.Path; required.  The Directory, where you want to store YOLO-Seg format labels. It can/can't exist
  
  images_src_pth: Optional , if not passed, it means Src images are stored in "data" folder, at same level where labels json file was present.
  Anyway, it is good to pass the path of images, to avoid confusion

  train_percent: type: float; required Percentage of data to put in Train Split

  val_percent: type: float; required Percentage of data to put in Val Split. Based on Train, and Val, Test split will be calculated

  increment_by_one type: bool; If COCO-labels Categories id start with 1, then it should be True, as we need to subtract 1 from CAT-Ids for YOLO format
  As they should start from 0
  
  '''
  if images_src_pth==None:
    images_root= coco_labels_pth.parent
  else:
    images_root=Path(images_src_pth)


  yolo_labels_root_pth=Path(yolo_labels_root_pth)
  yolo_labels_root_pth.mkdir(exist_ok=True,parents=True)
  

  yolo_train_pth = yolo_labels_root_pth/'train'
  yolo_train_pth.mkdir(exist_ok=True)
  yolo_valid_pth = yolo_labels_root_pth/'valid'
  yolo_valid_pth.mkdir(exist_ok=True)
  yolo_test_pth = yolo_labels_root_pth/'test'
  yolo_test_pth.mkdir(exist_ok=True) 


  coco_annotations = read_coco_labels(coco_labels_pth)
  coco_ann_imgs_df = pd.DataFrame(coco_annotations['images'])
  coco_train_df,coco_valid_df,coco_test_df = np.split(coco_ann_imgs_df,
                                                      [int(train_percent * len(coco_ann_imgs_df)),
                                            int((train_percent + val_percent) * len(coco_ann_imgs_df)),
                                            ])
  coco_ann_df = pd.DataFrame(coco_annotations['annotations'])

  
  #for split in ['train','valid','test']:
  saving_for_src_images(coco_train_df,coco_ann_df,
                        images_root,images_src_pth,
                        yolo_labels_root_pth,
                        'train',increment_by_one)
  print('Data and labels for Train Saved')
  saving_for_src_images(coco_valid_df,coco_ann_df,
                        images_root,images_src_pth,
                        yolo_labels_root_pth,
                        'valid',increment_by_one)
  print('Data and labels for Validation Saved')
  saving_for_src_images(coco_test_df,coco_ann_df,
                        images_root,images_src_pth,
                        yolo_labels_root_pth,
                        'test',increment_by_one)
  print('Data and labels for Test Saved')

  # Now saving data.yaml
  selected_labels=[i['name'] for i in coco_annotations['categories']]

  yaml_obj = open(str(yolo_labels_root_pth/'data.yaml'),'a')
  yaml_obj.write('names:')
  yaml_obj.write('\n')


  for label in selected_labels:
    yaml_obj.write(f'- {label}')
    yaml_obj.write('\n')
  yaml_obj.write(f'nc: {len(selected_labels)} \n')
  yaml_obj.write(f'train: {yolo_labels_root_pth}/train/images \n')
  yaml_obj.write(f'val: {yolo_labels_root_pth}/valid/images \n')
  yaml_obj.write(f'test: {yolo_labels_root_pth}/test/images \n')
 

  yaml_obj.close()








