from fastapi import FastAPI
from routes import user, courses, sections


app = FastAPI(
    title='my fastapi app'
)

app.include_router(user.router)
app.include_router(courses.router)
app.include_router(sections.router)
