from __future__ import unicode_literals
import youtube_dl
from flask import *
import imdb
import os
app = Flask(__name__)
decc1=[]
@app.route('/')
def home():
	return render_template('index.html')

@app .route('/result', methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		a = result.values()
		a = list(a)
		link = str(a[0])
		path = str(a[1])
		you_tube(link,path)
		return render_template('result.html')

def you_tube(link,path):
	ydl_opts = {}
	os.chdir(path)
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([link])

if __name__ == '__main__':
	app.run(debug = True)