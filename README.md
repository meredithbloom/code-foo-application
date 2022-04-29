# code-foo ign application
## Pt 3. Back End...
Meredith Bloom


### My techs:

**Deployment:** Heroku 

**Database:** Postgresql (the only directly Heroku compatible SQL db)

**Framework:** Django (I've also worked with Laravel/PHP and Express/Node.js for back ends, but found that Django/Python was my favorite of the three)

*requirements.txt file has all package dependencies.* 

**Language:** Python


### Storing the Data

Before jumping into any serious coding, I took a little while to look over the data in the csv file itself. I knew I needed to translate the csv to a sql-friendly format, and to do that, I needed to build a model for the database that the csv file would be pulled into (and aligned with). I wrote a SQL command that created a table with corresponding columns and data types that I determined based on my review of the raw data. The five final columns (genres, created_by, published_by, franchises, and regions) were the most varied, with some items having nothing listed at all, to some having multiple things listed under one category. As such, I made the data type for each of these columns an array of strings; I also knew that matching strings is a fairly easy way to execute a search request to an api, and I wanted clients to be able to filter/search for items based on genre, publisher, etc.. 


```
    CREATE TABLE media (
    id int,
    media_type varchar(10),
    name varchar(255),
    short_name varchar(255),
    long_description text,
    short_description text,
    created_at timestamp,
    updated_at timestamp,
    review_url varchar(255),
    review_score float,
    slug varchar(255),
    genres text[],
    created_by text[],
    published_by text[],
    franchises text[],
    regions text[]
);
```

Before deploying my api and database to Heroku, I ensured that the data was correctly reflected in a database I created on my local drive. Django automatically created a model based on the existing table/db that I had connected to my django project - kind of like a backwards migration. Django's literal translations and educated guesses about the data types for the columns were accurate, so I left the model mostly as-is, except for adjusting some additional parameters (i.e. Blank, null).

```
    class Media(models.Model):
        id = models.IntegerField(blank=True, primary_key=True)
        media_type = models.CharField(max_length=10, null=True)
        name = models.CharField(max_length=255, blank=True, null=True)
        short_name = models.CharField(max_length=255, blank=True, null=True)
        long_description = models.TextField(blank=True, null=True)
        short_description = models.TextField(blank=True, null=True)
        created_at = models.DateTimeField(blank=True, null=True)
        updated_at = models.DateTimeField(blank=True, null=True)
        review_url = models.CharField(max_length=255, blank=True, null=True)
        review_score = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
        slug = models.CharField(max_length=255, blank=True, null=True)
        genres = models.TextField(blank=True, null=True)  
        created_by = models.TextField(blank=True, null=True)  
        published_by = models.TextField(blank=True, null=True) 
        franchises = models.TextField(blank=True, null=True)  
        regions = models.TextField(blank=True, null=True) 

    class Meta:
        managed = True
        db_table = 'media'
        
    def __str__(self):
        return self.name
```

TLDR:
csv file -> sql create table -> populated table by copying csv file -> later, django auto-builds model based on existing table. 

### The API Service

I wanted to take advantage of Django's views feature, as I've always used React as a separate front end for my Django-backed projects. As such, I created an API with routes that return pure JSON data, as well as some *very* simple views for in-browser user navigation. Users can easily navigate between an index view and individual entries, with additional filters by media type (show, game, movie, comic). I also included a search bar. 

**Installing dependencies**

1. CD to directory with requirements.txt file
2. activate virtualenv (local python environment)
3. and run: `pip install -r requirements.txt`


Live Link: [Code Foo IGN Application](https://code-foo-ign.herokuapp.com/)

#### API Endpoints

Base URL: <https://code-foo-ign.herokuapp.com/>
GET requests only.

**GET All Items (default ordered by id/A-Z)**
Request path: 
`https://code-foo-ign.herokuapp.com/api`

*Additional filters* 

| Query Param | Options |
| ----------- | ------- |
| media_type | show, movie, comic, game |
| genre | *single string* i.e. drama, horror, comedy |
| min_rating | 0-10 |
| max_rating | 0-10 |
| created_by | *single string* i.e. netflix |
| publisher | *single string* i.e. netflix |

You can include multiple filters simultaneously, though only one value for genre/created_by/publisher. Strings are case insensitive (both Drama and drama will work).

**GET specific item (by id)**
Request path:
`https://code-foo-ign.herokuapp.com/api/<id>/`

admin site - 
superuser
Pass4321