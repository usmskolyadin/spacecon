"""step three

Revision ID: b608ae09cacd
Revises: 1603840793cf
Create Date: 2023-11-01 20:49:19.185341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b608ae09cacd'
down_revision: Union[str, None] = '1603840793cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
