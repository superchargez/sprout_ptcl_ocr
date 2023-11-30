import os
imgdir = r'images'
config='--psm 6 --oem 3 -c tessedit_char_whitelist="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,_ @"'
savedir = os.path.join(imgdir, "saved")
savedir = r'images/saved'
image_counter = 1  # Initialize a counter for image filenames
