# Tic-Tac-Toe in HTML

## Yes, really.

This is my version of Tic-tac-toe with all the game state encoded in the URL.
If you want to know more about how this works in theory, check out my 
[blog post](https://blog.sigma-star.io/2024/11/tic-tac-toe-in-html/) on the topic.

### But... why?

It's fun.

### Why are there Python files?

Since I'm not writing 443 HTML files by hand I wrote a script to generate them.

## How to run?

You'll need Python 3.12 and Poetry.

```bash
poetry install
poetry run python -m generator
```

The generated HTML files are stored in the output/ directory.
