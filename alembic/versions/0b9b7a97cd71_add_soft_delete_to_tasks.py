"""add soft delete to tasks

Revision ID: 0b9b7a97cd71
Revises: eac5fa972301
Create Date: 2026-01-19 20:38:56.311280

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '0b9b7a97cd71'
down_revision: Union[str, Sequence[str], None] = 'eac5fa972301'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'tasks',
        sa.Column(
            'is_deleted',
            sa.Boolean(),
            server_default=sa.false(),
            nullable=False,
        ),
    )
    op.add_column(
        'tasks',
        sa.Column(
            'deleted_at',
            sa.DateTime(timezone=True),
            nullable=True,
        ),
    )
    op.alter_column(
        'tasks',
        'is_deleted',
        server_default=None,
    )



def downgrade() -> None:
    op.drop_column('tasks', 'deleted_at')
    op.drop_column('tasks', 'is_deleted')
