import os 

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


# def save_xml():
#     # os.mkdir('label{}.csv'.format(j+1))
#     with open ('TLCM_Dataset/bad_leaf{}.xml'.format(j+1), 'wt') as f:
#         writer = csv.writer(f)
#         row0 = ('<annotation>')
#         row1 = ('<folder>TLCM_Dataset</folder>')
#         row2 = ('<filename>bad_leaf{}</filename>'.format(ii+1))
#         row3 = ('<path>bad_leaf{}</path>'.format(ii+1))
#         row4 = ('<source>')
#         row5 = ('<database>Unknown</database>')
#         row6 = ('</source>')
#         row7 = ('<size>')
#         row8 = ('<width>{}</width>'.format(ow))
#         row9 = ('<height>{}</height>'.format(oh))
#         row10 = ('<depth>{}</depth>'.format(oc))
#         row11 = ('</size>')
#         row12 = ('<segmented>0</segmented>')
#         writer.writerow([row0])
#         writer.writerow([row1])
#         writer.writerow([row2])
#         writer.writerow([row3])
#         writer.writerow([row4])
#         writer.writerow([row5])
#         writer.writerow([row6])
#         writer.writerow([row7])
#         writer.writerow([row8])
#         writer.writerow([row9])
#         writer.writerow([row10])
#         writer.writerow([row11])
#         writer.writerow([row12])
        
#         # writer.writerow(('Leaf', 'x1', 'y1', 'x2', 'y2'))
#         for i in range(k-1):
#             # row = ('1',var1[i][0], var1[i][1], var2[i][0], var2[i][1])
#             # writer.writerow(row)
#             rowr0 = ("<object>")
#             rowr1 = ('<name>bad</name>')
#             rowr2 = ('<pose>Unspecified</pose>')
#             rowr3 = ('<truncated>0</truncated>')
#             rowr4 = ('<difficult>0</difficult>')
#             rowr5 = ('<bndbox>')
#             rowr6 = ('<xmin>{}</xmin>'.format(temp_xy1[i][0]))
#             rowr7 = ('<ymin>{}</ymin>'.format(temp_xy1[i][1]))
#             rowr8 = ('<xmax>{}</xmax>'.format(temp_xy2[i][0]))
#             rowr9 = ('<ymax>{}</ymax>'.format(temp_xy2[i][1]))
#             rowr10 = ('</bndbox>')
#             rowr11 = ('</object>')
#             writer.writerow([rowr0])
#             writer.writerow([rowr1])
#             writer.writerow([rowr2])
#             writer.writerow([rowr3])
#             writer.writerow([rowr4])
#             writer.writerow([rowr5])
#             writer.writerow([rowr6])
#             writer.writerow([rowr7])
#             writer.writerow([rowr8])
#             writer.writerow([rowr9])
#             writer.writerow([rowr10])
#             writer.writerow([rowr11])

#         row_last = ('</annotation>')
#         writer.writerow(row_last)

def nosy_neighbors_elliminated(home, nosy_nb):
    """
    Remove deleted entries.
    """
    if len(home) >= 1 and len(nosy_nb) >= 1:
        for nb in nosy_nb:
            xx1, yy1, xx2, yy2 = nb[0][0], nb[0][1], nb[1][0], nb[1][1]
            # Increase the tolerance area by 20%.
            xx1, yy1, xx2, yy2 = int(1.2*xx1), int(1.2*yy1), int(1.2*xx2), int(1.2*yy2)
            for person in home:
                x1, y1, x2, y2 = person[0][0], person[0][1], person[1][0], person[1][1]
                if (xx1 < x1 < xx2) and (yy1 < y1 < yy2) and (xx1 < x2 < xx2) and (yy1 < y2 < yy2):
                    home.remove(person)
    return home


def get_box_area(tlc, brc):
    x1, y1, x2, y2 = tlc[0], tlc[1], brc[0], brc[1]
    area = abs(x2 - x1) * abs(y2 - y1)
    return area

if __name__ == '__main__':
    pass
