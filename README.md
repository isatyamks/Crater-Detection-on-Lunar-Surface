# Crater and Boulder Detection from OHRC Images

## Team: Shershaah

### Objectives

1. **Model Design**: Develop an AI/ML model to automatically detect all craters and boulders in OHRC images regardless of their shape, size, and illumination conditions.
2. **Quantification**: The model should quantify the selenographic position and diameter of the detected craters and boulders.

### Expected Outcomes

- Generate a polygonal shape file or provide shape-size information of craters and boulders with their location on the OHRC images.

### Dataset

- **Source**: OHRC datasets publicly available in PDS4 format on Chandrayaan Map Browse.

### Suggested Tools/Technologies

- **Programming Languages**: Python, C, C++
- **Techniques**: Image processing techniques for crater detection, AI/ML models for crater/boulder detection

### Steps to Achieve Objectives

1. **Selenoreference OHRC Images**:
   - Download OHRC images.
   - Utilize auxiliary information provided with the images to apply appropriate projection information and selenoreference the images.

2. **Data Preparation**:
   - Prepare the training and testing datasets from the OHRC images.
   - Annotate the datasets with craters and boulders for supervised learning.

3. **Model Training**:
   - Train the AI/ML model using the prepared datasets.
   - Employ image processing techniques to enhance detection accuracy.

4. **Model Evaluation**:
   - Develop evaluation metrics to assess the accuracy of the model.
   - Measure precision and recall to ensure the model detects craters and boulders accurately.

5. **Shape File Generation**:
   - Create a polygonal shape file for detected craters and boulders.
   - Include shape-size information and location coordinates in the shape file.

### Evaluation Parameters

- **Accuracy**: Precision of detected craters and boulders compared to actual craters and boulders in the image.
- **Relevance**: The degree to which detected craters and boulders and their associated information match the actual craters and boulders.

---

This README provides a structured approach to developing an AI/ML model for the detection of craters and boulders from OHRC images, ensuring all steps are well-defined and achievable.
