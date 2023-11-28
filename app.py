from flask import Flask, render_template, request, Response
from camera import *
global freeze

app = Flask(__name__)

headings = ("Name","Album","Artist")
df1 = music_rec()
df1 = df1.head(15)
freeze = False

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/how-to-use')
def how_to_use():
    return render_template('how-to-use.html')

@app.route('/more')
def more():
    return render_template('more.html')

@app.route('/feature', methods=['GET', 'POST'])
def index():
    global freeze
    global df_final
    if request.method == 'POST':
        if request.form.get('button_name') == 'BUTTON_VALUE':
            freeze = not freeze
            pass # do something
        else:
            pass # unknown
    elif request.method == 'GET':
        if freeze:
            df_final = df1
            return render_template('feature.html', headings=headings, data=df_final)
        else:
            return render_template('feature.html', headings=headings, data=df1)
            
    # print(df1.to_json(orient='records'))
    return render_template('feature.html', headings=headings, data=df1)

def gen(camera):
    while True:
        global df1
        frame, df1 = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/t')
def gen_table():
    return df1.to_json(orient='records')

if __name__ == '__main__':
    app.debug = True
    app.run()
