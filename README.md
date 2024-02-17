### About

ray tracing in a weekend BUT in python :snake:

Written while following the [original ray tracing in a weekend document](https://raytracing.github.io/books/RayTracingInOneWeekend.html)

### New and Noteworthy

tests check against ground truth in the original document for a pixel by pixel comparison.

Some results

![red-sphere](tests/files/test_simple_red_sphere.png)


### Installation

#### Get the Python Environment setup

install python 3.12. I usually use conda. In this case, I created an env called `rtow312-env` with python 3.12

```
conda create --name=rtow312-env python=3.12
# ... complete the installation ...
conda activate rtow312-env
```

#### Install Poetry

install poetry using pip

```
pip install poetry
```

#### Install all the packages

```
poetry install
```

### Code Hygiene

#### Linting

```
poetry run black .
```

#### More Linting and Formatting

```
poetry run ruff --fix .
```

#### Type Checking

```
poetry run mypy
```

#### Run tests

```
poetry run pytest
```

### Resources

Ray Tracing In a Weekend document - https://raytracing.github.io/books/RayTracingInOneWeekend.html
