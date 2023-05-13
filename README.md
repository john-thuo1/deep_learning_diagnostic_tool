# deep_learning_diagnostic_tool
The repo contains an implementation of a diagnostic tool used to classify chest related x -ray images of diseases such as Tuberculosis and Pneumonia. To develop the tool, VGG-19 pretrained model from imagenet was used.


# Model Performances
To build the image diagnostic tool, 3 X-ray Image datasets were used : Tuberculosis Dataset with 2 classes (Normal and Tuberculosis) of 1400 images, BreastCancer Dataset containing 2 classes(benign and Malignant) with 647 images & Pneumonia Dataset containing 2 classes(pneumonia and normal) with 1270 images. <br />
To construct the model, the concept of Transfer Learning was employed, utilizing the vgg19 convolutional neural network from imagenet. <br /> 
Three distinct models were then developed using these datasets to address various inefficiencies. These include tackling issues such as inaccurate image classification caused by human errors, overwhelmed doctors faced with a substantial influx of patients requiring X-ray image interpretations, high costs associated with imaging and subsequent diagnose.<br />
The results on the test data were as shown in the following Confusion matrix graphs and classification reports:  <br />

 1. ![image](https://github.com/john-thuo1/deep_learning_diagnostic_tool/assets/108690517/1157e87b-a4a6-4e63-a5d1-2ed0b17165c0) <br />
    Classification Report from Tuberculosis test data<br />
    ![image](https://github.com/john-thuo1/deep_learning_diagnostic_tool/assets/108690517/628113df-8011-4bba-827f-2db8f3aa560f)

 2.![image](https://github.com/john-thuo1/deep_learning_diagnostic_tool/assets/108690517/5e50919d-7eb3-4e4c-b806-ad1936b528f6) <br />
    Classification Report from Pneumonia test data<br />
    ![image](https://github.com/john-thuo1/deep_learning_diagnostic_tool/assets/108690517/ec7de1b0-8622-4e5a-b2a9-2696514c07c8)
    
 3.![image](https://github.com/john-thuo1/deep_learning_diagnostic_tool/assets/108690517/f040f3a6-f772-4fb4-b75d-be6207105e58)<br />
    Classification Report from Breast Cancer test data<br />
    ![image](https://github.com/john-thuo1/deep_learning_diagnostic_tool/assets/108690517/2110bdd8-df36-44ac-8efb-bf1670741b00)

