from flask import Flask, render_template_string
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/')
def hello():
    html = '''
    <!DOCTYPE html>
    <html>
        <head><title>Click Counter</title></head>
        <body>
            <h1>Counter: <span id="counter">0</span></h1>
            <button onclick="incrementCounter()">Increment</button>
            <script>
                let count = 0;
                function incrementCounter() {
                    count++;
                    document.getElementById('counter').textContent = count;
                }
            </script>
        </body>
    </html>
    '''
    return render_template_string(html)

def open_browser():
    webbrowser.open('http://127.0.0.1:8080')

if __name__ == '__main__':
    from waitress import serve
    Timer(1.5, open_browser).start()
    serve(app, host="0.0.0.0", port=8080)