from extensions import app, db
from flask import  render_template, redirect, flash
from forms import RegisterF, LoginF, AddReview, Discount
from models import Accounts
from flask_login import login_user, logout_user

samsung = [
    { "link": "https://alta.ge/images/thumbnails/270/250/detailed/274/1_n5p7-x3_4run-4e.png.jpg", 
        "price": "4590", 
        "name": "Samsung S911B Galaxy S23",
        "id": "1"
    },
    { "link": "https://alta.ge/images/thumbnails/270/250/detailed/314/148692_1_1r8e-q2.png.jpg", 
        "price": "3649", 
        "name": "Samsung S928B Galaxy S24 Ultra",
        "id": "2"
    },    
    { "link" : "https://alta.ge/images/thumbnails/270/250/detailed/278/1_3fk3-7v_amzj-al.png.jpg", 
        "price": "2478", 
        "name": "Samsung A145F Galaxy A14",
        "id": "3"
    }        
    ]
apple = [
    { "link": "https://alta.ge/images/thumbnails/270/250/detailed/248/129094_1.jpg.jpg", 
        "price": "3949", 
        "name": "Apple iPhone 15 Pro Max",
        "id": "1"
    },
    { "link": "https://alta.ge/images/thumbnails/270/250/detailed/259/WWEN_iPhone14_Q422_Blue_PDP_Image_Position-1a.jpg.jpg", 
        "price": "2249", 
        "name": "Apple iPhone 14",
        "id": "2"
    },    
    { "link" : "https://alta.ge/images/thumbnails/270/250/detailed/223/102507_1.png.jpg", 
        "price": "1379", 
        "name": "Apple iPhone 11",
        "id": "3"
    }        
    ]

lenovo = [
    { "link": "https://alta.ge/images/thumbnails/270/250/detailed/321/1_rz5h-83.png.jpg", 
        "price": "4549", 
        "name": "Lenovo IdeaPad Gaming 3",
        "id": "1"
    },
    { "link": "https://alta.ge/images/thumbnails/270/250/detailed/287/1_fbti-y5_tzsi-w5.png.jpg", 
        "price": "1379", 
        "name": "Lenovo IdeaPad Slim 3",
        "id": "2"
    }    
    ]
asus = [
    { "link": "https://alta.ge/images/thumbnails/270/250/detailed/289/128609_1.jpg.jpg", 
        "price": "7249", 
        "name": "Asus TUF Gaming F15",
        "id": "1"
    },
    { "link": "https://alta.ge/images/thumbnails/270/250/detailed/283/1_qwc7-78.png.jpg", 
        "price": "5379", 
        "name": "Asus VivoBook 16",
        "id": "2"
    }   
    ]  

@app.route("/")
def home():

    return render_template("index.html", samsung = samsung, apple = apple, lenovo = lenovo, asus = asus)


@app.route("/location")
def about():
    return render_template("location.html")


dicte = {
"Anna" : "“I was completely impressed with their professionalism and customer service.”",
"Giorgi" : "“I highly recommend this business.”",
"Vaso" : "“Pricing is fair and transparent - definitely value for money.”",
"Tornike" : "“Efficiency and punctuality are hallmarks of their service.”"
}
@app.route("/reviews")
def review():

    return render_template("review.html", customer_reviews = dicte)

@app.route("/partners")
def sponsors():
    return render_template("partners.html")

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/add_review", methods =["GET", "POST"])
def add_review():
    form = AddReview()
    if form.validate_on_submit():
        dicte["Your review"] = form.reviewc.data
        return redirect("/reviews")
    return render_template("add_review.html", form = form)
    

@app.route("/register", methods =["GET", "POST"])
def register():
    form = RegisterF()
    if form.validate_on_submit() and not Accounts.query.filter(Accounts.nickname == form.nickname.data).first():
        Ruser = { 
            "nickname": form.nickname.data,
            "password": form.password.data
        }
        account_to_add = Accounts(nickname = Ruser["nickname"], password = Ruser["password"])
        db.session.add(account_to_add)
        db.session.commit()

        flash("You successfully registered :) ", category="success")
        print(Ruser)
        print(Accounts.query.all())
        return redirect("/")
        
    if form.errors:
        print(form.errors)
        flash("You didnt register :( ", category="danger")
    return render_template("register.html", form = form)



@app.route("/login",  methods =["GET", "POST"])
def login():
    form = LoginF()
    if form.validate_on_submit():
        exists = Accounts.query.filter(Accounts.nickname == form.nickname.data).first()
        print(exists)
        if exists and exists.verify_password(form.password.data):
            login_user(exists)
            flash("You successfully logged in, now you can use discount codes and submit review :)", category="success")
            return redirect("/")
        else:
            flash("Incorrect password, try again :(", category="danger")
    return render_template("Login.html", form = form)

used_SAMSUNG_discount = False
used_APPLE_discount = False
used_LENOVO_discount = False
used_ASUS_discount = False
@app.route("/discount",   methods =["GET", "POST"])
def discount():
    global used_SAMSUNG_discount
    global used_APPLE_discount
    global used_LENOVO_discount
    global used_ASUS_discount
    form = Discount()
    if form.validate_on_submit():
        if form.discount_code.data == "LV5MAY14" and not used_SAMSUNG_discount:
            used_SAMSUNG_discount = True
            for phone in samsung:
                phone["price"] = int(phone["price"]) * 70//100
            flash("You successfully applied discount-code, Check prices :)", category="success")
            return redirect("/") 
        elif form.discount_code.data == "MNO123ST" and not used_APPLE_discount:
            used_APPLE_discount = True
            for phone in apple:
                phone["price"] = int(phone["price"]) * 50//100
            flash("You successfully applied discount-code, Check prices :)", category="success")
            return redirect("/")
        elif form.discount_code.data == "OLV4SY3R" and not used_LENOVO_discount:
            used_LENOVO_discount = True
            for laptop in lenovo:
                laptop["price"] = int(laptop["price"]) * 85//100
            flash("You successfully applied discount-code, Check prices :)", category="success")
            return redirect("/")
        elif form.discount_code.data == "ZUY4OPLQ" and not used_ASUS_discount:
            used_ASUS_discount = True
            for laptop in asus:
                laptop["price"] = int(laptop["price"]) * 75//100            
            flash("You successfully applied discount-code, Check prices :)", category="success")
            return redirect("/")
        else:
            flash("Discount code is wrong or already used, try again :( ", category="danger")


    return render_template("discount.html", form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")