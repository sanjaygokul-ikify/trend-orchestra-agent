# Makefile for Orchestra Agent

install:
	pip install -r requirements.txt

test:
	pytest

run:
	python agent.py