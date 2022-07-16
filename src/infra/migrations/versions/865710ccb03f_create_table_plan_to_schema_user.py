"""create table plan to schema user

Revision ID: 865710ccb03f
Revises: 3e32cc5f8dea
Create Date: 2022-07-09 22:17:34.011417

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = "865710ccb03f"
down_revision = "3e32cc5f8dea"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "plan",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("type", sa.String(50), nullable=False),
        sa.Column("price", sa.Float, default=0.0),
        sa.Column("active", sa.Boolean, default=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), onupdate=func.now()),
        schema="users",
    )


def downgrade() -> None:
    op.drop_table("plan", schema="users")
