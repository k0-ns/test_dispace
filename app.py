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

otveti = "Ответ 1\nОтвет 2\nОтвет 3\nОтвет 4\nОтвет 5\nОтвет 6\nОтвет 7\nОтвет 8"

PAGE = '''
<body style="margin:0;height:100vh;background:url(/static/background.png) center/contain fixed;">
    <textarea 
        id="dragBox"
        readonly 
        style="
            position: fixed;
            bottom: 20px;
            left: 20px;
            width: 300px;
            height: 75px;
            padding: 10px;
            font-size: 14px;
            resize: none;
            cursor: move;
            z-index: 1000;
            background: white;
            border: 1px solid #ccc;
        "
    >''' + otveti + '''</textarea>

    <script>
        const box = document.getElementById('dragBox');
        let dragging = false;
        let isSmall = false;
        
        box.onmousedown = function(e) {
            dragging = true;
            box.style.cursor = 'grabbing';
        };
        
        document.onmousemove = function(e) {
            if (!dragging) return;
            box.style.left = e.clientX - 150 + 'px';
            box.style.top = e.clientY - 37 + 'px';
            box.style.bottom = 'auto';
        };
        
        document.onmouseup = function() {
            dragging = false;
            box.style.cursor = 'move';
        };
        
        // Двойной клик - меняем размер
        box.ondblclick = function() {
            if (isSmall) {
                // Возвращаем нормальный
                box.style.width = '300px';
                box.style.height = '75px';
                box.style.fontSize = '14px';
                box.style.padding = '10px';
            } else {
                // Делаем очень маленькой
                box.style.width = '50px';
                box.style.height = '20px';
                box.style.fontSize = '2px';
                box.style.padding = '1px';
            }
            isSmall = !isSmall;
        };
    </script>
</body>
'''

@app.route('/')
def instruct():
    return 'номер вопроса в роуте пж (s4/1 или s5/23 в зависимости от семака, цифра после слеша это номер вопроса)'

@app.route('/seti/')
def get_all_seti():
    return PAGE


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