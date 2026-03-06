import numpy as np
import cv2
import os 
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\User\Downloads\TarbosaurusGDI")
def get_diameters(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if img is None: return np.array([0])
    alpha = img[:, :, 3]
    _, mask = cv2.threshold(alpha, 200, 255, cv2.THRESH_BINARY)
    diameters = []
    for col in mask.T:
        pixels = np.where(col > 0)[0]
        if len(pixels) > 5:
            diameters.append(pixels[-1] - pixels[0])
        else:
            diameters.append(0)
    return np.array(diameters)

lat = get_diameters("tarbolat.png")
dors = get_diameters("tarbodors.png")
min_len = min(len(lat), len(dors))
lat, dors = lat[:min_len], dors[:min_len]
tarbo_length = 10
pixel_to_meter = len(lat)/tarbo_length
axial_gdi = np.pi * (lat / (2 * pixel_to_meter)) * (dors / (2 * pixel_to_meter))
v_axial = np.sum(axial_gdi) * (1 / pixel_to_meter)
leglat = get_diameters("tarboleglat.png")
legfront = get_diameters("tarbolegfront.png")
leg_min_len = min(len(leglat), len(legfront))
leglat, legfront = leglat[:leg_min_len], legfront[:leg_min_len]
v_one_leg = np.sum(np.pi * (leglat / (2 * pixel_to_meter)) * (legfront / (2 * pixel_to_meter))) * (1 / pixel_to_meter)


v_appendicular = (v_one_leg) * 2

v_total = (v_appendicular) + (v_axial)
