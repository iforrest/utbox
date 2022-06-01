package:
	mkdir -p dist
	COPYFILE_DISABLE=1 tar --exclude='__pycache__' --exclude='*.pyc' --exclude="utbox/local" --exclude="utbox/metadata/local.meta" -cvzf dist/utbox.tar.gz utbox/ 

test:
	python -m unittest discover tests