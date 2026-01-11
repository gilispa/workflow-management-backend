"""add role to users

Revision ID: 3c6d73efcd1f
Revises: da94e9384428
Create Date: 2026-01-11 01:22:08.419434
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '3c6d73efcd1f'
down_revision: Union[str, Sequence[str], None] = 'da94e9384428'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    userrole_enum = sa.Enum('ADMIN', 'MEMBER', name='userrole')
    userrole_enum.create(op.get_bind(), checkfirst=True)

    op.add_column(
        'users',
        sa.Column(
            'role',
            userrole_enum,
            nullable=False,
            server_default='MEMBER'
        )
    )


def downgrade() -> None:
    op.drop_column('users', 'role')

    userrole_enum = sa.Enum('ADMIN', 'MEMBER', name='userrole')
    userrole_enum.drop(op.get_bind(), checkfirst=True)
