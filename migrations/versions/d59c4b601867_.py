"""empty message

Revision ID: d59c4b601867
Revises: 240387718678
Create Date: 2023-06-26 18:57:28.399439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd59c4b601867'
down_revision = '240387718678'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_constraint('fk_posts_user_id_users', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_posts_user_id_users'), 'users', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_posts_user_id_users'), type_='foreignkey')
        batch_op.create_foreign_key('fk_posts_user_id_users', 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###
