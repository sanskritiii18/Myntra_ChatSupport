from database import db
from models.products import Product
from app import app

products = [
    {
        "name": "Printed Round Neck T-shirt",
        "description": "Printed Round Neck T-shirt",
        "price": 421,
        "discount": 35,
        "brand": "Moda Rapido",
        "category": "Men T-shirt",
        "stock": 10,
        "image_url": "https://assets.myntassets.com/f_webp,dpr_1.5,q_60,w_210,c_limit,fl_progressive/assets/images/2378362/2018/6/9/270e0a7e-365b-4640-9433-b269c60bf3061528527188563-Moda-Rapido-Men-Maroon-Printed-Round-Neck-T-shirt-3811528527-1.jpg"
    },
    {
        "name": "Ultralyte Men Running T-shirt",
        "description": "Ultralyte Men Running T-shirt",
        "price": 800,
        "discount": 20,
        "brand": "HRX",
        "category": "Men T-shirt",
        "stock": 10,
        "image_url": "https://assets.myntassets.com/f_webp,dpr_1.5,q_60,w_210,c_limit,fl_progressive/assets/images/2314372/2018/6/19/29e8ddfd-6f5f-43fd-8b71-dfa8ac6cef681529385860869-HRX-by-Hrithik-Roshan-Men-Charcoal-Grey-Slim-Advanced-Rapid--1.jpg"
    },
    {
        "name": "Navy Blue Striped Round Neck T-shirt",
        "description": "Navy Blue Striped Round Neck T-shirt",
        "price": 421,
        "discount": 35,
        "brand": "Moda Rapido",
        "category": "Men T-shirt",
        "stock": 10,
        "image_url": "https://assets.myntassets.com/f_webp,dpr_1.5,q_60,w_210,c_limit,fl_progressive/assets/images/2378414/2018/2/8/11518071262125-Moda-Rapido-Men-Navy-Blue-Striped-Round-Neck-T-shirt-3641518071261992-1.jpg"
    },
    {
        "name": "Round Neck T-shirt Regular Fit",
        "description": "Round Neck T-shirt Regular Fit",
        "price": 350,
        "discount": 50,
        "brand": "H&M",
        "category": "Men T-shirt",
        "stock": 10,
        "image_url": "https://assets.myntassets.com/f_webp,dpr_1.5,q_60,w_210,c_limit,fl_progressive/assets/images/productimage/2021/2/25/dcd80c17-5db3-4176-a0f3-62b74ce386df1614246409273-1.jpg"
    },
    {
        "name": "Brush Printed T-shirt",
        "description": "Brush Printed T-shirt",
        "price": 419,
        "discount": 50,
        "brand": "Roadster",
        "category": "Men T-shirt",
        "stock": 10,
        "image_url": "https://assets.myntassets.com/f_webp,dpr_1.5,q_60,w_210,c_limit,fl_progressive/assets/images/2169170/2018/1/31/11517402469341-Roadster-Men-Black-Colourblocked-Round-Neck-T-shirt-6121517402469142-1.jpg"
    },
    {
        "name": "Slim Rapid Dry Raglan T-shirt",
        "description": "Slim Rapid Dry Raglan T-shirt",
        "price": 449,
        "discount": 10,
        "brand": "HRX",
        "category": "Men T-shirt",
        "stock": 10,
        "image_url": "https://assets.myntassets.com/f_webp,dpr_1.5,q_60,w_210,c_limit,fl_progressive/assets/images/2314433/2018/4/11/11523427507742-HRX-by-Hrithik-Roshan-Men-Tshirts-2051523427507608-4.jpg"
    },
    {
        "name": "Striped Polo Collar T-shirt",
        "description": "Striped Polo Collar T-shirt",
        "price": 1399,
        "discount": 30,
        "brand": "Nautica",
        "category": "Men T-shirt",
        "stock": 10,
        "image_url": "https://assets.myntassets.com/f_webp,dpr_1.5,q_60,w_210,c_limit,fl_progressive/assets/images/13573298/2021/5/17/b71cc490-1c1d-464a-846a-0461dc22f9101621250551546-Nautica-Men-Tshirts-2981621250550824-1.jpg"
    },
    {
        "name": "Coloured Round Neck T-shirt",
        "description": "Coloured Round Neck T-shirt",
        "price": 449,
        "discount": 10,
        "brand": "DILLINGER",
        "category": "Men T-shirt",
        "stock": 10,
        "image_url": "https://assets.myntassets.com/f_webp,dpr_1.5,q_60,w_210,c_limit,fl_progressive/assets/images/11067722/2019/12/10/1290831c-0862-4b6a-8eee-41a6cad1b1e01575972511857-DILLINGER-Men-Tshirts-3141575972509288-1.jpg"
    },
    {
        "name": "Striped Round Neck T-shirt",
        "description": "Striped Round Neck T-shirt",
        "price": 449,
        "discount": 10,
        "brand": "Roadster",
        "category": "Men T-shirt",
        "stock": 10,
        "image_url": "https://assets.myntassets.com/f_webp,dpr_1.5,q_60,w_210,c_limit,fl_progressive/assets/images/8807157/2019/2/28/c421d8d6-fcf6-44b0-bf34-d3d7690505051551343695119-Roadster-Men-Black-Colourblocked-Round-Neck-T-shirt-91915513-1.jpg"
    },
    {
        "name": "RAPID-DRY Round Neck T-shirt",
        "description": "RAPID-DRY Round Neck T-shirt",
        "price": 449,
        "discount": 10,
        "brand": "HRX",
        "category": "Men T-shirt",
        "stock": 10,
        "image_url": "https://assets.myntassets.com/f_webp,dpr_1.5,q_60,w_210,c_limit,fl_progressive/assets/images/2314400/2018/6/19/82353ec3-9ebf-421e-bb0f-c897166555641529389688071-HRX-by-Hrithik-Roshan-Men-Navy-Advanced-Rapid-Dry-Round-Neck-1.jpg"
    }
]


with app.app_context():
    for item in products:
        existing_product = Product.query.filter_by(
            name=item["name"]
        ).first()

        if existing_product:
            print("Product already exists:", item["name"])
            continue

        product = Product(
            name=item["name"],
            description=item["description"],
            price=item["price"],
            discount=item["discount"],
            brand=item["brand"],
            category=item["category"],
            stock=item["stock"],
            image_url=item["image_url"]
        )

        db.session.add(product)

    db.session.commit()
    print("Products added successfully")