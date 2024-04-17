
document.addEventListener("DOMContentLoaded", (event) => {
  let allSub = [];
  
  async function fetchSubjects() {
    try {
      const response = await fetch("/subjects");
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();

      // Now you can work with 'subs' here within the async function
      return data; // Optionally return it if needed elsewhere
    } catch (error) {
      console.error("Failed to fetch subjects:", error);
    }
  }
  
  fetchSubjects().then((data) => {
    allSub = data;
    console.log(allSub);
    for (let i = 7; i <13; i++) {
      console.log(i)
      
      addSubs(i);
    }
  });
  
  function addSubs(id) {
    const divElement = document.getElementById(`${id}`);
    console.log(allSub.subjects)
    const currentChoices = allSub.subjects?.filter(
      (item) =>  item.grade.level == id

    );
    
    console.log(currentChoices)
    divElement.innerHTML = "";
    currentChoices?.forEach((subject) => {
      const news = document.createElement("div")
      news.innerHTML = `
      <a href="show_resource/${subject.grade.level}/${subject.name}">
      <p>${subject.name}</p>
    </a>
    `;
      divElement.appendChild(news);
    });
  }

  // Call the function to perform the fetch
  const form = document.getElementById("upload");
  const file = document.getElementById("file");
  const grade = document.getElementById("grade");
  const subject = document.getElementById("subject");


 
  grade.addEventListener("change", function (event) {
    var gradeVal = grade.value;

    if (gradeVal) {
      changesub(gradeVal);
      console.log(gradeVal);
    }
  });
  function changesub(gradelvl) {
    const currentSub = allSub.subjects.filter(
      (subject) => subject.grade.id == gradelvl
    );
    subject.innerHTML = " <option selected disabled>Subject</option>";

    currentSub.forEach((sub) => {
      var newOption = document.createElement("option");
      newOption.text = sub.name;
      newOption.value = sub.id;
      
      subject.add(newOption);
    });

    console.log(currentSub);

    ///
    //subject.innerHTML = "";
    //gradelvl.forEach(function (option) {
    //  var newOption = document.createElement("option");
    //  newOption.text = option.text;
    //  newOption.value = option.value;
    //  subject.add(newOption);
    //});
  }

  file.addEventListener("change", function (event) {
    var file = event.target.files[0];

    if (file) {
      console.log(file.size / (1024 * 1024));
      var siz = sizeWithUnit(file.size);
      console.log(siz);
      var sizeMB = file.size / (1024 * 1024);
      if (sizeMB > 16) {
        alert("Upload only limited to 16MB. Sorry for the inconvience.");
        document.getElementById("file").value = "";
      } else {
        document.getElementById("fileSize").innerHTML = `Size = ${siz}`;
      }
    }
  });

  form.addEventListener("onsubmit", validateForm);

  function sizeWithUnit(bytes) {
    if (bytes > 1024 * 1024) {
      var siz = Math.round((bytes / (1024 * 1024)) * 10) / 10;
      var sizeU = `${siz}MB`;
      return sizeU;
    } else if (bytes > 1024) {
      var siz = Math.round((bytes / 1024) * 10) / 10;
      var sizeU = `${siz}KB`;
      return sizeU;
    }
  }
  function validateForm() {
    let grade = document.forms["myForm"]["grade"].value;
    if (grade === "") {
      console.log(grade);
      alert("way sulod");
    } else {
      console.log(grade);
    }
  }

  document.querySelectorAll(".grade-button").forEach((button) => {
    button.addEventListener("click", (event) => {
      const gradeId = button.getAttribute("data-grade");
      const subjectsDiv = document.getElementById(gradeId);
      if (subjectsDiv.style.display === "block") {
        subjectsDiv.style.display = "none";
      } else {
        subjectsDiv.style.display = "block";
        subjectsDiv.style.animationPlayState = "running";
        subjectsDiv.addEventListener("animationend", () => {
          subjectsDiv.style.display = "block";
        });
      }

      console.log(subjectsDiv);
    });
  });
});
