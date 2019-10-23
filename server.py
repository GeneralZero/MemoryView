import urllib, os, sys, flask, subprocess

from config import site

rootApp = flask.Flask(__name__)
rootApp.config.from_pyfile('app.cfg')

#Get files check in to git
def git_data():
	ret = []
	git_data = subprocess.check_output(["git", "ls-files"], cwd=site["git_folder"])
	for files in git_data.split(b"\n"):
		for ignore_files in site["git_ignore"]:
			#TODO Glob search
			if files.find(ignore_files.encode()) == -1:
				print(files)
			break


def generate_sitemap(git_files):
	pass


#Home Page with Challenges
@rootApp.route('')
@rootApp.route('/')
def home_page():
	return flask.render_template("index.html", content="", **site)

@rootApp.route('/sitemap.json')
def json_search():
	return flask.json(git_files)

@rootApp.route('/static/<filename>')
def server_static(filename):
	return flask.static_file(filename, root='./public')

@rootApp.route('/public/<filename>')
def server_static2(filename):
	return flask.static_file(filename, root='./public')

@rootApp.route('/<path:markdown_path>')
def show_subpath(markdown_path):
    # show the subpath after /path/
    return 'Subpath {}'.format(markdown_path)

if __name__ == '__main__':
	#Generate git file data
	git_data()
	#site_data = generate_sitemap()

	#rootApp.run(host='0.0.0.0', port=8080, debug=True, reloader=True)