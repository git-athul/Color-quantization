from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

# opens image
im = Image.open("example.jpg")
im.show()

# get pixel values from image
data = np.array(im.getdata())

# Kmeans learning
kmeans = KMeans(n_clusters=5, random_state=0).fit(data)
centers = kmeans.cluster_centers_.astype(int)


# Showing output
width = 128
height =128
palette = Image.new('RGB', (width*len(centers), height))
for i in range(len(centers)):
    col = Image.new("RGB", (width, height), tuple(centers[i]))
    palette.paste(col, (width*i,0))
palette.show()





