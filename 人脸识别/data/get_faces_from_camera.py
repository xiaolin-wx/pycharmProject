import dlib
import numpy as np
import cv2
import os
import shutil
import time
import logging

detector = dlib.get_frontal_face_detector()

class Face_Register:
    def __init__(self):
        self.path_photos_from_camera = "data_faces_from_camera/"
        self.font = cv2.FONT_ITALIC

        self.existing_faces_cnt = 0
        self.ss_cnt = 0
        self.current_frame_faces_cnt = 0

        self.save_flag = 1
        self.press_n_flag = 0

        self.frame_time = 0
        self.frae_start_time = 0
        self.fps = 0

    def pre_work_mkdir(self):
        if os.path.isdir(self.path_photos_from_camera):
            pass
        else:
            os.mkdir(self.path_photos_from_camera)

    def pre_work_del_old_face_folders(self):
        folders_rd = os.listdir(self.path_photos_from_camera)
        for i in range(len(folders_rd)):
            shutil.rmtree(self.path_photos_from_camera+folders_rd[i])
        if os.path.isfile("data/features_all.csv"):
            os.remove("data/features_all.csv")

    def check_existing_faces_cnt(self):
        if os.listdir("data_faces_from_camera/"):
            person_list = os.listdir("data_faces_from_camera/")
            person_num_list = []
            for person in person_list:
                person_num_list.append(person.split("_")[-1])
            self.existing_faces_cnt = max(person_num_list)

        else:
            self.existing_faces_cnt = 0

    def update_fps(self):
        now = time.time()
        self.frame_time = now - self.frae_start_time
        self.fps = 1.0/ self.frame_time
        self.frae_start_time = now

    def draw_note(self, img_rd):
        cv2.putText(img_rd, "Face Register", (20, 40), self.font, 1, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img_rd, "Faces" + str(self.current_frame_faces_cnt), (20, 40), self.font, 0.8, (0, 255, 0), 1 , cv2.LINE_AA)
        cv2.putText(img_rd, "N: Create face folder", (20, 350), self.font, 0.8, (255, 255, 255), 1 , cv2.LINE_AA)
        cv2.putText(img_rd, "S: Sava current face", (20, 400), self.font, 0.8, (255, 255, 255), 1 , cv2.LINE_AA)
        cv2.putText(img_rd, "Q: Quit", (20, 450), self.font, 0.8, (255, 255, 255), 1 , cv2.LINE_AA)

    def process(self, stream):
        self.pre_work_mkdir()
        self.check_existing_faces_cnt()

        while stream.isOpened():
            flag, img_rd = stream.read()
            kk = cv2.waitKey(1)
            faces = detector(img_rd, 0)

            if kk == ord("n"):
                self.existing_faces_cnt += 1


