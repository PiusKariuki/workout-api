"""foreign user_id key in workout

Revision ID: 52c9f7ee3d52
Revises: 079424387cf9
Create Date: 2023-10-24 20:23:52.064312

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '52c9f7ee3d52'
down_revision: Union[str, None] = '079424387cf9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key("user_id", "workout", "user", ['id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
