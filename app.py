from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('itsmymantra.html')


@app.route('/submit', methods=['POST'])
def submit():
    tone = request.form['tone']
    body_type = request.form['body_type']

    # Define the redirect URLs for each combination
    combinations = {
        ('Warm', 'Oval'): 'templates/Oval_Warm.html',
        ('Warm', 'Pear'): 'templates/Pear_Warm.html',
        ('Warm', 'Hourglass'): 'templates/Hourglass_Warm.html',
        ('Cool', 'Oval'): 'templates/Oval_Cool.html',
        ('Cool', 'Pear'): 'templates/Pear_Cool.html',
        ('Cool', 'Hourglass'): 'templates/Hourglass_Cool.html',
    }

    # Get the appropriate URL based on user selection
    redirect_url = combinations.get((tone, body_type), '/')

    return redirect(redirect_url)


if __name__ == '__main__':
    app.run(debug=True)
