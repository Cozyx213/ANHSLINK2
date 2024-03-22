document.addEventListener("DOMContentLoaded", load);

function load() {
  var articleData = document
    .getElementById("article-data")
    .getAttribute("data-article");

  var article = JSON.parse(articleData);
  console.log(article.post.author);
}
