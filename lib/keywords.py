from topia.termextract import extract
import pinboard


def print_keywords(text):
    extractor = extract.TermExtractor()
    print sorted(extractor(text))


def get_tags():
    p = pinboard.open("mattfinlayson", "m0foLamb")
    tags = p.tags()
    tags_set = set()
    for tag in tags:
        tags_set.add(tag['name'].decode("utf-8"))
    return tags_set


def print_tags(text, tags):
    text_set = set(text.split(" "))
    matches = tags & text_set
    return list(matches)[0:5]


def get_links(tags):
    p = pinboard.open("mattfinlayson", "m0foLamb")
    output = []
    for tag in tags:
        output.append(p.posts(tag=tag, count=3))
    return output
