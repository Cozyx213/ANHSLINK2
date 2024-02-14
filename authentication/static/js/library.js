
document.addEventListener('DOMContentLoaded', event => {
    var grade9Options = [
        { text: "Subject", value: "Subject", disabled: "disabled", selected: "selected" },
        { text: "Science", value: "Science" },
        { text: "Esp", value: "Esp" },
        { text: "Mapeh", value: "Mapeh" },
        { text: "Research", value: "Research" },
        { text: "Filipino", value: "Filipino" },
        { text: "English", value: "English" },
        { text: "Math", value: "Math" },
        { text: "Consumer Chemistry", value: "Consumer Chemistry" },
    ]
    var grade10Options = [
        { text: "Subject", value: "Subject", disabled: "disabled", selected: "selected" },
        { text: "Science", value: "Science" },
        { text: "Esp", value: "Esp" },
        { text: "Mapeh", value: "Mapeh" },
        { text: "Research", value: "Research" },
        { text: "Filipino", value: "Filipino" },
        { text: "English", value: "English" },
        { text: "Math", value: "Math" },
        { text: "Advance Chemistry", value: "Advance Chemistry" },
    ]
    const form = document.getElementById('upload');
    const file = document.getElementById('file');
    const grade = document.getElementById('grade');
    const subject = document.getElementById("subject");




    grade.addEventListener("change", function (event) {
        var gradeVal = grade.value;
        if (gradeVal === "grade9") {
            changesub(grade9Options)
            console.log("9");


        } else if (gradeVal === "grade10") {
            changesub(grade10Options)
            console.log("10");

        } else if (gradeVal === "grade11") {
            console.log("11");

        }


    });
    file.addEventListener("change", function (event) {
        var file = event.target.files[0];

        if (file) {
            console.log(file.size / (1024 * 1024));
            var sizeMB = file.size / (1024 * 1024);
            if (sizeMB > 16) {
                alert("Upload only limited to 16MB. Sorry for the inconvience.")
                document.getElementById('file').value = ''
            }

        }
    });


    form.addEventListener("onsubmit", validateForm);

    function validateForm() {
        let grade = document.forms["myForm"]["grade"].value;
        if (grade === '') {
            console.log(grade)
            alert("way sulod");

        }else{
            console.log(grade)
        }
    }


    function changesub(gradelvl) {
        subject.innerHTML = ''
        gradelvl.forEach(function (option) {
            var newOption = document.createElement("option");
            newOption.text = option.text;
            newOption.value = option.value;
            subject.add(newOption);
        });
    }







    document.querySelectorAll('.grade-button').forEach(button => {
        button.addEventListener('click', event => {
            const gradeId = button.getAttribute('data-grade');
            const subjectsDiv = document.getElementById(gradeId);
            if (subjectsDiv.style.display === 'block') {
                subjectsDiv.style.display = 'none';
            } else {
                subjectsDiv.style.display = 'block';
                subjectsDiv.style.animationPlayState = 'running';
                subjectsDiv.addEventListener('animationend', () => {
                    subjectsDiv.style.display = 'block';
                });
            }

            console.log(subjectsDiv);
        });
    });
});


