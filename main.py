from fastapi import FastAPI, HTTPException

app = FastAPI()
users = [
    {"id":1, "name":"Alice"},
    {"id":2, "name": "GUINICORN"},
]

@app.get("/users")
def get_users():
    return users

@app.get("/user/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users")
def create_user(user: dict):
    pass
        


