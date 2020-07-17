
import requests
import json
url = "http://localhost:8080/v1/books"
book = {
    "name": "The Art of Computer Programming",
    "authors": [
    "Donald Nuth"       # Typo
    ],
    "date": 1968,
    "isbn": "0-201-03801-3"
}

# Add the Book with a Typo to the author's name
response = requests.post(url, json=book)
book_data = response.json()

print("Response after ADDING the book to the library")
print(json.dumps(book_data, indent=4))


# Let's now update the Book with the correct author's name.
book_data["authors"] = ["Donald Knuth"]
update_book_url = "http://localhost:8080/v1/books/{}".format(book_data['uuid'])
response = requests.put(update_book_url, json=book_data)

print("http status code after updating the book: ", response.status_code)
