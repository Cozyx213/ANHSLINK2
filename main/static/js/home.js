function update(){

    fetch("{% url 'fetch'%")
        .then(response => response.json())
        .then(data=>{

            data.forEach(post =>{

                const table = document.createElement('tr');
                table.inertHTML = `
                
                <td>${post.description}</td>
                `

            })

        })
}
update();
setInterval(update,5000);