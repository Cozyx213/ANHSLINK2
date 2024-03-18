document.addEventListener("DOMContentLoaded", load);

function load() {
  const logsDiv = document.getElementById("logs");
  logsDiv.innerHTML = "";
  fetch("logs")
    .then((response) => response.json())
    .then((data) => {
      data.posts.forEach(display);
    });
}

async function deleteLog(element, id) {
  const csrftoken = document
    .querySelector('meta[name="csrf-token"]')
    .getAttribute("content");

  try {
    const response = await fetch(`deletePost/${id}`, {
      method: "DELETE",
      headers: {
        "X-CSRFToken": csrftoken,
      },
    });
    if (response.ok) {
      console.log(`Deleted: ${id}`);
      element.parentNode.remove();
      console.log(element);
    } else {
      console.error("Error deleting post");
    }
  } catch (error) {
    console.error("Error", error);
  }
}

function display(content) {
  const logsDiv = document.getElementById("logs");
  const news = document.createElement("div");
  news.innerHTML = `${content.title} <button onclick= deleteLog(this,${content.id})> Delete </button> `;
  logsDiv.appendChild(news);
  console.log(content.title);
}
