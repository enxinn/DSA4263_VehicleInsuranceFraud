# Abstract

Insurance fraud poses a major challenge to the industry, leading to significant financial losses, higher premiums and heavy manual investigation workload. To tackle this issue, our project develops a machine learning model to detect fraudulent vehicle insurance claims using a dataset containing 15,420 records. The dataset is highly imbalanced, with only around 6% fraudulent cases, making accurate detection difficult. 

After data cleaning, feature engineering, and exploratory data analysis, multiple resampling techniques were tested to handle imbalance, with SMOTEENN selected for providing the best minority-class detection. Several models were then trained, including Logistic Regression, Decision Tree, Random Forest, LightGBM, XGBoost and SVC. Among all models, a tuned LightGBM achieved the strongest performance, with a PR-AUC of 0.69, precision of 0.60 and recall of 0.67 on the test set, showing a good balance between identifying fraud and controlling false alarms.

Explainability method SHAP was used to explain the model’s prediction, revealing that features related to fault, policy type, deductibles, and claim timing strongly influence predictions. Fairness testing showed that the model performed unevenly across age groups, particularly for older policyholders, indicating potential bias that should be addressed before deployment.

Overall, the model demonstrates strong potential to support fraud investigators, reduce operational costs and offer insights into fraud patterns. Recommendations include targeted review strategies, better monitoring of first-time claimants, and complementing the model with tools such as graph analytics and NLP for enhanced fraud detection.


