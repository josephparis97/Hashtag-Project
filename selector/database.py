import psycopg2

connection = None

def connect():
    """ Connect to a postgresql database, returns connection """
    global connection
    if not connection:
        # connect using env variables, at least password and host
        connection = psycopg2.connect(user = "user",
                                password = "user",
                                host = "bdd",
                                port = "5432",
                                database = "hashtagbdd")
        init_database()
    return connection

def init_database():
    init_db = """
create table if not exists hashtags(
	hashtag varchar(255) primary key,
	popularity int,
	nb_post_hour int,
	last_update timestamp
);

create table if not exists related_hashtags(
	hashtag varchar(255) references hashtags(hashtag),
	relates_hashtag varchar(255)
);"""
    execute(init_db)

def execute(sql_cmd, args=None, fetch=False):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql_cmd, args)
    res = None
    if fetch:
        res = cursor.fetchall()
    
    cursor.close()
    connection.commit()
    return res

def execute_many(sql_cmd, args):
    """ Execute command for every arguments in the list """
    connection = connect()
    cursor = connection.cursor()

    cursor.executemany(sql_cmd, args)
    
    cursor.close()
    connection.commit()

def add_hashtag(hashtag, popularity, nb_posts_hour):
    """ Add a new hashtag to the db """
    sql_cmd = "insert into hashtags(hashtag,popularity,nb_post_hour,last_update) values(%s,%s,%s,now());"
    execute(sql_cmd, (hashtag, popularity, nb_posts_hour))

def update_hashtag(hashtag, popularity, nb_posts_hour):
    sql_cmd = "update hashtags set (popularity,nb_post_hour,last_update)=(%s,%s,now()) where hashtag=%s;"
    execute(sql_cmd, (popularity, nb_posts_hour, hashtag))

def get_hashtag(hashtag):
    """ Get hashtag, popularity, nb_post_hour, last_update for hashtag """
    sql_cmd = "select hashtag, popularity, nb_post_hour, last_update from hashtags where hashtag=%s;"
    res = execute(sql_cmd, (hashtag,), fetch=True)
    if len(res) == 0:
        return {}
    elif len(res) == 1:
        return dict(zip(("hashtag", "popularity", "nb_post_hour", "last_update"), res[0]))
    else:
        raise ValueError(f"More than one hashtag was fetched for {hashtag}")

def add_update_hashtag(hashtag, popularity, nb_posts_hour):
    """ Add a new hashtag or update it if it already exists """
    
    if get_hashtag(hashtag):
        update_hashtag(hashtag, popularity, nb_posts_hour)
    else:
        add_hashtag(hashtag, popularity, nb_posts_hour)

def add_relations(hashtag, related_hashtags):
    sql_cmd = "insert into related_hashtags(hashtag,relates_hashtag) values(%s,%s);"
    execute_many(sql_cmd, ((hashtag, related_hashtag) for related_hashtag in related_hashtags))

def get_related_hashtags(hashtag):
    sql_cmd = "select relates_hashtag from related_hashtags where hashtag=%s;"
    res = execute(sql_cmd, (hashtag,), fetch=True)
    return [r[0] for r in res]