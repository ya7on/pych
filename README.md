# Py2ch

[![codecov](https://codecov.io/gh/BehindLoader/py2ch/branch/master/graph/badge.svg)](https://codecov.io/gh/BehindLoader/py2ch)
[![Build Status](https://travis-ci.com/BehindLoader/py2ch.svg?branch=master)](https://travis-ci.com/BehindLoader/py2ch)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

## Docs

### `class py2ch.catalog.Catalog(board: str)`

Threads catalog class. Accepts the name of the board.

#### `Catalog.board`

__type__: `str`

The board short name.

#### `Catalog.threads`

__type__: [`Threads[]`](#class-py2chthreadthreadkwargs)

Threads list in specified board. (Lazy property, loads only when called.)

### `class py2ch.file.File(**kwargs)`

### `class py2ch.post.Post(**kwargs)`

### `class py2ch.thread.Thread(**kwargs)`
