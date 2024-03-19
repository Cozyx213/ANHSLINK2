document.addEventListener("DOMContentLoaded", load);
import { getTime } from "./scroll.js";
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

      const articleElement = element.closest("article");
      if (articleElement) {
        articleElement.remove();
      }

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
  news.innerHTML = `
  
  <article class="overflow-hidden rounded-lg shadow transition hover:shadow-lg">
  <div class="bg-white p-4 sm:p-6">

    <div class="flex justify-between"> 
    <button class="delete-btn rounded hover:bg-red-400" data-id="${
      content.id
    }"> Delete </button>
    <div></div>
    <time class=" block text-xs text-gray-500">
    ${getTime(content.uploaded_at)}
    </time>
    
   </div>
  
    <a  href="/forum/${content.id}">
      <h3 class="mt-0.5 text-lg text-gray-900">
      ${content.title}
      </h3>
      <p class="mt-2 line-clamp-3 text-sm/relaxed text-gray-500">Comments:
    ${content.comment_count}
    </p>
    </a>

    
  </div>
</article>
  
    `;
  logsDiv.appendChild(news);
  const deletebtn = news.querySelector(".delete-btn");
  deletebtn.addEventListener("click", () => {
    deleteLog(deletebtn, deletebtn.getAttribute("data-id"));
  });

  console.log(content.title);
}
