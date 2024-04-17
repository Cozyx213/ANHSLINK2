
var forms = document.querySelectorAll(".form").forEach(function(form){
    var submitButton = form.querySelector('[type="submit"]')
    form.addEventListener("submit",()=>{
        submitButton.disabled=true;
        submitButton.innerHTML ="Commenting..";
    }
    )
    console.log(form)
})

