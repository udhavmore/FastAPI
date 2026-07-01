from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Ola. Migo!!"}


@app.post("/createpost")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"message": f"Post Created: {payload['title']} - {payload['content']}"}