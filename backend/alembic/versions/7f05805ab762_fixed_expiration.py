"""Fixed Expiration

Revision ID: 7f05805ab762
Revises: af069190b60b
Create Date: 2025-03-14 13:43:18.124567

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '7f05805ab762'
down_revision: Union[str, None] = 'af069190b60b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_revoked_tokens_token', table_name='revoked_tokens')
    op.drop_table('revoked_tokens')
    op.drop_table('refresh_tokens')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('refresh_tokens',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('token', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='refresh_tokens_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='refresh_tokens_pkey')
    )
    op.create_table('revoked_tokens',
    sa.Column('token', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('expires_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('token', name='revoked_tokens_pkey')
    )
    op.create_index('ix_revoked_tokens_token', 'revoked_tokens', ['token'], unique=False)
    # ### end Alembic commands ###
