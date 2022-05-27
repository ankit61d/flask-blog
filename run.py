from flaskblog import create_app

app = create_app()

# if we run this file in python directly
if __name__ == '__main__':
    app.run(debug=True)    
