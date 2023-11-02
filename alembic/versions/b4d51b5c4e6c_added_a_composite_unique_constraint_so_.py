"""added a composite unique constraint so that each user can have unique workout dates

Revision ID: b4d51b5c4e6c
Revises: 3af2af5d043f
Create Date: 2023-11-02 10:04:19.902869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'b4d51b5c4e6c'
down_revision: Union[str, None] = '3af2af5d043f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('unique_dates_per_user', 'workout', ['user_id', 'date'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_dates_per_user', 'workout', type_='unique')
    # ### end Alembic commands ###
