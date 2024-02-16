document.addEventListener("DOMContentLoaded", event => {

    const leftButton = document.getElementById("left");
    const rightButton = document.getElementById("right");

    leftButton.addEventListener('click',() =>plusDivs(-1));
    rightButton.addEventListener('click',() =>plusDivs(+1));

    var slideIndex = 1;
    showDivs(slideIndex);

    function plusDivs(n) {
        showDivs(slideIndex += n);
    }

    function showDivs(n) {
        var i;
        var x = document.getElementsByClassName("strands");
        if (n > x.length) { slideIndex = 1 };
        if (n < 1) { slideIndex = x.length };
        for (i = 0; i < x.length; i++) {
            x[i].style.display = "none";
            console.log(x[i])
        }
        console.log(slideIndex);
        x[slideIndex - 1].style.display = "block";
    }
});