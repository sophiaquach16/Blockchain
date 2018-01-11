from sanic import Sanic, response

app = Sanic()

@app.route('/')
def test(request):
    return response.json({'rolo': 1})

app.run('0.0.0.0', port=8080)