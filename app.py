from flask import Flask, request
from page_generator import generate_page
from questions import load_questions_from_file, questions_to_text, load_questions_unformatted
app = Flask(__name__)


questions4_bos = load_questions_from_file('bos/answers4.txt')
questions5_bos = load_questions_from_file('bos/answers5.txt')
# questions_seti = questions_to_text(load_questions_from_file('seti/answers.txt'))
questions_seti = load_questions_unformatted('seti/answers.txt')

current_background=1

@app.route('/')
def instruct():
    return 'роуты: /seti/ , /s4/ , /s5/ '

@app.route('/seti/')
def get_all_seti():
    global current_background
    if request.args.get('next'):
        current_background = (current_background % 20) + 1
    img = f'{current_background}.png'
    return generate_page(questions_seti, f'/static/backgrounds/seti/{img}')


#5 semak bos
@app.route('/s5/')
def get_all_s5():
    out = "<pre>"
    out += questions_to_text(questions5_bos)
    out += '</pre>'
    for question_id in range(1,40):
        out += f'<img src="/static/answers/bos/s5/1 ({question_id}).png" width=1000>' + '\n'
    return out

@app.route('/s5/<int:question_id>/')
def get_answer(question_id):
    if 0 < question_id < 40:
        return (
            f'<pre>\n\n {questions5_bos[question_id - 1]} \n\n</pre>'
            f'<img src="/static/answers/bos/s5/1 ({question_id}).png" width=1000>'
            )
    return 'хуйню попросил', 404

#4 semak bos
@app.route('/s4/')
def get_all_s4():
    out = "<pre>"
    out += questions_to_text(questions4_bos)
    return out + '</pre>'

@app.route('/s4/<int:question_id>/')
def get_question(question_id):
    if 1 <= question_id <= len(questions4_bos):
        return '<pre>\n\n' + questions4_bos[question_id - 1] + '\n\n</pre>'
    else:
        return "хуйню попросил", 404

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')