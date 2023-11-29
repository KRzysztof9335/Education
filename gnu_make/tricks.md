## Use environment variable which is a list

In bash source script:
```
export ENV_VAR="value1:value2"
```

In makefile:
```
values := $(strip $(subst :, ,${ENV_VAR}))
```
