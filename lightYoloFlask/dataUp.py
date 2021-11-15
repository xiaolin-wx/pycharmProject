import numpy as np
import tensorflow
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img


def date_enhancement(img_input_path, img_output_path):
    image = load_img(img_input_path)
    image = img_to_array(image) #图像转为数组
    image = np.expand_dims(image, axis=0) #增加一个维度
    img_dag = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
                            height_shift_range = 0.1, shear_range = 0.2, zoom_range = 0.2,
                            horizontal_flip = True, fill_mode = "nearest") #旋转，宽度移动范围，高度移动范围，裁剪范围，水平翻转开启，填充模式

    img_generator = img_dag.flow(image, batch_size=1,
                                 save_to_dir=img_output_path,
                                 save_prefix = "image", save_format = "jpg")#测试一张图像bath_size=1
    count =0 #计数器
    for img in img_generator:
        count += 1
        if count == 15:  #生成多少个样本后退出
            break


if __name__ == "__main__":
    image_path =r"E:\Python\yolov5-master_light\data\images\0.jpg"
    image_out_path = r"E:\Python\yolov5-master_light\data\outimages"
    date_enhancement(image_path, image_out_path)
