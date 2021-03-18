function DeleteElement(html_element) {
  if(html_element){
    html_element.remove();
  }
} 

//Hide or Delete things not in use
DeleteElement(document.querySelector("div.md-footer-nav"))
DeleteElement(document.querySelector("a.md-content__button"))
DeleteElement(document.querySelector("article.md-content__inner h1"))

