from roboflow import Roboflow
rf = Roboflow(api_key="Y2LRE9e8VH3wgMyRBF3H")
project = rf.workspace("drone-dataset-mvh8i").project("detection-bzujh")
dataset = project.version(1).download("yolov5")
