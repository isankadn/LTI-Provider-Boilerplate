from flask import Flask, request, render_template, session
from pylti.flask import lti
import os
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.DEBUG)

load_dotenv() 

app = Flask(__name__) 
app.secret_key = os.getenv('CONSUMER_SECRET')  


app.config['PYLTI_CONFIG'] = {
    'consumers': {
        os.getenv('CONSUMER_KEY'): {
            'secret': os.getenv('CONSUMER_SECRET')
        }
    }
}

def lti_error(exception=None):
    return render_template('error.html', exception=exception)

@app.route("/lti_launch", methods=["POST"])
@lti(request='initial', error=lti_error, app=app)
def lti_launch(lti=lti):
    user_id = lti.user_id
    return render_template('lti_launch.html', user_id=user_id)

if __name__ == "__main__":
    app.run(debug=True)  