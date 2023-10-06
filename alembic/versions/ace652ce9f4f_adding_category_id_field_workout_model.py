"""Adding category id field workout model

Revision ID: ace652ce9f4f
Revises: b62eab60e3a6
Create Date: 2023-10-05 13:33:22.838420

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ace652ce9f4f'
down_revision: Union[str, None] = 'b62eab60e3a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('workout', sa.Column('category_id', sa.String))
    op.create_foreign_key('category_id', 'category', 'workout',['id'], ['id'])


def downgrade() -> None:
    pass
