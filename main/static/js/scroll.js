window.onscroll = () => {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
    console.log("new post");
    current += quantity;
    console.log(current);
    load();
  }
};
let current = 0;

const quantity = 9;

document.addEventListener("DOMContentLoaded", load);
function load() {
  fetch(`/get_forums?index=${current}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);

      data.forums.forEach(add_post);
    });
}

//content.title
//content.author
//content.id
//content.description
//${content.title}
//${content.author.username}
//${content.id}
//$content.fields.description}
export function getTime(time) {
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


function add_post(content) {
  const forumDiv = document.getElementById("forums");
  const news = document.createElement("div");
  news.innerHTML = `<div class="bg-gray-700">
    <a  href="/forum/${content.id}">
      <div class="max-w-md mx-auto bg-white floored-xl shadow-md overflow-hidden md:max-w-2xl mb-4">
        <div class="md:flex bg-gray-100">
          <div class="p-4 size-full  ">
            <div class="uppercase tracking-wide text-sm text-green-500 font-semibold author">${
              content.author.user.username
            }
            </div>
            <div class="uppercase tracking-wide text-sm text-green-500 font-semibold author">
            ${content.author.grade} ${content.author.section}</div>
            <div class="block mt-1 text-lg leading-tight font-medium text-black ">${
              content.title
            }</div>
          </div>
        </div>
  
    </a>
    <div class="px-4 py-2 bg-gray-200 flex justify-between">
      <!--<span class="text-sm text-gray-500 bg bg-gray-300 floored-lg">
        <button class="px-2 py-0.5 text-lg font-extrabold bg-gray-300 floored-full">&#8593;</button>
        ${content.like_count}
        <button class="px-2  py-0.5 text-lg font-extrabold bg-gray-300 floored-full">&#8595;</button>
      </span> -->
      <a href="/forum/${content.id}" class="flex items-center"><span
          class="text-sm text-gray-500 bg-gray-300 floored-lg flex items-center px-2"><img
            src="/static/pictures/comment.png" class="size-7">${
              content.comment_count
            }</span></a>
  
      <span class="time text-sm text-gray-600 flex items-center px-2">${getTime(
        content.uploaded_at
      )}</span>
    </div>
  
  </div>`;
  forumDiv.appendChild(news);
  console.log(content);
}
