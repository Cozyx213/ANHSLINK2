function update() {
    fetch("/fetch")
        .then(response => response.json())
        .then(data => {

            const postsList = JSON.parse(data.posts);
           // const table = document.getElementById('table');
            const update = document.getElementById("update")

            //table.innerHTML = "";
            update.innerHTML = "";
            postsList.forEach(post => {

                //const row = document.createElement('tr');
                //row.innerHTML = `
                //<td>${post.fields.description}</td>
                //<td>asd</td>
                //`;
                //table.appendChild(row); 

                const news = document.createElement("div")
                console.log(post)
                news.innerHTML=`<div class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl m-3">
                <div class="md:flex">
                  <div class="p-3">
                    <div class="flex justify-between"><span class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">${post.fields.author.username}
                      </span>
                      <span class="text-sm text-gray-600">${post.fields.created_at}</span>
                    </div>
              
                    <a href="#" class="block mt-1 text-lg leading-tight font-medium text-black hover:underline">${post.fields.title}</a>
                    <p class="mt-2 text-gray-500 font-extrabold">${post.fields.description}</p>
                  </div>
                </div>
                <div class="px-4 py-2 bg-gray-200 text-right">
              
                </div>
              </div>`
                update.appendChild(news)
                console.log(post.fields.description)
                console.log(news)

            })

        })
        .catch(error => console.error('Error fetching data:', error));

}


update();
setInterval(update, 5000);