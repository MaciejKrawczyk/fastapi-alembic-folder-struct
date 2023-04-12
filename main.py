from fastapi import FastAPI
from routes import users, courses, sections
from config.database import engine
from models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title='my fastapi app'
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
