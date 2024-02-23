function update() {
    fetch("/fetch")
        .then(response => response.json())
        .then(data => {

            const postsList = JSON.parse(data.posts);
            const table = document.getElementById('table');
            
            table.innerHTML = "";

            postsList.forEach(post => {

                const row = document.createElement('tr');
                row.innerHTML = `
                <td>${post.fields.description}</td>
                <td>asd</td>
                `;
                table.appendChild(row); 

                console.log(post.fields.description)

            })

        })
        .catch(error => console.error('Error fetching data:', error));

}


update();
setInterval(update, 5000);