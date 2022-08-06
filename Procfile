release: alembic upgrade head
web: gunicorn -w 2 -b 0.0.0.0:5000 "server:create_app()" --reload