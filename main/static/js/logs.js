import commentload from "./commentLogs.js";

document.addEventListener("DOMContentLoaded", load);


function getTime(time) {
  const timeString = time;

  // Parse the timestamp and create a Date object
  const pastDate = new Date(timeString);

  // Get the current time as a Date object
  const currentDate = new Date();

  // Calculate the difference in milliseconds
  const timeElapsed = currentDate - pastDate;

  // Convert milliseconds to seconds
  const secondsElapsed = timeElapsed / 1000;

  var mins = secondsElapsed / 60;
  var hours = mins / 60;
  var days = hours / 24;

  if (days >= 1) {
    if (days >= 2) {
      return Math.floor(days) + " days ago";
    }
    return Math.floor(days) + " day ago";
  } else if (hours >= 1) {
    if (hours >= 2) {
      return Math.floor(hours) + " hours ago";
    }
    return Math.floor(hours) + " hour ago";
  } else if (mins >= 1) {
    if (mins >= 2) {
      return Math.floor(mins) + " minutes ago";
    }
    return Math.floor(mins) + " minute ago";
  } else {
    return Math.floor(secondsElapsed) + " seconds ago";
  }
}

export default function load() {
  const logsDiv = document.getElementById("logs");
  logsDiv.innerHTML = "";
  fetch("forumLogs")
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
    const response = await fetch(`deleteForum/${id}`, {
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
        load();
        commentload();
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

    <div class="flex items-center"><time class=" block text-xs text-gray-500">
    ${getTime(content.uploaded_at)}
    </time>
    </div>
    
    
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
