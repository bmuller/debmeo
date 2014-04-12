PYDOCTOR=pydoctor

docs:
	$(PYDOCTOR) --make-html --html-output apidoc --add-package debmeo --project-name=debmeo --project-url=http://github.com/bmuller/debmeo --html-use-sorttable --html-use-splitlinks --html-shorten-lists 

lint:
	pep8 --ignore=E303,E251,E201,E202 ./debmeo --max-line-length=140
	find ./debmeo -name '*.py' | xargs pyflakes

install:
	python setup.py install
