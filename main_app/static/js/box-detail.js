const closeBtn = document.querySelector(".close")
const itemForm = document.querySelector('.item-form')

console.log(itemForm);
console.log(closeBtn.innerText)

function hideForm(){
  if (closeBtn.innerText === "Open Box") {
    itemForm.setAttribute("hidden", true)
  }
}

hideForm()
