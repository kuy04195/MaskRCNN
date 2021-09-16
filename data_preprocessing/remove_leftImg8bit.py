import os
import re

leftImg8bit_DIR = "../../data/leftImg8bit"
subsets_DIR = ["{}/{}".format(leftImg8bit_DIR, subset) for subset in ['train', 'val', 'test']]

for subset in subsets_DIR:
    print(subset)
    files = os.listdir(subset)
    for f in files:
        try:
            newname = re.findall(r'(.+)_leftImg8bit.png$', f)[0]
            newname += '.png'
        except Exception as e:
            print(e)
            continue
        src_file = os.path.join(subset, f)
        dst_file = os.path.join(subset, newname)
        os.rename(src_file, dst_file)
#        print("Successfully rename {} -> {}".format(src_file, dst_file))