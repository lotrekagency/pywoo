
clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

test: clean
	@flake8 pywoo
	@pytest --cov pywoo -s --cov-report term-missing

docs: clean
	@sphinx-build -b html ./docs pywoo_docs
