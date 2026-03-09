from transformers import pipeline
from ultralytics import YOLO

import numpy as np
from PIL import Image
import cv2
import os
from collections import deque
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = '1'

if __name__ == "__main__":

    # Object segmentation
    seg_model = YOLO('yolov8n-seg.pt')

    # depth anything
    pipe = pipeline(
        task="depth-estimation", 
        model="depth-anything/Depth-Anything-V2-Small-hf",
        device='mps')

    depths = deque(maxlen=5)
    contours = None
    image_mask = None

    video = cv2.VideoCapture(0)
    logo = cv2.imread('./letters.png')

    while video.isOpened():
        ret, frame_bgr = video.read()
        # Segmentation (only persons, class==0)
        segm_output = seg_model.predict(frame_bgr, classes=[0], retina_masks=True)
        masks = segm_output[0].masks
        
        # Convert tensor to mask
        if masks is not None and ret:
            contours = masks.xy[0].astype(np.int32)
            image_mask = masks.data.numpy()[0, :, :].astype(np.uint8)*255

            frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
            frame_pil = Image.fromarray(frame_rgb)

            # Depth estimation and mask extraction
            preds = pipe(frame_pil)
            depth2show = preds["depth"]
            depth2show = np.asarray(depth2show)
            
            # visualization
            image_mask = np.stack((image_mask,)*3, axis=-1)
            cv2.drawContours(image_mask, [contours], -1, (255,255,0), 6)

            depth2show = cv2.resize(depth2show, fx=0.5, fy=0.5, dsize=None)
            image_mask = cv2.resize(image_mask, fx=0.5, fy=0.5, dsize=None)

            depth2show = cv2.normalize(
                depth2show, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

            depth2show = cv2.applyColorMap(depth2show, cv2.COLORMAP_JET)

            img2show = np.vstack((depth2show, image_mask))
    
            cv2.imshow('Depth', img2show)
            cv2.waitKey(10)