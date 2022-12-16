# import cv2 
# img = cv2.imread('Dataset/5.jpg')

# height, width = img.shape[:2]
# print(height, width)
# with open('Annotations/5.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         name = line.replace('\n', '')
#         class_id, xc, yc, w, h = name.split(' ')
#         class_id = int(class_id)
#         xc, yc = float(xc), float(yc)
#         h, w = float(h), float(w)
#         # print(f"Class ID: {class_id}, Xc: {xc}, Yc: {yc}, Height: {h}, Width: {w}")
#         box_h = int(height*h)
#         box_w = int(width*w)
#         # print(xc - w/2)
#         x_center = int(xc*width)
#         y_center = int(yc*height)

#         x1 = x_center - int(box_w/2)
#         y1 = y_center - int(box_h/2)
#         x2 = x1 + box_w 
#         y2 = y1 + box_h

#         cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
# cv2.imshow('Validation', img)
# cv2.waitKey(0)