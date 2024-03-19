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
      return Math.round(days) + " days ago";
    }
    return Math.round(days) + " day ago";
  } else if (hours >= 1) {
    if (hours >= 2) {
      return Math.round(hours) + " hours ago";
    }
    return Math.round(hours) + " hour ago";
  } else if (mins >= 1) {
    if (mins >= 2) {
      return Math.round(mins) + " minutes ago";
    }
    return Math.round(mins) + " minute ago";
  } else {
    return Math.round(secondsElapsed) + " seconds ago";
  }
}
function post(data) {
  const update = document.getElementById("update");

  update.innerHTML = "";

  //console.log(data)
  //console.log(data.posts)

  data.posts.forEach((content) => {
    const news = document.createElement("div");
    news.innerHTML = `
    <article class="overflow-hidden rounded-lg shadow transition hover:shadow-lg">
    
  

  <div class="bg-white p-4 sm:p-6">
    <time class="block text-xs text-gray-500"> ${getTime(
      content.created_at
    )} </time>

    <a href="#">
      <h3 class="mt-0.5 text-lg text-gray-900">${content.title}</h3>
    </a>

    <p class="mt-2 line-clamp-3 text-sm/relaxed text-gray-500">
    ${content.description}
    </p>
  </div>
</article>
    
   
</div>`;
    update.appendChild(news);
  });
}
function update() {
  fetch("/fetch")
    .then((response) => response.json())
    .then((data) => {
      //const table = document.getElementById('table');
      //const forums = data.posts
      //forums.forEach(post)
      post(data);
    })
    .catch((error) => console.error("Error fetching data:", error));
}

update();
setInterval(update, 5000);
