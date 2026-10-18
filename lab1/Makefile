.PHONY: help venv install run lint format format-check typecheck fullcheck precommit clean

help:
	@echo Доступные команды:
	@echo   make venv          - Создать виртуальное окружение
	@echo   make install       - Установить зависимости
	@echo   make run           - Запуск программы
	@echo   make lint          - Проверка кода линтером (Ruff)
	@echo   make format        - Автоформатирование кода (Ruff)
	@echo   make format-check  - Проверка форматирования (Ruff)
	@echo   make typecheck     - Проверка типов (Pyright)
	@echo   make fullcheck     - Все статические проверки
	@echo   make precommit     - Установка Git hooks
	@echo   make clean         - Очистка временных файлов

venv:
	python -m venv .myvenv

install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

run:
	python lab2_2.py

lint:
	python -m ruff check .

format-check:
	python -m ruff format --check .

format:
	python -m ruff format .

typecheck:
	python -m pyright

fullcheck: lint format-check typecheck

precommit:
	python -m pre_commit install
	python -m pre_commit install --hook-type pre-push

clean:
	rm -rf __pycache__ .ruff_cache .pyright_cache