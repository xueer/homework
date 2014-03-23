#-*- coding:utf8 -*-
from flask import Flask,request,redirect,render_template,g,url_for,flash
from pymongo import Connection
from bson.objectid import ObjectId

app = Flask(__name__)
app.debug = True



@app.before_request
def before_request():
	conn = Connection()
	g.db = conn.test1        #连接数据库test1
	

def get_todos():            #得到一个列表
	
	return g.db.todo.find().sort('_id', -1)

def get_todo(todo_id):        #得到一条记录
	return g.db.todo.find_one({'_id': ObjectId(todo_id)})

def update(todo_id, data):    #修改记录
	return g.db.todo.update({'_id': ObjectId(todo_id)}, {'$set': data})
	

def add_todo():              #添加记录
	
	return g.db.todo.insert({'title': request.form['title']})


@app.route('/', methods=['GET', 'POST'])   #首页,新建记录
def index():
	
    todos = get_todos()
    
    
    if request.method == 'POST':

    	add_todo()

    return render_template('todo.html', todolist=todos)

@app.route('/edit/<todo_id>')         #编辑记录
def edit_todo(todo_id):

	todo = get_todo(todo_id)

	if(todo):
		return render_template('edit_todo_form.html', todo=todo)
	else:
		return redirect(url_for('index'))

@app.route('/update_todo', methods=['POST'])   #编辑提交记录
def update_todo():

	
		data = request.form.to_dict()
		todo_id = request.form['id']
		tt = get_todo(todo_id)
		update(todo_id, data)
		return redirect(url_for('index'))





@app.route('/delete/<todo_id>')     #删除记录
def tododelete(todo_id):

	g.db.todo.remove({'_id': ObjectId(todo_id)})
	return redirect(url_for('index'))


	
if __name__ == '__main__':
	app.run()             #run函数来让应用运行在本地服务器上.


