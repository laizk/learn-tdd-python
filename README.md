# learn-tdd-python
Inspired from 'TDD Full Course (Learn Test Driven Development with Python)': https://www.youtube.com/watch?v=eAPmXQ0dC7Q

## Summary

1. Test in isolation
2. TDD forces you to think design
3. Ensures your codes are covered by tests
4. Builds lowest-level documentation

3 rules of TDD

1. Write a failing test first
2. Write just enough test to fail
3. Write just enough code to pass

## Install

Activate virtual environment
```sh
virtualenv env -p python3
source env/bin/activate
```

Install packages
```sh
pip install -r requirements.txt 
```

Download the small language model for NLP
```sh
python -m spacy download en_core_web_sm
```

Create directories
```sh
mkdir static templates test
```

All install current directory as a package
```sh
vim setup.py
```

```sh
pip install -e .
```