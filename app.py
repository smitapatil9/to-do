from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample in-memory data store
tasks = []

@app.route('/')
def index():
    return render_template('index.html',name="Smita")

'''@app.route('/add', methods=['POST'])
def add_task():
    task_description = request.form['task_description']
    tasks.append({'id': len(tasks) + 1, 'description': task_description})
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if request.method == 'POST':
        task['description'] = request.form['task_description']
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('index'))'''

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
