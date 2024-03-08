
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
      return Math.round(days) + " days ago"
    }
    return Math.round(days) + " day ago"
  } else if (hours >= 1) {
    if (hours >= 2) {
      return Math.round(hours) + " hours ago"
    }
    return Math.round(hours) + " hour ago"
  } else if (mins >= 1) {
    if (mins >= 2) {
      return Math.round(mins) + " minutes ago"
    }
    return Math.round(mins) + " minute ago"
  } else {
    return Math.round(secondsElapsed) + " seconds ago"
  }
}
function post(data) {
  const update = document.getElementById("update")

  update.innerHTML = "";
  
  //console.log(data)
  //console.log(data.posts)

  data.posts.forEach(content => {
    const news = document.createElement("div")
    news.innerHTML = `<div class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl m-3">
  <div class="md:flex">
    <div class="p-3">
      <div class="">
      <span class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">${content.author.username}</span>
      <span class="time text-sm text-gray-600">${getTime(content.created_at)}</span>
      </div>

      <a href="#" class="block mt-1 text-lg leading-tight font-medium text-black hover:underline">${content.title}</a>
      <p class="mt-2 text-gray-500 font-extrabold">${content.description}</p>
    </div>
  </div>
  <div class="px-4 py-2 bg-gray-200 text-right">

  </div>
</div>`
    update.appendChild(news)
  });


 


}
function update() {
  fetch("/fetch")
    
    .then(response => response.json())
    .then(data => {
      //const table = document.getElementById('table');
      //const forums = data.posts
      //forums.forEach(post)
      post(data)

    })
    .catch(error => console.error('Error fetching data:', error));

}


update();
setInterval(update, 5000);