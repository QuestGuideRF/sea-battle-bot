from typing import Sequence ,Union
from alembic import op
import sqlalchemy as sa
revision :str ='c2c59db636bb'
down_revision :Union [str ,Sequence [str ],None ]=None
branch_labels :Union [str ,Sequence [str ],None ]=None
depends_on :Union [str ,Sequence [str ],None ]=None
def upgrade ()->None :
    op .create_table ('players',
    sa .Column ('id',sa .Integer (),nullable =False ),
    sa .Column ('telegram_id',sa .String (),nullable =False ),
    sa .Column ('username',sa .String (),nullable =True ),
    sa .Column ('first_seen',sa .DateTime (),nullable =True ),
    sa .Column ('last_seen',sa .DateTime (),nullable =True ),
    sa .PrimaryKeyConstraint ('id'),
    sa .UniqueConstraint ('telegram_id')
    )
    op .create_table ('matches',
    sa .Column ('id',sa .Integer (),nullable =False ),
    sa .Column ('game_id',sa .String (),nullable =False ),
    sa .Column ('player_1_id',sa .Integer (),nullable =False ),
    sa .Column ('player_2_id',sa .Integer (),nullable =False ),
    sa .Column ('winner_id',sa .Integer (),nullable =True ),
    sa .Column ('started_at',sa .DateTime (),nullable =True ),
    sa .Column ('ended_at',sa .DateTime (),nullable =True ),
    sa .Column ('result',sa .String (),nullable =True ),
    sa .ForeignKeyConstraint (['player_1_id'],['players.id'],),
    sa .ForeignKeyConstraint (['player_2_id'],['players.id'],),
    sa .ForeignKeyConstraint (['winner_id'],['players.id'],),
    sa .PrimaryKeyConstraint ('id'),
    sa .UniqueConstraint ('game_id')
    )
    op .create_table ('player_stats',
    sa .Column ('player_id',sa .Integer (),nullable =False ),
    sa .Column ('games_played',sa .Integer (),nullable =True ),
    sa .Column ('wins',sa .Integer (),nullable =True ),
    sa .Column ('losses',sa .Integer (),nullable =True ),
    sa .Column ('rating',sa .Integer (),nullable =True ),
    sa .ForeignKeyConstraint (['player_id'],['players.id'],),
    sa .PrimaryKeyConstraint ('player_id')
    )
def downgrade ()->None :
    op .drop_table ('player_stats')
    op .drop_table ('matches')
    op .drop_table ('players')