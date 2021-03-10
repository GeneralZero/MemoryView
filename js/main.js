//Hide the Bottom Navagation 
function HideElement(html_element) {
  if (html_element.style.display === "none") {
    html_element.style.display = "block";
  } else {
    html_element.style.display = "none";
  }
} 

function DeleteElement(html_element) {
  if(html_element){
    html_element.remove();
  }
} 

//Reorder the Nav folder first then files
function ReorderNavList(wrapper){
  var html_items = wrapper.children;

  var folder_fragment = document.createDocumentFragment();
  var file_fragment = document.createDocumentFragment();

  for (let index = 0; index < html_items.length; index++) {
    if(html_items[index].classList.contains('md-nav__item--nested')){
      folder_fragment.appendChild(html_items[index].cloneNode(true));
    }
    else{
      file_fragment.appendChild(html_items[index].cloneNode(true));
    }
  }

  wrapper.innerHTML = null;
  wrapper.appendChild(folder_fragment);
  wrapper.appendChild(file_fragment);
  
  var html_items = wrapper.children;

  //Recurse to all other folders
  for (let index = 0; index < html_items.length; index++) {
    if(html_items[index].classList.contains('md-nav__item--nested')){
      var inner_nav =  html_items[index].querySelector("ul.md-nav__list")
      ReorderNavList(inner_nav)
      //folder_fragment.appendChild(html_items[index].cloneNode(true));
    }
  }
  
}

/*
// SVG Blob info
import init, { svgbob } from './svgbob.js';

async function run() {
  const result = svgbob.to_svg("------------->");
  document.write(result);
  console.log(`${result}`);
}

run();
*/

//Hide or Delete things not in use
DeleteElement(document.querySelector("div.md-footer-nav"))
DeleteElement(document.querySelector("a.md-content__button"))
DeleteElement(document.querySelector("article.md-content__inner h1"))

//Reorder the Nav list
//ReorderNavList(document.querySelector("ul.md-nav__list"))

