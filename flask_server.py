from flask import Flask, request, render_template
from bin.dbschema import *

app = Flask(__name__)

@app.route('/')
@app.route("/home/")
def landing():
    entries = TableDef.query.all()
    return render_template('landing.html', entries = entries)

@app.route('/submit', methods=['POST'])
def submit():
    e = TableDef()
    e.name = str(request.form['val'])
    db.session.add(e)
    db.session.commit()
    return 'success!'

if __name__ == "__main__":
    
    # Only Do This Once!
    #db.create_all()
    
    app.run(debug=True)
