import os
from nudenet import NudeClassifierLite
# from nudenet import NudeClassifier
from nudenet import NudeDetector
import requests
import shutil

def classify(addr):
    classifier = NudeClassifierLite()
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

def detect(addr):
    detector = NudeDetector()
    result = detector.detect(addr, mode='fast')
    # result = detector.detect(addr)
    return result
