import os
import cv2 
import numpy as np


def ignore(x):
    pass


def save(img_file, shape, boxes):
    """
    Saves annotations to a text file in YOLO format,
    class, x_centre, y_centre, width, height
    """
    img_height = shape[0]
    img_width = shape[1]

    # Check if the Annotations folder is empty.

    if not os.path.exists('Annotations'):
        os.mkdir('Annotations')
        
    with open('Annotations/' + img_file + '.txt', 'w') as f:
        for box in boxes:
            x1, y1 = box[0][0], box[0][1]
            x2, y2 = box[1][0], box[1][1]
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            x_centre = int(width/2)
            y_centre = int(height/2)

            norm_xc = x_centre/img_width
            norm_yc = y_centre/img_height
            norm_width = width/img_width
            norm_height = height/img_height

            yolo_annotations = ['0', ' ' + str(norm_xc), ' ' + str(norm_yc), ' ' + str(norm_width), ' ' + str(norm_height), '\n']
            f.writelines(yolo_annotations)



def get_box_area(tlc, brc):
    x1, y1, x2, y2 = tlc[0], tlc[1], brc[0], brc[1]
    area = abs(x2 - x1) * abs(y2 - y1)
    return area


def draw_dotted_lines(img, pt1, pt2, color, thickness=1, style='dotted', gap=10):
    """
    Draw dotted lines. 
    Adopted from StackOverflow.
    """
    dist = ((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**0.5
    pts= []
    for i in  np.arange(0, dist, gap):
        r = i/dist
        x = int((pt1[0] * (1-r) + pt2[0] * r) + 0.5)
        y = int((pt1[1] * (1-r) + pt2[1] * r) + 0.5)
        p = (x,y)
        pts.append(p)

    if style == 'dotted':
        for p in pts:
            cv2.circle(img, p, thickness, color, -1)
    else:
        s = pts[0]
        e = pts[0]
        i = 0
        for p in pts:
            s = e
            e = p
            if i%2 == 1:
                cv2.line(img, s, e, color, thickness)
            i += 1
