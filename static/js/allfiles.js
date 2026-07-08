
if (JSON.parse(localStorage.getItem("products")) == null) {
    localStorage.setItem("products", JSON.stringify(products))
}

function showProducts(d) {
    let products = d;

    products.forEach(function (el) {
        appendProduct(el);
    })
}

function appendProduct(el) {
    let catalogue = document.getElementById('products-right');

    let div = document.createElement("div")

    // console.log(el);

    div.addEventListener("click", function () {
        localStorage.setItem("clickedProduct", JSON.stringify(el))
    })

    div.innerHTML = `<a class="each-product" href="moda.html"
              ><div>
                <img
                  src= ${el.img}
                  alt=""
                />
                <div class="brand">${el.brand_name}</div>
                <div class="name">${el.T_shirt_name}</div>
                <div class="price">
                 Rs. ${Math.ceil(el.oldprice * (100 - el.discount) / 100)} <span class="line-through">Rs. ${el.oldprice}</span>
                  <span class="discount">(${el.discount}% OFF)</span>
                </div>
              </div></a
            >`
    // console.log(div)



    catalogue.append(div)
}

showProducts(JSON.parse(localStorage.getItem("products")))



function sort() {
    let menu = document.getElementById("type");
    menu.addEventListener("change", generateData);

    function generateData(event) {
        if (menu.value == '1') {
            let products = JSON.parse(localStorage.getItem("products"))
            let catalogue = document.getElementById('products-right');
            catalogue.innerHTML = null;

            products = products.sort(function (a, b) {
                return b.price - a.price
            });

            showProducts(products);
        } else if (menu.value == '2') {
            let products = JSON.parse(localStorage.getItem("products"))
            let catalogue = document.getElementById('products-right');
            catalogue.innerHTML = null;

            products = products.sort(function (a, b) {
                return a.price - b.price
            });

            showProducts(products);
        } else if (menu.value == '3') {
            let products = JSON.parse(localStorage.getItem("products"))
            let catalogue = document.getElementById('products-right');
            catalogue.innerHTML = null;

            products = products.sort(function (a, b) {
                return b.discount - a.discount
            });

            showProducts(products);
        }
        else if (menu.value == '4') {
            let products = JSON.parse(localStorage.getItem("products"))
            let catalogue = document.getElementById('products-right');
            catalogue.innerHTML = null;

            showProducts(products);
        }
    }
}
sort();

function filter(x) {
    let products = JSON.parse(localStorage.getItem("products"))

    products = products.filter(function (el) {
        return el.brand_name == x;
    })

    let catalogue = document.getElementById('products-right');
    catalogue.innerHTML = null;
    showProducts(products);
}

function priceFilter(x, y) {
    let products = JSON.parse(localStorage.getItem("products"))

    products = products.filter(function (el) {
        return el.price < x && el.price > y;
    })

    let catalogue = document.getElementById('products-right');
    catalogue.innerHTML = null;
    showProducts(products);
}