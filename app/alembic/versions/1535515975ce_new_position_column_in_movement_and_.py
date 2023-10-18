"""new position column in movement and workout junction table

Revision ID: 1535515975ce
Revises: 19abe92e2ec6
Create Date: 2023-10-08 12:43:02.652682

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1535515975ce'
down_revision: Union[str, None] = '19abe92e2ec6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("movementworkoutjunction", sa.Column('position', sa.Integer))


def downgrade() -> None:
    pass

