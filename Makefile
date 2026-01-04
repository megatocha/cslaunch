.PHONY: help build up down restart logs clean install dev

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

install: ## Install dependencies locally
	pip install -r requirements.txt

dev: ## Run development server locally
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

build: ## Build Docker image
	docker-compose build

up: ## Start Docker containers
	docker-compose up -d

down: ## Stop Docker containers
	docker-compose down

restart: ## Restart Docker containers
	docker-compose restart

logs: ## Show Docker logs
	docker-compose logs -f

clean: ## Remove Docker containers and volumes
	docker-compose down -v
	rm -rf data/* logs/*

shell: ## Open shell in running container
	docker-compose exec cs2-controller /bin/bash

ps: ## Show running containers
	docker-compose ps