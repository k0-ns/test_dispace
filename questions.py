
def load_questions_from_file(filename, delimiter='%'):
    with open(f'static/answers/{filename}', 'r', encoding='utf-8') as file:
        content = file.read()
        questions = content.split(delimiter)
        questions = [q.strip() for q in questions if q.strip()]
        return questions 
    
def questions_to_text(questions):
    return '\n\n'.join(questions)