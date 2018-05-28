from sklearn.cluster import KMeans
import numpy as np
import tensorflow as tf
from tensorflow.contrib import factorization
import os

class KMeans_processor():
    def __init__(self, pix_data, max_color):
        super(KMeans_processor, self).__init__()
        h, w, d = pix_data.shape
        self.pix_data = np.reshape(pix_data, (h * w, d))
        self.max_color = max_color
        self._KMeans = KMeans(n_clusters=max_color)
    
    def quantize(self):
        self._KMeans.fit(self.pix_data)
        return np.array(self._KMeans.cluster_centers_, dtype=np.uint8)


class KMeans_TF_processor():
    def __init__(self, pix_data, max_color):
        super(KMeans_TF_processor, self).__init__()
        h, w, d = pix_data.shape
        self.pix_data = np.reshape(pix_data, (h * w, d))
        self.max_color = max_color

    def quantize(self):
        #sess = tf.Session()
        tf.device('/gpu:0')
        get_inputs = lambda: tf.train.limit_epochs(tf.convert_to_tensor(self.pix_data, dtype=np.float32), num_epochs=1)
        #print(sess.run(tf.convert_to_tensor(self.pix_data, dtype=np.float32)[0,:]))
        cluster = factorization.KMeansClustering(
            num_clusters=self.max_color,
            initial_clusters=factorization.KMeansClustering.KMEANS_PLUS_PLUS_INIT,
            model_dir='./color_model/'
        )
        cluster.train(input_fn=get_inputs, steps=2000)
        return cluster.cluster_centers()
    
