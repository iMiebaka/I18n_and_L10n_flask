# I18n and 

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

My little experiment with I18n and L10n on flask

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on 

### Prerequisites

- Python
- Web Browser


```
Give examples
```

### Installing

```
pip install requirements.txt
```


### Configure

```
pybabel extract -F babel.cfg -o messages.pot .
```
```
pybabel init -i messages.pot -d translations -l es
```
```
pybabel compile -d translations
```

