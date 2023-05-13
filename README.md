# Problem
The misclassification of chest X-ray images depicting diseases like Pneumonia, Tuberculosis, and Breast Cancer presents a significant challenge in healthcare. Accurate interpretation of these images is crucial for timely diagnosis and appropriate treatment planning. In Africa, during the period of 2020-2021, a substantial number of individuals were identified with these diseases, and unfortunately, a considerable proportion succumbed to late image reading or inaccurate interpretations by doctors. The statistics reveal that out of the total population screened for chest X-rays, approximately 20% were misclassified, leading to delayed intervention and compromised patient outcomes.<br />
Moreover, the cost associated with obtaining accurate image interpretations is high, particularly in rural areas where healthcare facilities are limited. This financial burden further exacerbates the problem, preventing patients from accessing timely and accurate diagnoses, thereby compromising their chances of recovery. Addressing these challenges is essential to improve healthcare outcomes, reduce mortality rates, and enhance the affordability and availability of diagnostic services in resource-constrained regions.
The repo contains an implementation of a diagnostic tool used to classify chest related x -ray images of diseases such as Tuberculosis and Pneumonia. To develop the tool, VGG-19 pretrained model from imagenet was used.

# Proposed Solution
To address the challenges posed by misclassification of chest X-ray images in diseases such as Pneumonia, Tuberculosis, and Breast Cancer, a solution leveraging Convolutional Neural Networks (CNNs) and deep learning(DL) can be implemented. By utilizing transfer learning techniques and the VGG19 CNN architecture, an automated tool can accurately classify these images, aiding in timely and accurate diagnoses.

The proposed solution involves a doctor uploading the patient's X-ray images to the tool, which applies the trained CNN model to analyze and classify the images. The output result is then reviewed by the doctor, who further verifies it based on their expertise in the medical field. This collaborative approach ensures a reliable diagnosis while saving time and cost.

By implementing this solution, doctors and hospitals particularly in rural areas can diagnose a larger number of patients at a cheaper rate, significantly reducing the burden of late image reading or inaccurate interpretations. This tool not only enhances diagnostic accuracy but also complements the doctor's clinical expertise, enabling them to provide more efficient and affordable healthcare services to the population. Ultimately, this solution contributes to improved healthcare outcomes, reduced mortality rates, and increased accessibility of accurate diagnostic services in resource-constrained regions, as highlighted in the problem statement.

# Models Performances
To build the image diagnostic tool, 3 X-ray Image datasets were used : Tuberculosis Dataset with 2 classes (Normal and Tuberculosis) of 1400 images, BreastCancer Dataset containing 2 classes(benign and Malignant) with 647 images & Pneumonia Dataset containing 2 classes(pneumonia and normal) with 1270 images. <br />
To construct the model, the concept of Transfer Learning was employed, utilizing the vgg19 convolutional neural network from imagenet. <br /> 
Three distinct models were then developed using these datasets to address various inefficiencies. These include tackling issues such as inaccurate image classification caused by human errors, overwhelmed doctors faced with a substantial influx of patients requiring X-ray image interpretations, high costs associated with imaging and subsequent diagnose.<br />
The results on the test data were as shown in the following Confusion matrix graphs and classification reports:  <br />

 1. 
  ![image](https://github.com/john-thuo1/deep_learning_diagnostic_tool/assets/108690517/1157e87b-a4a6-4e63-a5d1-2ed0b17165c0) <br />
    Classification Report from Tuberculosis test data<br />
    ![image](https://github.com/john-thuo1/deep_learning_diagnostic_tool/assets/108690517/628113df-8011-4bba-827f-2db8f3aa560f)

 2.
  ![image](https://github.com/john-thuo1/deep_learning_diagnostic_tool/assets/108690517/5e50919d-7eb3-4e4c-b806-ad1936b528f6) <br />
    Classification Report from Pneumonia test data<br />
    ![image](https://github.com/john-thuo1/deep_learning_diagnostic_tool/assets/108690517/ec7de1b0-8622-4e5a-b2a9-2696514c07c8)
    
 3.
  ![image](https://github.com/john-thuo1/deep_learning_diagnostic_tool/assets/108690517/676d81f1-a02b-4ee6-8389-45e26ed48e0c)<br />
     Classification Report from Breast Cancer test data<br />
    ![image](https://github.com/john-thuo1/deep_learning_diagnostic_tool/assets/108690517/2110bdd8-df36-44ac-8efb-bf1670741b00)

