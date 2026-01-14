"""add projects and project members

Revision ID: 98d2700715f7
Revises: 3c6d73efcd1f
Create Date: 2026-01-13 20:52:32.245434

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98d2700715f7'
down_revision: Union[str, Sequence[str], None] = '3c6d73efcd1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

projectrole_enum = sa.Enum(
    'OWNER',
    'MEMBER',
    name='projectrole',
    create_type=False
)

def upgrade() -> None:
    op.create_table(
        'projects',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=False),
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=True
        ),
        sa.ForeignKeyConstraint(
            ['owner_id'],
            ['users.id'],
            ondelete='CASCADE'
        ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(
        op.f('ix_projects_id'),
        'projects',
        ['id'],
        unique=False
    )

    op.create_table(
        'project_members',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('project_id', sa.Integer(), nullable=False),
        sa.Column(
            'role',
            projectrole_enum,
            nullable=False
        ),
        sa.Column(
            'joined_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=True
        ),
        sa.ForeignKeyConstraint(
            ['project_id'],
            ['projects.id'],
            ondelete='CASCADE'
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
            ondelete='CASCADE'
        ),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('project_members')
    op.drop_index(op.f('ix_projects_id'), table_name='projects')
    op.drop_table('projects')

    projectrole_enum = sa.Enum('OWNER', 'MEMBER', name='projectrole')
    projectrole_enum.drop(op.get_bind(), checkfirst=True)
