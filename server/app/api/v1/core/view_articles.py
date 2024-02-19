# searching for articles with /search endpoint
# def search_articles(query):
#     return Article.query.filter(Article.title.ilike(f'%{query}%')).all()

# Or
# return {article.to_json() for article in Article.objects(name_contains=query).all()}