#!/usr/bin/env python3
import frontend
from fastapi import FastAPI
from contextlib import asynccontextmanager
from heavyTask import HeavyTask
from demo import Demo
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_burner()
    yield

app = FastAPI(lifespan=lifespan)

@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/test')
def read_test():
    return {'Hello': 'Test'}

def on_progress(progress, demo: Demo):
    print(f"on_progress, {progress}")
    demo.number = progress

async def simulate_burner():
    for i in range(0,101):
        await asyncio.sleep(0.2)
        heavyTask.mock_progress_changed(i)


async def init_burner() -> None:
    print(f"init_burner")

    await heavyTask.listen(lambda progress: on_progress(progress, Demo.get_instance()))
    asyncio.create_task(simulate_burner())


if __name__ == '__main__':
    print('Please start the app with the "uvicorn" command as shown in the start.sh script')
    demo = Demo.get_instance()


heavyTask = HeavyTask()
frontend.init(app)


