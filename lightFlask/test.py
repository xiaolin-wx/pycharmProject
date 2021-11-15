"""
from flask import Flask
app = Flask(__name__)

# 一个装饰器，它告诉应用程序哪个URL应该调用相关的函数。
@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()
"""

"""
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>',methods=["GET"])
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run()
"""

from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
   app.run()