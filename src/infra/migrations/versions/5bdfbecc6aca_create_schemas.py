"""create schemas

Revision ID: 5bdfbecc6aca
Revises:
Create Date: 2022-07-09 16:39:25.165395

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "5bdfbecc6aca"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS user;")
    op.execute("CREATE SCHEMA IF NOT EXISTS expense;")


def downgrade() -> None:
    op.execute("DROP SCHEMA IF NOT EXISTS user;")
    op.execute("DROP SCHEMA IF NOT EXISTS expense;")
