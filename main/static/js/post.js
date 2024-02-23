document.addEventListener("DOMContentLoaded", () => {

    const title = document.getElementById("title");
    const description = document.getElementById("description");
    const countTitle = document.getElementById("countTitle");
    const countDescription = document.getElementById("countDescription");
    const submit = document.getElementById("submit")
    let maxNumTitle = 200;
    let maxNumDescription =400;

    function disableSubmit(){
        submit.style.background='red';
        submit.style.pointerEvents = 'none';
    }
    function enableSubmit(){
        submit.style.background='green';
        submit.style.pointerEvents = '';
        submit.style.display = 'block';
    }

    title.addEventListener("input", () => {
        var charCounts = title.value.length;
        
        if (maxNumTitle - charCounts >= 0 ) {
            countTitle.style.color = 'white';
            enableSubmit();
        
        } else if (maxNumTitle - charCounts < 0) {
            console.log("RED");
            countTitle.style.color = 'red';
            disableSubmit();
        }
        countTitle.innerHTML =`${charCounts} / 200` ;

    });

    description.addEventListener("input", () => {
        var charCounts = description.value.length;

        if( maxNumDescription - charCounts >= 0){
            countDescription.style.color = 'white';
        } else if (maxNumDescription - charCounts <0 ){
            countDescription.style.color = 'red';
        }

        console.log(charCounts)
        countDescription.innerHTML =`${ charCounts} / 400`;

    });
});