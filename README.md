<div align="center">
  <h1>Template base para backend python</h1>
</div>

----

# 1° Passo

```
git init
```

# 2° Passo

```
python3 -m venv .venv
```

# 3° Passo

```
source .venv/bin/activate
```

# 4° Passo

```
pip install > requirements.txt
```

# 5° Passo

```
pre-commit install
```

# 6° Passo

```
gunicorn -w 5 -b 0.0.0.0:5000 "server:create_app()"
```

# 7° Passo

```
docker-compose up
```

