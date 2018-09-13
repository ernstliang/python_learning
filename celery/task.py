from celery import Celery

BROKER = 'redis://localhost:6379'
BACKEND = 'redis://localhost:6379'

app = Celery('task', broker=BROKER, backend=BACKEND)

@app.task
def add(x, y):
    return x * y