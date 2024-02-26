document.addEventListener("DOMContentLoaded",()=>{
    const submitButton = document.getElementById("submit")
    const titleButton = document.getElementById("title")
    const form = document.getElementById("formFurom")
    submitButton.addEventListener('click', (e)=>{
        
        
        
        form.submit();
        titleButton.disabled=true;

    })

})