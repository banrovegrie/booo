import os
from nudenet import NudeClassifierLite
# from nudenet import NudeClassifier
from nudenet import NudeDetector
import requests
import shutil
import PIL
from PIL import ImageOps, ImageFilter
import numpy as np

def read_image(path):
    try:
        image = PIL.Image.open(path)
        return image
    except Exception as e:
        print(e) 

def read_from_url(url):
    ext = url.split('.')[-1]
    response = requests.get(url, stream=True, )
    with open(f'test_image.{ext}', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    return read_image(f"test_image.{ext}")

detector = NudeDetector()
# classifier = NudeClassifierLite()

def show(image):
    image_arr = np.array(image)
    plt.imshow(image_arr)

def make_boxes(result):
    not_allowed = ['EXPOSED_BREAST_F','EXPOSED_BUTTOCKS' ,'EXPOSED_ANUS','EXPOSED_GENITALIA_F','EXPOSED_GENITALIA_M']
    boxes = []
    for item in result:
        if item['label'] in not_allowed:
            boxes.append(item['box'])
    return boxes

def add_boxes(image, top_image, boxes):
    scale_factor = 1.25
    blur_depth = 0
    for box in boxes:
        w = int(abs(box[3] - box[1])*scale_factor)
        h = int(abs(box[2] - box[0])*scale_factor)
        corner = (box[0], box[1])
        new_top = top_image.resize((h,w))
        ic = image.crop(box)
        for i in range(blur_depth):
            ic = ic.filter(ImageFilter.BLUR)
        image.paste(ic,box)
        image.paste(new_top,box=corner, mask=new_top)
        print("added pumpkin")
    return image

def classify(addr):
    global classifier
    # classifier = NudeClassifier()
    #print(classifier.classify(addr)[addr]['unsafe'])
    unsafeness = classifier.classify(addr)[addr]['unsafe']
    print(unsafeness)
    return unsafeness

def save_img(url_addr, ext):
    response = requests.get(url_addr, stream=True)
    with open(f'./images/test_image{ext}', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

def detect(addr, top_image_addr):
    global detector
    result = detector.detect(addr, mode='fast')
    print(result)
    boxes = make_boxes(result)
    print(f"boxes {boxes}")
    nude = PIL.Image.open(addr)
    top_image = PIL.Image.open(top_image_addr)
    nude = add_boxes(nude,top_image,boxes)
    return boxes, nude