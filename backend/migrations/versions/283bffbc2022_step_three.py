"""step three

Revision ID: 283bffbc2022
Revises: b608ae09cacd
Create Date: 2023-11-01 20:56:30.414964

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '283bffbc2022'
down_revision: Union[str, None] = 'b608ae09cacd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
