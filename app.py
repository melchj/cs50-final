from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# TODO: connect to database (or create, if required)

@app.route("/")
# @login_required
def index():
    return render_template("upload.html")
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