#-*- coding:utf8 -*-
from flask import Flask,request,redirect,render_template,g,url_for,flash
from pymongo import Connection
from bson.objectid import ObjectId

app = Flask(__name__)
app.debug = True



@app.before_request
def before_request():
	conn = Connection()
	g.db = conn.test1        #
	

def get_todo():
	
	return g.db.todo.find().sort('_id', -1)
	

def add_todo():
	
	return g.db.todo.insert({'title': request.form['title']})


@app.route('/', methods=['GET', 'POST'])
def index():
	
    todos = get_todo()
    
    
    if request.method == 'POST':

    	add_todo()

    return render_template('todo.html', todolist=todos)



@app.route('/delete/<todo_id>')
def tododelete(todo_id):

	g.db.todo.remove({'_id': ObjectId(todo_id)})
	return redirect(url_for('index'))


	
if __name__ == '__main__':
	app.run()             #run函数来让应用运行在本地服务器上.


