install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calcul:
	uv run brain-calcul

brain-logic:
	uv run brain-logicbr

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games
