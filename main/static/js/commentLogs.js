import load from "./logs.js";
document.addEventListener("DOMContentLoaded", commentload);
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
export default function commentload() {
  const logsDiv = document.getElementById("commentLogs");
  logsDiv.innerHTML = "";
  fetch("commentLogs")
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
    const response = await fetch(`deleteComment/${id}`, {
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
  console.log(content);
  console.log(content.forum);
  const logsDiv = document.getElementById("commentLogs");
  const news = document.createElement("div");
  news.innerHTML = `
  
  <article class="overflow-hidden rounded-lg shadow transition hover:shadow-lg">
  <div class="bg-white p-4 sm:p-6">

    <div class="flex justify-between"> 
    <button class="delete-btn rounded text-red-500" data-id="${
      content.id
    }"> Delete </button>
    <div></div>

    <div class="flex items-center"><time class=" block text-xs text-gray-500">
    ${getTime(content.uploaded_at)}
    </time></div>
    
    
   </div>
  
    <a  href="/forum/${
      content.forum == null ? content.parent.forum.id : content.forum.id
    }">
      <h3 class="mt-0.5 text-lg text-gray-900">
      ${content.text}
      </h3>
      <p class="mt-2 line-clamp-3 text-sm/relaxed text-gray-500">Replies:
    ${content.reply_count}
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
