from github import Github

def render_gist(gist_id):
    g = Github()
    gist = g.get_gist(gist_id)

    embed_url = "<script src=\"https://gist.github.com/%s/%s.js\"></script>" % (gist.user.login, gist_id)
    output = "<p>%s</p> %s" % (gist.description, embed_url)
    return output
