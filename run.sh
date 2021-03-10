sudo cp custom_codefences.py /lib/python3.9/site-packages/pymdownx/

export PYTHONPATH=`pwd`
mkdocs build

#cp css/main.css site/assets/stylesheets/custom.css
#cp js/main.js   site/assets/javascripts/custom.js
#cp css/highlighting/dracula.css site/assets/stylesheets/dracula.css
#cp js/katex_init.js site/assets/javascripts/katex_init.js
#cp js/svgbob.js site/assets/javascripts/svgbob.js

python3 -m http.server -d ./site
