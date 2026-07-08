function colorFixed() {

  let circles = document.getElementsByClassName("circles");

  for (let i = 0; i < circles.length; i++) {

    circles[i].addEventListener("click", function () {

      for (let j = 0; j < circles.length; j++) {
        circles[j].classList.remove("clicked");
      }

      circles[i].classList.add("clicked");

    });

  }

}

colorFixed();