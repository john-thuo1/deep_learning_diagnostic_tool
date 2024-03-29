# Problem
The misclassification of chest X-ray images depicting diseases like Pneumonia, Tuberculosis, and Breast Cancer presents a significant challenge in healthcare. Accurate interpretation of these images is crucial for timely diagnosis and appropriate treatment planning. In Africa, during the period of 2020-2021, a substantial number of individuals were identified with these diseases, and unfortunately, a considerable proportion succumbed to late image reading or inaccurate interpretations by doctors. The statistics reveal that out of the total population screened for chest X-rays, approximately 20% were misclassified, leading to delayed intervention and compromised patient outcomes.<br />

Moreover, the cost associated with obtaining accurate image interpretations is high, particularly in rural areas where healthcare facilities are limited. This financial burden further exacerbates the problem, preventing patients from accessing timely and accurate diagnoses, thereby compromising their chances of recovery. Addressing these challenges is essential to improve healthcare outcomes, reduce mortality rates, and enhance the affordability and availability of diagnostic services in resource-constrained regions.


# Proposed Solution
To address the challenges posed by misclassification of chest X-ray images in diseases such as Pneumonia, Tuberculosis, and Breast Cancer, a solution leveraging Convolutional Neural Networks (CNNs) and deep learning(DL) can be implemented. By utilizing transfer learning techniques and the VGG19 CNN architecture, an image diagnostic tool can classify these images, aiding in timely and imporved accurate diagnoses, hence reducing the number of False Positives and Negatives.

The proposed solution involves a doctor uploading the patient's X-ray images to the tool, which applies the trained CNN model to analyze and classify the images. The output result is then reviewed by the doctor, who further verifies it based on their expertise in the medical field. This collaborative approach ensures a reliable diagnosis while saving time and cost.

By implementing this solution, doctors and hospitals particularly in rural areas can diagnose a larger number of patients at a cheaper rate, significantly reducing the burden of late image reading or inaccurate interpretations. This tool not only enhances diagnostic accuracy but also complements the doctor's clinical expertise, enabling them to provide more efficient and affordable healthcare services to the population. Ultimately, this solution contributes to improved healthcare outcomes, reduced mortality rates, and increased accessibility of accurate diagnostic services in resource-constrained regions, as highlighted in the problem statement.


# Models Performances
To build the current image diagnostic tool, 3 X-ray Image datasets were used : Tuberculosis Dataset with 2 classes (Normal and Tuberculosis) of 1400 images, BreastCancer Dataset containing 2 classes(benign and Malignant) with 647 images & Pneumonia Dataset containing 2 classes(pneumonia and normal) with 1270 images. <br />
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


# Steps to run the Application Locally
1. Download all the models required for this application from :
 [here](https://drive.google.com/drive/folders/1T4mN9k_82RwVyT1Ad9eYFEjT_GW3ineZ?usp=sharing).
 
2. Git clone this repository and set up a virtual env on your project.
3. Run this command on your Project's terminal run : pip install -r requirements.txt . This will install all the dependencies used.
4. Followed by this command : streamlit run home_page.py
5. Check your browser for the running project

# Future Steps
1. Increasing dataset complexities. Such include increasing the number of classes for each disease. e.g Breast Cancer could either be malignant, benign or normal. Same to the other datasets.
2. Using larger datasets to improve on the accuracy of the model. Techniques I could apply on the current datasets include Data Augmentation but I currently don't have enough Computing Resources to do so.
3. Adding more models trained on other diseases.
4. Research and implementation of  better performing algorithms for faster and more accurate Image Classification.
5. Further Testing on the models included and researching on the overall implication of having such a tool in various Hospitals in rural areas.

