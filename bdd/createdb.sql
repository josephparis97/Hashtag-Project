
create table hashtags(
	hashtag varchar(255) primary key,
	popularity int,
	nb_post_hour int,
	last_update timestamp
);

create table related_hashtags(
	hashtag varchar(255) references hashtags(hashtag),
	relates_hashtag varchar(255)
);