"""create table plans_contract to schema user

Revision ID: b948fc87c266
Revises: 865710ccb03f
Create Date: 2022-07-09 22:22:22.663573

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = "b948fc87c266"
down_revision = "865710ccb03f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "plans_contract",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "user_id",
            sa.Integer,
            sa.ForeignKey(
                "users.users.id",
                name="users",
            ),
            nullable=False,
        ),
        sa.Column(
            "plan_id",
            sa.Integer,
            sa.ForeignKey("users.plan.id", name="users"),
            nullable=False,
        ),
        sa.Column("value_plan", sa.Float, nullable=False),
        sa.column("start_time_stamp", sa.DateTime(timezone=True)),
        sa.Column("end_time_stamp", sa.DateTime(timezone=True)),
        sa.Column("active", sa.Boolean, default=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), onupdate=func.now()),
        schema="users",
    )


def downgrade() -> None:
    op.drop_table("plans_contract", schema="users")
