const categoryImage = document.querySelector(".category-image-large");

function changeImage(element) {
  const category = element.id;
  if (category === "flags") {
    categoryImage.setAttribute("id", "flags-bg");
  }
  if (category === "animals") {
    categoryImage.setAttribute("id", "animals-bg");
  }
  if (category === "apps") {
    categoryImage.setAttribute("id", "apps-bg");
  }
  if (category === "fruits") {
    categoryImage.setAttribute("id", "fruits-bg");
  }
  if (category === "emojis") {
    categoryImage.setAttribute("id", "emojis-bg");
  }
  if (category === "traffic") {
    categoryImage.setAttribute("id", "traffic-bg");
  }
  if (category === "flowers") {
    categoryImage.setAttribute("id", "flowers-bg");
  }
  if (category === "food") {
    categoryImage.setAttribute("id", "food-bg");
  }
}

//Preloading the images to improve speed
var images = [];
function preload() {
  for (var i = 0; i < arguments.length; i++) {
    images[i] = new Image();
    images[i].src = preload.arguments[i];
  }
}

//-- usage --//
preload(
  "./Assets/Categories/animals-large.webp",
  "./Assets/Categories/app-large.webp",
  "./Assets/Categories/app-small.webp",
  "./Assets/Categories/emoji-small.webp",
  "./Assets/Categories/emoji-large.webp",
  "./Assets/Categories/app-small.webp",
  "./Assets/Categories/app-large.webp",
  "./Assets/Categories/fruits-small.webp",
  "./Assets/Categories/fruits-large.webp",
  "./Assets/Categories/traffic-sign-small.webp",
  "./Assets/Categories/traffic-sign-large.webp",
  "./Assets/Categories/food-small.webp",
  "./Assets/Categories/food-large.webp",
  "./Assets/Categories/car-logo-large.webp",
  "./Assets/Categories/car-logo-small.webp"
);

function createDivs() {
  const passwordImageContainer = document.querySelector(".selected-passwords");
  for (let i = 0; i < 25; i++) {
    const passwordImage = document.createElement("button");
    passwordImage.id = "p" + i;
    passwordImage.type = "button";
    passwordImage.classList.add("password-container");
    passwordImage.classList.add("password-btn");
    passwordImageContainer.appendChild(passwordImage);

    // console.log(passwordImage.id);
  }
}
createDivs();

// let passwordPattern1, passwordPattern2;

// function doSubmit() {
//   if (passwordPattern1 === passwordPattern2) {
//     document.getElementById("pwdInput").value = passwordPattern1;
//     document.getElementById("myForm").submit();
//   } else {
//     alert("Entered passwords did not match, try again:(");
//     document.location.href = "/";
//   }
// }

// function doSubmit() {
//   document.getElementById("pwdInput").value = passwordPattern;
//   document.getElementById("myForm").submit();
// }
