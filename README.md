

## use

```
# use python 3.5.1
pip install -r packages_requirements.txt
```

## typeshed

```
export MYPYPATH=./out/
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