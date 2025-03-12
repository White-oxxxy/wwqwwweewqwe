"""delete useless relationship

Revision ID: 1f490de9695d
Revises: f810f369748a
Create Date: 2025-03-08 21:20:55.147527

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1f490de9695d"
down_revision: Union[str, None] = "f810f369748a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("tags_uploader_id_fkey", "tags", type_="foreignkey")
    op.drop_constraint("texts_uploader_id_fkey", "texts", type_="foreignkey")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(
        "texts_uploader_id_fkey", "texts", "users", ["uploader_id"], ["id"]
    )
    op.create_foreign_key(
        "tags_uploader_id_fkey", "tags", "users", ["uploader_id"], ["id"]
    )
    # ### end Alembic commands ###
