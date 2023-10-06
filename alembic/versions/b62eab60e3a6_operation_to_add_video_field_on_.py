"""Operation to add video field on Movement table

Revision ID: b62eab60e3a6
Revises: 2803f5192908
Create Date: 2023-10-05 11:38:08.434252

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'b62eab60e3a6'
down_revision: Union[str, None] = '2803f5192908'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('movement', sa.Column('video', sa.String))


def downgrade() -> None:
    pass
