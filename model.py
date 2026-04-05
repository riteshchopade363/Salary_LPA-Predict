import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


df = pd.read_csv('clean_data.csv')

x=df[['gender' , 'age' , 'hsc_percentage' , 'hsc_board' , 'hsc_stream' , 'degree_percentage' , 'degree_field' , 'internships_count' , 'projects_count' ,
      'certifications_count' , 'technical_skills_score' , 'soft_skills_score' , 'aptitude_score' , 'communication_score' , 'work_experience_months' ,
      'backlogs' , 'placed']]

y=df['salary_lpa']

model = LinearRegression()

model.fit(x, y)

fh = open('trained_model.pkl', 'wb')
pickle.dump(model, fh)
fh.close()