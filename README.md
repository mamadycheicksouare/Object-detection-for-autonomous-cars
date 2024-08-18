# Object-detection-for-autonomous-cars

Object detection for autonomous vehicles represents a transformative leap in the field of transportation technology. As self-driving cars become increasingly prevalent, their ability to navigate safely and efficiently through complex environments hinges on advanced perception systems. Central to these systems is object detection, a critical component that enables vehicles to identify and interpret various elements within their surroundings, including pedestrians, other vehicles, traffic signs, and obstacles.

The project focuses on developing and implementing an object detection system tailored for autonomous vehicles using YOLO algorithm and OpenCV.

The main goal of this project is to detect cars and traffic lights and provide these informations to a Reinforcement Learning model and train a self-driving car.

# Preparing the dataset
Dataset preparation is a crucial step in developing an object detection system for autonomous vehicles. It involves several key processes to ensure that the data used for training and testing the model is comprehensive, accurate, and representative of real-world conditions.
In this project the LISA Traffic light Dataset was used, also video captures from CARLA simulator were used to ensure the model works well in different
environments. 

ROBOFLOW was used for the annotation and preprocessing total of 500 images.

![lasttrain,png](https://github.com/user-attachments/assets/edeb8ad2-fd04-43d8-ab94-2a1d1179e6f3)

# Data training
Ultralytics YOLO version 8 was used to train the model over 100 epochs 


![training](https://github.com/user-attachments/assets/84c964b5-b809-40c4-9f38-112f6e68332b)

On a single image many traffic light can be detected, but which one are we going to take into consideration!! Good question!!!

To solve this problem a python function was written to find the biggest box after traffic light detection
Well, What about the light?

Similarly a function was written to find the color present inside the box. 

These functions can be found in the color_detection.py file.


![deneme](https://github.com/user-attachments/assets/1942326e-ba35-4606-8773-cc9c6c3a7cad)





![best](https://github.com/user-attachments/assets/367fc923-e0e8-4a36-a0c7-9f4f851a5e21)


After the model is trained only the Region of interests are given to a RL algorithm.
To obtain that ROI a mask can be used.
The final results after the projects are just bellow. 


![roi](https://github.com/user-attachments/assets/5d01cfe0-8bdf-4b5e-bbd6-a8b9987c54a1)





![last test](https://github.com/user-attachments/assets/736728a3-4d3e-442c-94fa-8ee0eede0fa6)
