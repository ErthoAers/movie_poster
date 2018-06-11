from calculate_max_color import get_pix_data, get_theme
import numpy as np
import os, json
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

with open('label_list.json') as f:
    label_list = json.load(f)

color = {}
for k, v in label_list['color'].items():
    pix = np.concatenate([get_pix_data(i, 60) for i in v])
    theme = get_theme(pix, 6)
    color[k] = [list(i) for i in theme]
    print('%s: ' + theme)

print(color)