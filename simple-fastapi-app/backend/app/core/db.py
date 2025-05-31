from sqlmodel import create_engine, Session, SQLModel
from core.config import settings

# creating engine to connect with database
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG, # log SQL queries in debug mode
    pool_pre_ping=True, # verify connections before use
)

def create_db_and_tbls():
    """Create database tables"""
    SQLModel.metadata.create_all(engine)
    
def get_session():
    """Dependency to get database sesion"""
    with Session(engine) as session:
        yield session