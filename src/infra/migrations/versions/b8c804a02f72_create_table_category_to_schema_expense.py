"""create table category to schema expense

Revision ID: b8c804a02f72
Revises: b948fc87c266
Create Date: 2022-07-09 22:32:44.152900

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = "b8c804a02f72"
down_revision = "b948fc87c266"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "category",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "user_id",
            sa.Integer,
            sa.ForeignKey("users.users.id", name="users", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("name", sa.String(128), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), onupdate=func.now()),
        schema="expenses",
    )


def downgrade() -> None:
    op.drop_table("category", schema="expenses")
