from posts import create_app as a1
from weather import create_app as a2

app1 = a1()
app2 = a2()

if __name__ == '__main__':
    app1.run(debug=True)
    # app2.run(debug=True)