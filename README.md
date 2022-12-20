# Automated Annotation Tool

Single class automated image annotation tool. Check out accompanying blog post [Automated Annotation using OpenCV](https://learnopencv.com/automated-image-annotation-tool-using-opencv-python/).

<img src="https://learnopencv.com/wp-content/uploads/2022/12/annotation-tool.gif" alt="Automated Annotation Tool OpenCV" width="900">

## Example Use Cases
<img src="https://learnopencv.com/wp-content/uploads/2022/11/stags-and-boars-image-annotation-tool-opencv-contour-analysis.png" alt="Automated Annotation pyOpenAnnotate" width="900">


## Annotate Images

```
annotate --img <images_directory_path>
```

## Annotate Video
```
annotate --vid <path_to_video_file>
```
## Global Flags
```
-T : View mask window.
--resume <existing-annotations-dir>: Continue from where you left off.
--skip <int(Frames)> : Frames to skip while processing a video file.
```

## Mouse Controls
```
Click and Drag: Draw bounding boxes.
Double Click: Remove existing annotation.
```
## Keyboard Navigation
```
N or D : Save and go to next image
B or A : Save and go back
C : Toggle clear screen 
T : Toggle mask window
Q : Quit
```
