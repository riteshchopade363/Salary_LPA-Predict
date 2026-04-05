Salary_LPA Prediction is a Machine Learning project based on Linear Regression that estimates a candidate’s expected salary package (LPA). It analyzes factors like academic performance, skills, internships, and experience to predict salary. The model is integrated with a Flask web app for real-time predictions through a simple user interface.

Project Workflow (Step-by-Step)
🔹 Step 1: Data Collection
Dataset contains student details like marks, skills, internships, experience, etc.

🔹 Step 2: Data Preprocessing
Handle missing values
Convert categorical data into numeric format
Clean and prepare dataset

🔹 Step 3: Model Training
Apply Linear Regression algorithm
Train model using input features
Evaluate model performance

🔹 Step 4: Save Model
import pickle
pickle.dump(model, open('trained_model.pkl', 'wb'))

🌐 Web Application Flow
🔹 Step 5: User Opens App
python flask_app.py

Open in browser:
http://127.0.0.1:5000/

🔹 Step 6: Fill the Form
User enters:
Gender
Age
HSC Percentage
HSC Board
HSC Stream
Degree Percentage
Degree Field
Internships Count
Projects Count
Certifications Count
Technical Skills Score
Soft Skills Score
Aptitude Score
Communication Score
Work Experience (months)
Backlogs
<img width="1899" height="863" alt="Screenshot 2026-04-05 170058" src="https://github.com/user-attachments/assets/dc0f15b3-1919-4e4a-ae26-b2829deed8fe" />
<img width="1887" height="851" alt="Screenshot 2026-04-05 170119" src="https://github.com/user-attachments/assets/1f7286b4-8a3e-4295-ba7a-df7a5453f2fb" />

Step 7: Submit Form
Click on Submit button
🔹 Step 8: Prediction Process
Data is sent to Flask backend
Model processes the input
Linear Regression predicts salary

Step 9: View Result
💰 Predicted Salary shown in LPA (Lakhs Per Annum)
<img width="1918" height="860" alt="Screenshot 2026-04-05 170034" src="https://github.com/user-attachments/assets/ba46572e-59f7-445a-91cc-9e9e709ce11e" />


