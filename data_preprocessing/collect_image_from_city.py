import shutil
import os

gtFINE_TRAIN_DIR = "../../data/gtFine/train"
gtFINE_TEST_DIR = "../../data/gtFine/test"
gtFINE_VAL_DIR = "../../data/gtFine/val"
leftImg8bit_TRAIN_DIR = "../../data/leftImg8bit/train"
leftImg8bit_TEST_DIR = "../../data/leftImg8bit/test"
leftImg8bit_VAL_DIR = "../../data/leftImg8bit/val"

DATA_DIR = [gtFINE_TRAIN_DIR,
            gtFINE_TEST_DIR,
            gtFINE_VAL_DIR,
            leftImg8bit_TRAIN_DIR,
            leftImg8bit_TEST_DIR,
            leftImg8bit_VAL_DIR]

for data_DIR in DATA_DIR:
    for city in os.listdir(data_DIR):
        city_DIR = "{}/{}".format(data_DIR, city)
        for filename in os.listdir(city_DIR):
            shutil.move("{}/{}".format(city_DIR, filename), "{}/{}".format(data_DIR, filename))
        os.rmdir(city_DIR)