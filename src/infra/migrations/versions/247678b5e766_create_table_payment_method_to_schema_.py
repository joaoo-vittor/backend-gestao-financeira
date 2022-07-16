"""create table payment_method to schema expense

Revision ID: 247678b5e766
Revises: b8c804a02f72
Create Date: 2022-07-09 22:38:07.788573

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = "247678b5e766"
down_revision = "b8c804a02f72"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "payment_method",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(128), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), onupdate=func.now()),
        schema="expense",
    )


def downgrade() -> None:
    op.drop_table("payment_method", schema="expense")
