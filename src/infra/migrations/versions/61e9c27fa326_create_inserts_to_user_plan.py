"""create inserts to user plan

Revision ID: 61e9c27fa326
Revises: eaa83c87cb41
Create Date: 2022-07-17 13:31:08.249120

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "61e9c27fa326"
down_revision = "eaa83c87cb41"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        "INSERT INTO users.plan(id, type, price, active)\
            VALUES\
        ('1', 'Freemium', '0.0', '1');"
    )
    op.execute(
        "INSERT INTO users.plan(id, type, price, active)\
            VALUES\
        ('2', 'Premium', '5.9', '1');"
    )


def downgrade() -> None:
    op.execute(
        "DELETE FROM users.plan\
        WHERE id = 1"
    )
    op.execute(
        "DELETE FROM users.plan\
        WHERE id = 2"
    )
