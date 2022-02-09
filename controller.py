from main import app

@app.route('/')
def index():
    return "halelua"

@app.route('/get_fish/<id>')
def fish(id):
    return "<div><p>Fish</p> <p>"+id+"</p> </div>"

@app.route("/fish", methods = ["GET"])
def get_fish():
    return "getting_fish"

@app.route("/fish", methods = ["POST"])
def post_fish():
    return "posting_fish"