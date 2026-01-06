from flask import Flask

app = Flask(__name__)

def load_questions_from_file(filename, delimiter='%'):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        questions = content.split(delimiter)
        questions = [q.strip() for q in questions if q.strip()]
        return questions 

questions4 = load_questions_from_file('answers4.txt')
questions5 = load_questions_from_file('answers5.txt')


@app.route('/')
def instruct():
    return 'номер вопроса в роуте пж (s4/1 или s5/23 в зависимости от семака, цифра после слеша это номер вопроса)'

@app.route('/s5/')
def get_all_s5():
    out = "<pre>"
    for i in questions5:
        out += i + '\n\n'
    out += '</pre>'
    for question_id in range(1,40):
        out += f'<img src="/static/1 ({question_id}).png" width=1000>' + '\n'
    return out

@app.route('/s4/')
def get_all_s4():
    out = "<pre>"
    for i in questions4:
        out += i + '\n\n'
    return out + '</pre>'

#5 semak
@app.route('/s5/<int:question_id>/')
def get_answer(question_id):
    if 0 < question_id < 40:
        return (
            f'<pre>\n\n {questions5[question_id - 1]} \n\n</pre>'
            f'<img src="/static/1 ({question_id}).png" width=1000>'
            )
    return 'хуйню попросил', 404

#4 semak
@app.route('/s4/<int:question_id>/')
def get_question(question_id):
    if 1 <= question_id <= len(questions4):
        return '<pre>\n\n' + questions4[question_id - 1] + '\n\n</pre>'
    else:
        return "хуйню попросил", 404

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')