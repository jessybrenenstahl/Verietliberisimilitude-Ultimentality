.PHONY: check build serve clean

# run the link-integrity validator (the test)
check:
	python3 tools/check_links.py

# generate the static site into ./site (validates first)
build: check
	python3 tools/build_site.py

# build and serve locally
serve: build
	@echo "Serving ./site at http://localhost:8000 (Ctrl-C to stop)"
	cd site && python3 -m http.server 8000

clean:
	rm -rf site
