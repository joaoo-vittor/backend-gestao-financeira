"""create table expenses to schema expenses

Revision ID: eaa83c87cb41
Revises: 247678b5e766
Create Date: 2022-07-09 22:40:42.528661

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = "eaa83c87cb41"
down_revision = "247678b5e766"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "expenses",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "user_id",
            sa.Integer,
            sa.ForeignKey("users.users.id", name="users"),
            nullable=False,
        ),
        sa.Column(
            "category_id",
            sa.Integer,
            sa.ForeignKey("expenses.category.id", name="category"),
            nullable=False,
        ),
        sa.Column(
            "payment_method_id",
            sa.Integer,
            sa.ForeignKey("expenses.payment_method.id", name="payment_method"),
            nullable=False,
        ),
        sa.Column("name", sa.String(128), nullable=False),
        sa.Column("value", sa.Float, nullable=False),
        sa.Column("status", sa.String(128), nullable=False),
        sa.Column("time_stamp", sa.DateTime(timezone=True), nullable=False),
        sa.Column("voucher", sa.String(255), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), onupdate=func.now()),
        schema="expenses",
    )


def downgrade() -> None:
    op.drop_table("expenses", schema="expenses")
