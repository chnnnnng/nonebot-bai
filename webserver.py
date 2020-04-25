import os
import web

urls = (
    '/update', 'update'
)

app = web.application(urls, globals())

class update:
    def POST(self):
        try:
            return 'OK'
        finally:
            print("RECEIVE UPDATE")
            os.system("sh update.sh")

if __name__ == "__main__":
    app.run()