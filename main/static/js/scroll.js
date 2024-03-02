window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        console.log("new post");
        current += quantity;
        console.log(current)
        load();
    }
}
let current = 0

const quantity = 9;

document.addEventListener('DOMContentLoaded', load);
function load() {
    fetch(`/get_forums?index=${current}`)
        .then(response => response.json())
        .then(data => {

            const forumList = JSON.parse(data.forums);
            forumList.forEach(add_post)
        })

}

//content.fields.title
//content.fields.author
//content.fields.id
//content.fields.description
//${content.fields.title}
//${content.fields.author.username}
//${content.fields.id}
//$content.fields.description}
function add_post(content) {
    const forumDiv = document.getElementById("forums");
    const news = document.createElement("div");
    news.innerHTML = `<div class="bg-gray-700">
    <a href="{% url 'forum_comment'  ${content.fields.id} %}">
      <div class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl mb-4">
        <div class="md:flex bg-gray-100">
          <div class="p-4 size-full  ">
            <div class="uppercase tracking-wide text-sm text-green-500 font-semibold author">${content.fields.author.username}
            </div>
            <div class="block mt-1 text-lg leading-tight font-medium text-black ">${content.fields.title}</div>
          </div>
        </div>
  
    </a>
    <div class="px-4 py-2 bg-gray-200 flex justify-between">
      <span class="text-sm text-gray-500 bg bg-gray-300 rounded-lg">
        <button class="px-2 py-0.5 text-lg font-extrabold bg-gray-300 rounded-full">&#8593;</button>
        {{forum.likes}}
        <button class="px-2  py-0.5 text-lg font-extrabold bg-gray-300 rounded-full">&#8595;</button>
      </span>
      <a href="{% url 'forum_comment'  forum.id %}" class="flex items-center"><span
          class="text-sm text-gray-500 bg-gray-300 rounded-lg flex items-center px-2"><img
            src="{% static 'pictures/comment.png' %}" class="size-7">{{forum.comment_count}}</span></a>
  
      <span class="time text-sm text-gray-600 flex items-center px-2">{{forum.uploaded_at}}</span>
    </div>
  
  </div>`;
    forumDiv.appendChild(news)
    console.log("here")
}