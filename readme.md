### How To Use

1. Install this Python package by adding to your **requirements.txt**

```python
azure-functions
git+https://github.com/Hazhzeng/application-ext-timer@master
```

2. Set `PYTHON_ENABLE_WORKER_EXTENSIONS="true"` and `PYTHON_ISOLATE_WORKER_DEPENDENCIES="true"` in your environment variable

3. Run the function app with `func host start`

### Collect Result from Stdout

Example:
```
HttpTriggerExperiment Elapsed: 1.23 seconds
```