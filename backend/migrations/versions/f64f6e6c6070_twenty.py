"""twenty

Revision ID: f64f6e6c6070
Revises: 8bd50adf4fa2
Create Date: 2023-11-02 14:19:58.272251

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f64f6e6c6070'
down_revision: Union[str, None] = '8bd50adf4fa2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
