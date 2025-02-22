"""only username

Revision ID: 91d28c9106a5
Revises: 94408297fb70
Create Date: 2025-02-22 08:48:17.649699

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '91d28c9106a5'
down_revision: Union[str, None] = '94408297fb70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
