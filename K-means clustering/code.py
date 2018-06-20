from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse # not using here
import cv2
import numpy


def centroid_histogram(cluster):
    numlabels = numpy.arange(0, len(numpy.unique(cluster.labels_))+1)
    print(numlabels)
    (hist,_) = numpy.histogram(cluster.labels_, bins=numlabels)
    hist = hist.astype("float")
    hist = hist/hist.sum() # histogram normalisation
    return hist

def plot_colors(hist, colors):
    bar = numpy.zeros((50,300,3),dtype="uint8")
    startX = 0
    for(percent, color) in zip(hist, colors):
        endX = startX + (percent*300)
        cv2.rectangle(bar, (int(startX),0), (int(endX),50),color.astype("uint8").tolist(), -1)
        startX = endX
        #print(color) - prints like [241.23533618 227.47566556   4.19686822]---RGB
    return bar



'''ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
ap.add_argument("-c", "--clusters", required=True)
args = vars(ap.parse_args())'''


image = cv2.imread("sample.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #  BGR for matplotlib



image = image.reshape((image.shape[0]*image.shape[1],3))
cluster = KMeans(n_clusters=5)
cluster.fit(image)


hist = centroid_histogram(cluster)
bar = plot_colors(hist, cluster.cluster_centers_)  # cluster.cluster_centers_ gives array of colours of k(=5) subsets
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()

