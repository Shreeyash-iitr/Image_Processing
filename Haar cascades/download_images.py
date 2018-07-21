import urllib.request
import cv2
import numpy
import os

def store_raw_images():
    # Negative samples
    links =['http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00017222']
            #'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
            #'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    for url in links:
        neg_images_urls = urllib.request.urlopen(url).read().decode()

    if not os.path.exists('neg'):
        os.makedirs('neg')

    pic_num = 1497

    for i in neg_images_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, 'neg/'+str(pic_num)+'.jpg')
            img = cv2.imread('neg/'+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100,100))
            cv2.imwrite('neg/'+str(pic_num)+'.jpg', resized_image)
            pic_num += 1
        except Exception as e:
            print(str(e))


def find_uglies():
    for img in os.listdir('neg'):
        for ugly in os.listdir('uglies'):
            try:
                current_img_path = 'neg/'+str(img)
                ugly_image = cv2.imread('uglies/'+str(ugly))
                current_img = cv2.imread(current_img_path)
                if ugly_image.shape == current_img.shape and not(numpy.bitwise_xor(ugly_image, current_img).any()):
                    print('Deleting : ', current_img_path)
                    os.remove(current_img_path)
            except Exception as e:
                print(str(e))

def create_pos_n_neg():
    for img in os.listdir('neg'):
        line = 'neg/'+img+'\n'
        with open('bg.txt','a') as f:
            f.write(line)

#store_raw_images()
#find_uglies()
#create_pos_n_neg()
i=1
for img in os.listdir('neg'):
    print(i)
    i = i+1