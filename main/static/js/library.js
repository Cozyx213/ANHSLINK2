document.addEventListener("DOMContentLoaded", (event) => {
  var grade7Options = [
    {
      text: "Subject",
      value: "Subject",
      disabled: "disabled",
      selected: "selected",
    },
    { text: "Enhanced Science", value: "Enhanced Science" },
    { text: "Esp", value: "Esp" },
    { text: "Mapeh", value: "Mapeh" },
    { text: "Creative Technology", value: "Creative Technology" },
    { text: "Filipino", value: "Filipino" },
    { text: "English", value: "English" },
    { text: "Enhanced Math", value: "Enhanced Math" },
    { text: "Science Research", value: "Science Research" },
    { text: "AP", value: "AP" },
  ];

  var grade8Options = [
    {
      text: "Subject",
      value: "Subject",
      disabled: "disabled",
      selected: "selected",
    },
    { text: "Science", value: "Science" },
    { text: "Esp", value: "Esp" },
    { text: "Mapeh", value: "Mapeh" },
    { text: "ICT", value: "ICT" },
    { text: "Filipino", value: "Filipino" },
    { text: "English", value: "English" },
    { text: "Math", value: "Math" },
    { text: "Biotechnology", value: "Biotechnology" },
    { text: "AP", value: "AP" },
  ];
  var grade10Options = [
    {
      text: "Subject",
      value: "Subject",
      disabled: "disabled",
      selected: "selected",
    },
    { text: "Science", value: "Science" },
    { text: "Esp", value: "Esp" },
    { text: "Mapeh", value: "Mapeh" },
    { text: "Research", value: "Research" },
    { text: "Filipino", value: "Filipino" },
    { text: "English", value: "English" },
    { text: "Math", value: "Math" },
    { text: "Advanced Chemistry", value: "Advanced Chemistry" },
  ];
  var grade11Options = [
    {
      text: "Subject",
      value: "Subject",
      disabled: "disabled",
      selected: "selected",
    },
    { text: "Reading and Writing", value: "Reading and Writing" },
    { text: "Pagbasa at Pagsusuri..", value: "Pagbasa at Pagsusuri.." },
    {
      text: "Disaster and Risk Reduction",
      value: "Disaster and Risk Reduction",
    },
    {
      text: "Physical Education and Health 1",
      value: "Physical Education and Health 1",
    },
    { text: "Statistics and Probability", value: "Statistics and Probability" },
    { text: "Practical Research 1", value: "Practical Research 1" },
    {
      text: "Understanding Culture, Society, and Politics",
      value: "Understanding Culture, Society, and Politics",
    },
    { text: "Applied Economics", value: "Applied Economics" },
    { text: "Fundamentals of ABM", value: "Fundamentals of ABM" },
    { text: "Basic Calculus", value: "Basic Calculus" },
    { text: "Gen Biology 2", value: "Gen Biology 2" },
    {
      text: "Disciplines and Ideas in Applied Social Sciences",
      value: "Discipline and Ideas in Applied Social Sciences",
    },
    {
      text: "Creative Writing, Malikhaing Pagsulat",
      value: "Creative Writing, Malikhaing Pagsulat",
    },
  ];

  const form = document.getElementById("upload");
  const file = document.getElementById("file");
  const grade = document.getElementById("grade");
  const subject = document.getElementById("subject");

  grade.addEventListener("change", function (event) {
    var gradeVal = grade.value;

    if (gradeVal === "Grade 7") {
      changesub(grade7Options);
      console.log("7");
    } else if (gradeVal === "Grade 8") {
      changesub(grade8Options);
      console.log("8");
    } else if (gradeVal === "Grade 9") {
      changesub(grade9Options);
      console.log("9");
    } else if (gradeVal === "Grade 10") {
      changesub(grade10Options);
      console.log("10");
    } else if (gradeVal === "Grade 11") {
      changesub(grade11Options);
      console.log("11");
    }
  });
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

  function changesub(gradelvl) {
    subject.innerHTML = "";
    gradelvl.forEach(function (option) {
      var newOption = document.createElement("option");
      newOption.text = option.text;
      newOption.value = option.value;
      subject.add(newOption);
    });
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
