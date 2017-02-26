
## python setup

```
# install pyenv & pyenv virtual
pyenv install 3.6.0
pyenv virtualenv 3.6.0 deep_learning_sample_3.6.0
pyenv local deep_learning_sample_3.6.0
```

## use

```
# use python 3.6.0
pip install -r packages_requirements.txt
```

## type check

```
export MYPYPATH=./out/
mypy --python-version 3.6 ./chapter2/
```

# for developer

## save

```
pip freeze > packages_requirements.txt
```

## gen stub

```
stubgen matplotlib
stubgen matplotlib.pyplot
```