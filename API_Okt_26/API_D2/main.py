# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return{"message": "Hello World"}



from fastapi import FastAPI,

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Hello World"}

# books = [
#     {"id": 1, "title": "Dune", "author": "Frank Herbert", "year": 1965},
#     {"id": 2, "title": "Neuromancer", "author": "William Gibson", "year": 1984},
#     {"id": 3, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
#     {"id": 4, "title": "Foundation", "author": "Isaac Asimov", "year": 1951},
# ]

#  @app.get("/books")
# def get_books ...