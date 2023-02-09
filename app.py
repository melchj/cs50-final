import os
from flask import Flask, redirect, render_template, flash, request
from werkzeug.utils import secure_filename

# Configure application
app = Flask(__name__)
# the below probably shouldnt be hardcoded in "real life"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(__file__), 'uploads')


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("layout.html")
    # """Show portfolio of stocks"""
    # # get all the shares in portfolio (list of (symbol, sum(shares)) from transactions table)
    # rows = db.execute("SELECT symbol, SUM(shares) FROM transactions WHERE user_id = ? GROUP BY symbol;", session.get("user_id"))
    # # add company name and current price to the list for each stock. and calculate total
    # total = 0
    # stocks = []
    # for row in rows:
    #     if row["SUM(shares)"] > 0:
    #         lookup_resp = lookup(row["symbol"])
    #         row["price"] = lookup_resp["price"]
    #         row["name"] = lookup_resp["name"]
    #         total = total + row["price"] * row["SUM(shares)"]
    #         stocks.append(row)

    # # get cash value
    # cash = db.execute("SELECT cash FROM users WHERE id=?;", session.get("user_id"))[0]["cash"]

    # # pass data to portfolio template
    # return render_template("portfolio.html", stocks=stocks, total=total, cash=cash)

@app.route('/upload', methods=['GET', 'POST'])
def upload_data():
    if request.method == "POST":
        # flask docs: https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/
        # check if post request has the file part
        if 'file' not in request.files:
            flash("no file part!")
            return redirect(request.url)
        file = request.files['file']
        # check for empty file (browser default)
        if file.filename == '':
            flash("no selected file!")
            return redirect(request.url)
        # check that it's a json file (at least in name)
        if '.json' not in file.filename.lower():
            flash("must upload .json file!")
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("file uploaded successfully!")
            # return redirect(url_for(analysis))
            # TODO: redirect somewhere else here after successful upload of file
    return render_template("upload.html")