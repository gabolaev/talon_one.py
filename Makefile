.PHONY: testenv
testenv:
	docker run \
		--rm -it \
		-v $(PWD):/tmp/talon-client \
		-w /tmp/talon-client/ \
		python:3.7.13-slim-buster \
		/bin/bash -c "pip install -r requirements.txt; pip install -r test-requirements.txt; /bin/bash"

.PHONY: test
test:
	docker run \
		--rm -it \
		-v $(PWD):/tmp/talon-client \
		-w /tmp/talon-client/ \
		python:3.7.13-slim-buster \
		/bin/bash -c "pip install -r requirements.txt; pip install -r test-requirements.txt && chmod +x test.sh && IAPI_KEY=$(IAPI_KEY) MAPI_KEY=$(MAPI_KEY) ./test.sh"