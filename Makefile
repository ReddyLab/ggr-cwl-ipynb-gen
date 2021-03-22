.PHONY: clean install uninstall

PYTHON_FILES=$(wildcard ggr_cwl_ipynv_gen/*/*.py)

clean:
	-rm -rf ggr_cwl_ipynv_gen.egg-info build dist

dist: $(PYTHON_FILES)
	if [[ -z $$(pip list | grep -e "^build\s") ]]; then pip install build; fi
	python -m build

install: dist
	pip install dist/*.whl

uninstall:
	pip uninstall ggr_cwl_ipynb_gen
