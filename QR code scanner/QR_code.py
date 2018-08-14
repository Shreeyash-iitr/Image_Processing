from pyzbar import pyzbar
import cv2
import numpy
import urllib
import imutils
url = "http://10.42.0.23:8080/shot.jpg"

while True:
    img = urllib.request.urlopen(url)
    img = numpy.array(bytearray(img.read()),dtype=numpy.uint8)
    img = cv2.imdecode(img, -1)
    img = imutils.resize(img, width=400)
    barcodes = pyzbar.decode(image=img)
    for barcode in barcodes:
        print("found")
        (x, y, w, h) = barcode.rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        data = barcode.data.decode('utf-8')
        type = barcode.type
        text = "{}({})".format(data, type)
        cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

