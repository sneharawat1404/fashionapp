from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('itsmymantra.html')

@app.route('/submit', methods=['POST'])
def submit():
    tone = request.form['tone']
    body_type = request.form['body_type']

    # Determine which template to render based on input
    if tone == 'Warm' and body_type == 'Pear':
        return render_template('Pear_Warm.html')
    elif tone == 'Warm' and body_type == 'Oval':
        return render_template('Oval_Warm.html')
    elif tone == 'Warm' and body_type == 'Hourglass':
        return render_template('Hourglass_Warm.html')
    elif tone == 'Cool' and body_type == 'Pear':
        return render_template('Pear_Cool.html')
    elif tone == 'Cool' and body_type == 'Oval':
        return render_template('Oval_Cool.html')
    elif tone == 'Cool' and body_type == 'Hourglass':
        return render_template('Hourglass_Cool.html')
    else:
        return render_template('itsmymantra.html')  # Fallback to main page

if __name__ == '__main__':
    app.run(debug=True)
