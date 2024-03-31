const menubtn = document.querySelector(".menu_btn");
const navlinksmain = document.querySelector(".nav_links_main");

///////////////// menu btn funciotnlaity
menubtn.addEventListener("click", function () {
  navlinksmain.classList.toggle("navlinks_show");
});

/////////////////// handling the increment and decremetn buttons

function handleEnableDisable(itemId) {
  var currentValue = parseInt($(`#id_qty_${itemId}`).val());
  var minusDisabled = currentValue < 2;
  var plusDisabled = currentValue > 98;
  $(`#decrement-qty_${itemId}`).prop("disabled", minusDisabled);
  $(`#increment-qty_${itemId}`).prop("disabled", plusDisabled);
}
console.log("sadfsafsafsd");

var allQtyInputs = $(".qty_input");
for (var i = 0; i < allQtyInputs.length; i++) {
  var itemId = $(allQtyInputs[i]).data("item_id");
  handleEnableDisable(itemId);
}

$(".qty_input").change(function () {
  var itemId = $(this).data("item_id");
  handleEnableDisable(itemId);
});

// Increment quantity
$(".increment-qty").click(function (e) {
  e.preventDefault();
  var closestInput = $(this).closest(".input-group").find(".qty_input")[0];
  var currentValue = parseInt($(closestInput).val());
  $(closestInput).val(currentValue + 1);
  var itemId = $(this).data("item_id");
  handleEnableDisable(itemId);
});

// Decrement quantity
$(".decrement-qty").click(function (e) {
  e.preventDefault();
  var closestInput = $(this).closest(".input-group").find(".qty_input")[0];
  var currentValue = parseInt($(closestInput).val());
  $(closestInput).val(currentValue - 1);
  var itemId = $(this).data("item_id");
  handleEnableDisable(itemId);
});

///////////////////// soritng the data

$(document).ready(function () {
  $("#sort-selector").change(function () {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if (selectedVal != "reset") {
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

////////////////////////upate the code code from bag.html

// Update quantity on click
$(".update-link").click(function (e) {
  var form = $(this).prev(".update-form");
  form.submit();
});
