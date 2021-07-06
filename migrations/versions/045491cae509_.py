"""empty message

Revision ID: 045491cae509
Revises: 2a554ce926aa
Create Date: 2021-07-04 09:07:59.273971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '045491cae509'
down_revision = '2a554ce926aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('ctime', sa.DateTime(), nullable=True),
    sa.Column('read_num', sa.Integer(), nullable=True),
    sa.Column('save_num', sa.Integer(), nullable=True),
    sa.Column('click_zan', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article')
    # ### end Alembic commands ###