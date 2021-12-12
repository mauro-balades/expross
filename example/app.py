from expross import Expross

app = Expross()

# Can't do the anonimus function, sry
def index(req, res):
    return "hello!"


def run():
    print("Listening on http://localhost:8080/")


app.get("/", index)
app.listen(8080, run)
