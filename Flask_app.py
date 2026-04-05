from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('trained_model.pkl', 'rb'))

@app.route('/' , methods=['GET', 'POST'])
def salary():
    if request.method == 'GET':
        return  render_template('from.html')
    elif request.method == 'POST':
        gender = int(request.form.get('gender'))
        age = int(request.form.get('age'))
        hsc_percentage = float(request.form.get('hsc_percentage'))
        hsc_board = int(request.form.get('hsc_board'))
        hsc_stream = int(request.form.get('hsc_stream'))
        degree_percentage = float(request.form.get('degree_percentage'))
        degree_field = int(request.form.get('degree_field'))
        internships_count = int(request.form.get('internships_count'))
        projects_count = int(request.form.get('projects_count'))
        certifications_count = int(request.form.get('certifications_count'))
        technical_skills_score = float(request.form.get('technical_skills_score'))
        soft_skills_score = float(request.form.get('soft_skills_score'))
        aptitude_score = float(request.form.get('aptitude_score'))
        communication_score = float(request.form.get('communication_score'))
        work_experience_months = int(request.form.get('work_experience_months'))
        backlogs = int(request.form.get('backlogs'))
        placed = int(request.form.get('placed'))

        salary_arr = model.predict([[
            gender, age, hsc_percentage, hsc_board, hsc_stream,
            degree_percentage, degree_field, internships_count,
            projects_count, certifications_count,
            technical_skills_score, soft_skills_score,
            aptitude_score, communication_score,
            work_experience_months, backlogs ,placed
        ]])
        result = salary_arr[0]
        return render_template('salary_lpa.html' , salaray_value = result)


if __name__ == '__main__':
    app.run(debug=True)
