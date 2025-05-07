from pycocotools.coco import COCO
import cv2

def load_coco_annotations(json_path, image_dir):
    coco = COCO(json_path)
    image_ids = coco.getImgIds()
    data = []
    
    for img_id in image_ids:
        img_info = coco.loadImgs(img_id)[0]
        img_path = f"{image_dir}/{img_info['file_name']}"
        ann_ids = coco.getAnnIds(imgIds=img_id)
        annotations = coco.loadAnns(ann_ids)
        
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        data.append({
            "image": image,
            "annotations": annotations,
            "file_name": img_info['file_name']
        })
    return data

train_data = load_coco_annotations("dataset/train/_annotations.coco.json", "dataset/train")