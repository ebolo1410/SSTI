from flask import Flask, request, render_template_string

app = Flask(__name__)

# Bật chế độ debug trong cấu hình của Flask
# app.config['DEBUG'] = True
app.jinja_env.add_extension('jinja2.ext.debug')

@app.route('/')
def hello_world():
    name = request.args.get('name')
    template = '''
    <p>Hello, %s!</p>
    ''' %name

    return render_template_string(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)