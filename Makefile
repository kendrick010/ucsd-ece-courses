run:
	python3 run.py

install:
	pip3 install -r requirements.txt

build:
	python3 setup.py build bdist_wheel sdist
	twine check dist/*

clean:
	rm -rf build
	rm -rf dist
	rm -rf ucsd_ece_courses.egg-info