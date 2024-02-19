import mongoengine as db
from users import User
from articles import Article
from platforms import Platform

db.connect('morya', host='mongodb+srv://morya:9jj7nsxBsoOT43nL@morya.kxt9fkg.mongodb.net/')