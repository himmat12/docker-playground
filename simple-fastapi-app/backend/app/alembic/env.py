from logging.config import fileConfig
from sqlmodel import SQLModel
from alembic import context
from backend.app.core.config import settings

# Import your table models explicitly
from backend.app.models import User, Item  # These are your table=True models

# Import your table models explicitly
try:
    from backend.app.models import User, Item
    print("✓ Models imported successfully")
    print(f"✓ Available tables: {list(SQLModel.metadata.tables.keys())}")
    print(f"✓ Metadata object: {SQLModel.metadata}")
except ImportError as e:
    print(f"✗ Import error: {e}")
    
    
# this is the Alembic Config object
config = context.config

# Set database URL
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = SQLModel.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    from sqlalchemy import engine_from_config, pool

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()