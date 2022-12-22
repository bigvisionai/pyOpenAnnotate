# Automated Annotation Tool

Automate your image annotation pipeline using <b>pyOpenAnnotate</b>. It is built harnessing the power of OpenCV. Perfect for annotating single class datasets. Check out accompanying blog post to understand how <b>pyOpenAnnotate</b> has been designed. 

[Automated Image Annotation Tool Using OpenCV](https://learnopencv.com/automated-image-annotation-tool-using-opencv-python/).

<br>
<br>

<img src="https://learnopencv.com/wp-content/uploads/2022/12/annotation-tool.gif" alt="Automated Annotation Tool OpenCV" width="900">

## Example Use Cases
<img src="https://learnopencv.com/wp-content/uploads/2022/11/stags-and-boars-image-annotation-tool-opencv-contour-analysis.png" alt="Automated Annotation pyOpenAnnotate" width="900">

<img src="https://learnopencv.com/wp-content/uploads/2022/11/image-annotation-tool-strawberries-and-fishes-opencv-contour-analysis.png" alt="Automated Annotation pyOpenAnnotate" width="900">

## How To Use pyOpenAnnotate?
Annotating images using pyOpenAnnotate is pretty simple. Use the command `annotate` followed by the following flags as per the requirement.
### 1. Annotate Images

```
annotate --img <images_directory_path>
```

### 2. Annotate Video
```
annotate --vid <path_to_video_file>
```
### 3. Global Flags
```
-T : View mask window.
--resume <existing-annotations-dir>: Continue from where you left off.
--skip <int(Frames)> : Frames to skip while processing a video file.
```

### 4. Mouse Controls
```
Click and Drag: Draw bounding boxes.
Double Click: Remove existing annotation.
```

## Display Annotations
Visualize your annotations using the `showlbls` command.
```
showlbls --img <single_image_or_a_directory> --ann <single_annotation_text_file_or_a_directory>
```

## Keyboard Navigation
```
N or D : Save and go to next image
B or A : Save and go back
C : Toggle clear screen (during annotation)
T : Toggle mask window (during annotation)
Q : Quit
```
