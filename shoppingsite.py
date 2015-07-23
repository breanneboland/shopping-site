"""Ubermelon shopping application Flask server.

Provides web interface for browsing melons, seeing detail about a melon, and
put melons in a shopping cart.

Authors: Joel Burton, Christian Fernandez, Meggie Mahnken.
"""


from flask import Flask, render_template, redirect, flash, session, request
import jinja2

import model


app = Flask(__name__)

# Need to use Flask sessioning features

app.secret_key = '234509cosdwe-0efjwlkjl2k43'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.

app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")


@app.route("/melons")
def list_melons():
    """Return page showing all the melons ubermelon has to offer"""

    melons = model.Melon.get_all()
    return render_template("all_melons.html",
                           melon_list=melons)


@app.route("/melon/<int:id>")
def show_melon(id):
    """Return page showing the details of a given melon.

    Show all info about a melon. Also, provide a button to buy that melon.
    """

    melon = model.Melon.get_by_id(id)
    print melon
    return render_template("melon_details.html",
                           display_melon=melon)


@app.route("/cart")
def shopping_cart():
    """Display content of shopping cart."""

    # TODO: Display the contents of the shopping cart.
    #   - The cart is a list in session containing melons added
    shopping_list = session['shopping_cart']
    melon_tuple_list = []
    for melon_id in shopping_list:
        # price = melon_id.price
        # Maybe create a Class method in model.py that returns the 'self' melon given and id, then you can ask that instance for its .price, .common_name, etc.
        print model.Melon.melon.id 

        # this_melon = model.Melon.get_by_id(item)
        # common_name = this_melon[1]
        # price = this_melon[2]
        # melon_tuple = (common_name, price)
        # melon_tuple_list.append(melon_tuple)

        # From here, use the attributes of each melon object (.price, .common_name) and append them to a list of two-item lists. Then pass that list to Jinja and unpack each two-item list with indices. Presto, cart. No tuples necessary.

    return render_template("cart.html", shopping_list = shopping_list, melon_tuple_list = melon_tuple_list)


@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    """Add a melon to cart and redirect to shopping cart page.

    When a melon is added to the cart, redirect browser to the shopping cart
    page and display a confirmation message: 'Successfully added to cart'.
    """
    
    if 'shopping_cart' in session:
        session['shopping_cart'].append(id)
    else:
        session['shopping_cart'] = [id]

    # TODO: Finish shopping cart functionality
    #   - use session variables to hold cart list

    flash("Melon added to cart!")
    print session

    return redirect("/cart")


@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    # TODO: Need to implement this!

    return "Oops! This needs to be implemented"


@app.route("/checkout")
def checkout():
    """Checkout customer, process payment, and ship melons."""

    # For now, we'll just provide a warning. Completing this is beyond the
    # scope of this exercise.

    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/melons")


if __name__ == "__main__":
    app.run(debug=True)
