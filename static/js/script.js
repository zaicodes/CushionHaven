const menubtn = document.querySelector(".menu_btn");
const navlinksmain = document.querySelector(".nav_links_main");
const searchbtn = document.querySelector(".search_btn_navbar");
const navbar_Search = document.querySelector(".navbar_Search");
const sm_search_btn = document.querySelector(".sm_search_btn");
const small_link = document.querySelectorAll(".small_link");

///search button on mobile and computer 
searchbtn.addEventListener("click", function (e) {
  e.preventDefault();
  navbar_Search.classList.toggle("navbar_Search_show");
  sm_search_btn.classList.toggle("sm_search_btn_show");
});

//for emailJs on Contact us
(function () {
  emailjs.init("YHTCkok7fd_7kaLK-");
})();
document.querySelector(".contact_submit").addEventListener("click" , function (e){
  e.preventDefault()
 
  var params = {
    fromName: document.getElementById("fullname").value,
    emailId: document.getElementById("email_id").value,
    message: document.getElementById("message").value,
  };


  const value = document.getElementById("email_id").value;
  if (value.indexOf("@") === -1) {
    alert("Please enter a valid email");
    return;
  } else {
    emailjs
      .send("service_qxmr6gc", "template_47nej3m", params)
      .then(function (res) {
        console.log("EmailJS Response:", res);
        document.querySelector(".popupcontact").classList.remove("hidden")
        setTimeout(() => {
    document.querySelector(".popupcontact").classList.add("hidden")
  }, 5000);




      })


    document.getElementById("fullname").value = "";
    document.getElementById("email_id").value = "";
    document.getElementById("message").value = "";
  }
  })


// Menu btn function 
menubtn.addEventListener("click", function () {
  navlinksmain.classList.toggle("navlinks_show");
});

small_link.forEach(function(element) {
  element.addEventListener("click", function () {
    navlinksmain.classList.toggle("navlinks_show");
  });
});

// Toasts messages alert 
document.addEventListener("DOMContentLoaded", function() {
  var customToast = document.getElementById("customToast");
  var closeButton = customToast.querySelector(".close");


  closeButton.addEventListener("click", function() {
    var toast = new bootstrap.Toast(customToast);
    toast.hide();
  });
});

// Funciton for quantity 
function handleEnableDisable(itemId) {
  var allQtyInputs = document.querySelectorAll(".qty_input");
  for (let i = 0; i < allQtyInputs.length; i++) {
    var currentItem = allQtyInputs[i];
    if (currentItem.dataset.item_id === itemId) {
      var currentValue = parseInt(currentItem.value);
      var minusDisabled = currentValue < 2;
      var plusDisabled = currentValue > 98;
document.getElementById(`decrement-qty_${itemId}`).disabled = minusDisabled;
document.getElementById(`increment-qty_${itemId}`).disabled = plusDisabled;
    }
  }
}

var allQtyInputs = document.querySelectorAll(".qty_input");
allQtyInputs.forEach(function(input) {
  input.addEventListener("change", function() {
    var itemId = this.dataset.item_id;
    handleEnableDisable(itemId);
  });
});

// Increasing quantity 
document.querySelectorAll(".increment-qty").forEach(function(button) {
  button.addEventListener("click", function (e) {
    e.preventDefault();
    var closestInput = this.closest(".input-group").querySelector(".qty_input");
    var currentValue = parseInt(closestInput.value);
    closestInput.value = currentValue + 1;
    var itemId = this.dataset.item_id;
    handleEnableDisable(itemId);
  });
});

// Decreasing quantity 
document.querySelectorAll(".decrement-qty").forEach(function(button) {
  button.addEventListener("click", function (e) {
    e.preventDefault();
    var closestInput = this.closest(".input-group").querySelector(".qty_input");
    var currentValue = parseInt(closestInput.value);
    closestInput.value = currentValue - 1;
    var itemId = this.dataset.item_id;
    handleEnableDisable(itemId);
  });
});

//Sort btn 
document.addEventListener("DOMContentLoaded", function () {
document.getElementById("sort-selector").addEventListener("change",
     function () {
    var selector = this;
    var currentUrl = new URL(window.location);
    var selectedVal = selector.value;
    if (selectedVal !== "reset") {
      var sort = selectedVal.split("_")[0];
      var direction = selectedVal.split("_")[1];
      currentUrl.searchParams.set("sort", sort);
      currentUrl.searchParams.set("direction", direction);
    } else {
      currentUrl.searchParams.delete("sort");
      currentUrl.searchParams.delete("direction");
    }

    window.location.href = currentUrl.toString();
  });
});

// Update btn 
document.querySelectorAll(".update-link").forEach(function(link) {
  link.addEventListener("click", function (e) {
    e.preventDefault();
    var form = this.previousElementSibling;
    form.submit();
  });
});