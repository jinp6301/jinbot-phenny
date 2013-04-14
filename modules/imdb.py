
ia = IMDb()
def imdb(phenny, input):

   movie_title = input.group(2)
   s_result = ia.search_movie(movie_title)
   first_result=s_result[0]
   ia.update(first_result)
   rating=first_result['rating']
   short_title=first_result['title']
   year1 = first_result['year']
   runtime1 = first_result['runtime'][0]
   genres1 = ' | '.join(first_result['genre'])
   imdburl1 = ia.get_imdbURL(first_result).replace('http://akas.', 'http://', 1)
   phenny.reply("\x02" + short_title + "\x02" + ' ' + '(' + str(year1) + ')' + ', ' + str(runtime1) + ' min, ' + genres1 + ' -- ' + imdburl1)
 
imdb.commands = ['imdb']
imdb.priority = 'high'