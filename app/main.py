from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auth_routes import session_router
from app.routes.mongo_crud_routes import crud_router
from app.routes.user_routes import user_router
from app.helpers.startup_events import connect_to_mongo_db
from app.utils.constants import STARTUP, CRUD, SESSION, ALL_ORIGIN

app = FastAPI()

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=[ALL_ORIGIN, "http://localhost:8001"],
    allow_credentials=True,
    allow_methods=[ALL_ORIGIN],
    allow_headers=[ALL_ORIGIN],
)


def startup_event():
    connect_to_mongo_db()


# MongoDB connection setup during startup
app.add_event_handler(STARTUP, startup_event)

# Include routers
app.include_router(crud_router, tags=[CRUD])
app.include_router(session_router, tags=[SESSION])
app.include_router(user_router, tags=["user"])