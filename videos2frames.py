from __future__ import print_function, division
import os
import sys
import subprocess
from PIL import Image
import ipdb

def class_process(dir_path, dst_dir_path, class_name):
    class_path = os.path.join(dir_path, class_name)
    if not os.path.isdir(class_path):
        return

    dst_class_path = os.path.join(dst_dir_path, class_name)
    if not os.path.exists(dst_class_path):
        os.mkdir(dst_class_path)

    for file_name in sorted(os.listdir(class_path)):
        if 'depth.avi' not in file_name:
            continue
        name, ext = os.path.splitext(file_name)
        dst_directory_path = os.path.join(dst_class_path, name)
        # ipdb.set_trace()
        video_file_path = os.path.join(class_path, file_name)
        try:
            if os.path.exists(dst_directory_path):
                if not os.path.exists(os.path.join(dst_directory_path, '000001.png')):
                    subprocess.call('rm -r \"{}\"'.format(dst_directory_path), shell=True)
                    print('remove {}'.format(dst_directory_path))
                    os.mkdir(dst_directory_path)
                else:
                    continue
            else:
                os.mkdir(dst_directory_path)
        except:
            print(dst_directory_path)
            continue
        # cmd = 'ffmpeg -i \"{}\" -r 30 -ss 00:00:00.030 -s 600*300 \"{}/%06d.png\"'.format(video_file_path, dst_directory_path)
        cmd = 'ffmpeg -i \"{}\" -r 30 -ss 00:00:00.030 -s 380*300 \"{}/%06d.png\"'.format(video_file_path, dst_directory_path)
        print(cmd)
        subprocess.call(cmd, shell=True)
        for frame_name in sorted(os.listdir(dst_directory_path)):
            frame_path = dst_directory_path+'/'+frame_name
            frame = Image.open(frame_path)
            # img = frame.crop([190,40,400,300])
            img = frame.crop([70,40,280,300])
            img.save(frame_path)
        # ipdb.set_trace()
        print('\n')


if __name__=="__main__":
    dir_path = '../videos/'
    dst_dir_path = '../frames/'

    for class_name in sorted(os.listdir(dir_path)):
        class_process(dir_path, dst_dir_path, class_name)
