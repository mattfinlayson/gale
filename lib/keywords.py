from topia.termextract import extract
import pinboard
import pymongo

mongo = {'host': 'localhost', 'db': 'pinboard', 'collection': 'posts'}
pinboard_creds = {'username': 'mattfinlayson', 'password': 'm0foLamb'}
configuration = {'mongo': mongo, 'pinboard_creds': pinboard_creds, 'update_all': False}


def extract_keywords(text):
    extractor = extract.TermExtractor()
    return sorted(extractor(text))


def get_tags():
    post_collection = get_collection(configuration)
    tags = post_collection.distinct('tags')
    return tags


def generate_tags(text):
    noted_words = extract_keywords(text)
    tags = get_tags()
    matches = []
    for word in noted_words:
        if word[0] in tags:
            matches.append(word[0])
    return matches[0:5]


def get_relevant_links(tags):
    links = {}
    post_collection = get_collection(configuration)
    for tag in tags:
        posts = []
        for post in post_collection.find({'tags': tag}).limit(5):
            posts.append(post)
        links[tag] = posts
    return links


def update_links(post_collection, config):
    p = pinboard.open(config['pinboard_creds']['username'], config['pinboard_creds']['password'])
    remote_posts = {}
    if config['update_all']:
        remote_posts = p.posts()
    else:
        latest_posts = post_collection.find().sort('time', pymongo.DESCENDING).limit(1)
        for latest_post in latest_posts:
            remote_posts = p.posts(fromdt=latest_post['time'])

    for post in remote_posts:
        try:
            del post['time_parsed']
        except KeyError:
            pass
        spec = {'hash': post['hash']}
        post_collection.update(spec, post, True)


def get_collection(config):
    mongo = pymongo.Connection(config['mongo']['host'])
    mongo_db = mongo[config['mongo']['db']]
    return mongo_db[config['mongo']['collection']]


if __name__ == '__main__':
    posts = get_collection(configuration)
    update_links(posts, configuration)
