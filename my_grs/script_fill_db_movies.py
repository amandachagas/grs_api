import my_grs.constants as constants
import pandas as pd
from my_grs.models import Movie

items = pd.read_csv(constants.ITEMS_PATH, low_memory=False)
for index, row in items.iterrows():
	movie = Movie.objects.create(
		movie_id=int(row.movieId), 
		title=row.title, 
		genres=row.genres, 
		year=row.year, 
		imdb_id=row.imdbId, 
		imdb_link=row.imdbLink, 
		poster=row.poster, 
		youtubeId=row.youtubeId, 
		tags=row.tags)
	print(movie)




	# print('id: {}, title: {}'.format(row.movieId, row.title))