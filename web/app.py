import web
import os
import uuid

urls = (
    '/', 'Index',
)

render = web.template.render('templates/')

class Index:
    def GET(self):
        return render.index()

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()