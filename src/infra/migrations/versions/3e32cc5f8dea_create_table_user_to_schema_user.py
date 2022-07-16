"""create table user to schema user

Revision ID: 3e32cc5f8dea
Revises: 5bdfbecc6aca
Create Date: 2022-07-09 16:42:05.551863

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = "3e32cc5f8dea"
down_revision = "5bdfbecc6aca"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(128), nullable=True),
        sa.Column("email", sa.String(255), nullable=False, unique=True),
        sa.Column("password_hash", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), onupdate=func.now()),
        schema="user",
    )


def downgrade() -> None:
    op.drop_table("user", schema="user")
