# Customer-Churn-Analysis


Summary

This Jupyter Notebook provides an end-to-end analysis of customer churn using a real-world dataset. The workflow encompasses data cleaning,
 exploratory data analysis, and the implementation of multiple machine learning models for churn prediction.

## Key Highlights

- **Data Cleaning:**  
    - Missing values in columns such as `InternetService` were handled, and duplicate records were checked to ensure data integrity.
    - The dataset contains a total of `df.shape[0]` rows and `df.shape[1]` columns, providing a substantial sample for analysis.

- **Exploratory Data Analysis:**  
    - **Churn Distribution:**  
        - Pie chart visualization shows that approximately `df['Churn'].value_counts(normalize=True).round(2)*100`% of customers have churned, while the remaining have stayed.
    - **Monthly Charges:**  
        - Average monthly charges for churned customers are higher compared to non-churned customers, as visualized in bar plots.
    - **Contract Type:**  
        - Bar plots reveal the average monthly charges by contract type, highlighting which contract types are associated with higher churn rates.
    - **Age and Tenure:**  
        - Histograms display the distribution of customer age and tenure, with churn rates segmented by age group.
    - **Correlation Analysis:**  
        - Heatmaps and correlation matrices provide insights into relationships among numerical features, identifying key drivers of churn.

- **Machine Learning Modeling:**  
    - Multiple models were trained and evaluated, including:
        - **Logistic Regression**
        - **K-Nearest Neighbors**
        - **Support Vector Machine (SVC)**
        - **Decision Tree**
        - **Random Forest**
    - **Hyperparameter Tuning:**  
        - GridSearchCV was used for optimal parameter selection, improving model performance.
    - **Model Performance:**  
        - The SVC model achieved the highest accuracy, outperforming other models.  
        - Accuracy scores for each model were reported, with the best model exceeding `accuracy_score(y_test, y_pred)*100`%.
  - **Web Predictions:**
    - Using Streamlit & joblib for customer churn prediction.  

## Visual Insights

- Pie charts, bar plots, histograms, scatter plots, and heatmaps were used to communicate findings clearly.
- Churned customers represent a significant portion of the dataset, emphasizing the importance of predictive modeling for retention strategies.

## Conclusion

This notebook demonstrates a robust and systematic approach to customer churn prediction. By combining thorough data exploration, detailed visualizations,
 and advanced machine learning techniques, actionable insights were derived to support business decision-making. The best-performing model is ready for deployment,
  enabling proactive measures to reduce churn and improve customer retention.




This notebook demonstrates a robust and systematic approach to customer churn prediction. By combining thorough data exploration, detailed visualizations,
 and advanced machine learning techniques, actionable insights were derived to support business decision-making. The best-performing model is ready for deployment,
  enabling proactive measures to reduce churn and improve customer retention.
