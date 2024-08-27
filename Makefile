.PHONY: all deploy build-pypi publish-pypi clean


# deploy step
deploy: install-deps build-jupyterlite download-kuzu

# install dependencies
install-deps:
	python -m pip install -r requirements.txt
	npm install

# Build JupyterLite site
build-jupyterlite:
	cp README.md content
	jupyter lite build --contents content --output-dir dist
	cp deploy/netlify.toml dist

# Download kuzu-wasm
download-kuzu:
	npm view @kuzu/kuzu-wasm dist.tarball | xargs curl -o dist/package.tgz
	tar -xz -C dist -f dist/package.tgz && rm dist/package.tgz

# Render Quarto REPL example
render-repl:
	quarto render examples/Quarto/repl-example.qmd --output-dir ../../dist

# Render Quarto live example
render-quarto-live:
	quarto render examples/Quarto/quarto-live.qmd --output-dir ../../dist

# Clean build files
clean:
	rm -rf dist build/ *.egg-info

# Build the package for PyPI
pypi: 
	python setup.py bdist_wheel
	twine upload $(ls -t dist/*.whl | head -1)

# Server the dist folder
server:
	python deploy/http_server.py dist 8000