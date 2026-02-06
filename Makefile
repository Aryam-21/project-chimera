PROJECT_NAME=project-chimera
IMAGE_NAME=chimera-dev

.PHONY: setup test spec-check clean

## Build the Docker image
setup:
	docker build -t $(IMAGE_NAME) .

## Run failing tests inside Docker
test:
	docker run --rm $(IMAGE_NAME)

## Verify implementation aligns with specs (optional but recommended)
spec-check:
	python scripts/spec_check.py

## Cleanup
clean:
	docker rmi $(IMAGE_NAME) || true
