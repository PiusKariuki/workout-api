"""workout.category.id

Revision ID: 19abe92e2ec6
Revises: ace652ce9f4f
Create Date: 2023-10-05 13:41:36.033058

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19abe92e2ec6'
down_revision: Union[str, None] = 'ace652ce9f4f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('workout', sa.Column('category_id', sa.String))


def downgrade() -> None:
    pass
