from PIL import Image
import os

def desaturate(data):
    R = data[::3]
    G = data[1::3]
    B = data[2::3]
    pixels = zip(R, G, B)
    averaged = []
    for pixel in list(pixels):
        avg = int(sum(pixel)/len(pixel))
        averaged.append((avg, avg, avg))
    unzipped = list(zip(*averaged))
    new_R = list(unzipped[0])
    new_G = list(unzipped[1])
    new_B = list(unzipped[2])
    new_data = []
    for index in range(len(new_R)):
        new_data.append(new_R[index])
        new_data.append(new_G[index])
        new_data.append(new_B[index])
    new_bytes = bytes(new_data)
    return new_bytes


def process(path):
    img = Image.open(path)
    if img.mode == 'RGB':
        data = img.tobytes()
        new_data = desaturate(data)
        new_img = Image.frombytes(img.mode, img.size, new_data)
        new_img.save(path.replace('.', '_desaturated.'))
    else:
        print('Unknown image mode')

def process_folder(folder):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            process(path)
        elif os.path.isdir(path):
            process_folder(path)
