from kmeans import KMeans_processor, KMeans_TF_processor
import numpy as np
import cv2, json, time
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

new_height = 600
max_color = 6

def get_pix_data(movie_id, new_height):
    filename = 'poster/%s.jpg' % movie_id
    img = cv2.cvtColor(cv2.imread(filename, 1), cv2.COLOR_BGR2RGB)
    new_width = int(img.shape[1] * 600 / img.shape[0])
    img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
    return img

def get_theme(pix_data, max_color):
    theme = KMeans_TF_processor(pix_data, max_color).quantize()
    return theme.astype(np.uint8)

print('Loading processed data...')
with open('imdb_process.json') as f:
    movies = json.load(f)
print('Done.\n')

def img_palette(img, theme):
    pale = np.zeros((600, 162, 3), dtype=np.uint8)
    for y in range(600):
        pale[y,:,:] = np.array(theme[int(y / 100)], dtype=np.uint8)
    w = int(img.shape[1] * 600 / img.shape[0])
    img = cv2.resize(img, (w, 600), interpolation=cv2.INTER_CUBIC)
    result = np.zeros((600, w + 162, 3), dtype=np.uint8)
    for i in range(600):
        result[i,:,:] = np.array(list(img[i]) + list(pale[i]), dtype=np.uint8)
    #cv2.imwrite('main%d.jpg' % num, result)

themefile = open('poster_theme.json', 'w')

themefile.write('[\n')
tf.device('/gpu:0')
for m in movies:
    try:
        film_id = list(m.keys())[0]
        start = time.process_time()
        pix_data = get_pix_data(film_id, new_height)
        theme = get_theme(pix_data, max_color)
        while (theme[:, 0] == theme[:, 1]).all() and (theme[:, 1] == theme[:, 2]).all():
            print('Film {0} All equal. Calculate again.'.format(film_id))
            os.system('rm -rf ./color_model/*')
            theme = get_theme(pix_data, max_color) 
        os.system('rm -rf ./color_model/*')
        print([[int(j) for j in list(i)] for i in list(theme)])
        themefile.write(json.dumps({film_id:[[int(j) for j in list(i)] for i in list(theme)]}) + ',\n')
        print("Film {0}: KMeans Time cost: {1}".format(film_id, round(time.process_time() - start, 6)))
        #img_palette(pix_data, theme)
    except:
        print('Error!')
        continue

themefile.write('{}]\n')
themefile.close()