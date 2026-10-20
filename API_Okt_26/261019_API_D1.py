# import requests

# response = requests.get("https://fakestoreapi.com/products")
# print(response)

# print(response[0])   # The response is like a package...

# status code .... headers ....body

# print(response.status_code)
# print(response.headers["Content-Type"])                       
# print(response.text[:200])

# Headers extract information about the response
# - It doesn't contain the data, it tells us something agout the data.
# - Like from dictionary...

# print(response.text[0]['title'])  # ovo ce dati gresku...

# data = response.json()

# print(type(data))       #<class 'list'>
# print(len(data))        # 20 - products
# print(data[0])          # {'id': 1, 'title': 'Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops', 'price': 109.95, 
#                         # 'description': 'Your perfect pack for everyday use and walks in the forest. 
#                         #  Stash your laptop (up to 15 inches) in the padded sleeve, your everyday', 'category': "men's clothing", 'image': 'https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png', 'rating': {'rate': 3.9, 'count': 120}}

# Idemo sa petljom da navedemo neke podatke - rekorde
# for product in data[:5]:
#     print(f"{product['id']}:{product['title']} - ${product['price']}")

# Zelimo sada na primer da dobijemo produkt 15:

# response = requests.get("https://fakestoreapi.com/products/15")
# product = response.json()

# print(product)  # {'id': 15, 'title': "BIYLACLESEN Women's 3-in-1 Snowboard Jacket Winter Coats", 'price': 56.99, 'description': 
                #'Note:The Jackets is US standard size, Please choose size as your usual wear Material: 100% Polyester; 
                # # Detachable Liner Fabric: Warm Fleece. Detachable Functional Liner: Skin Friendly, Lightweigt and Warm.
                # Stand Collar Liner jacket, keep you warm in cold weather. Zippered Pockets: 2 Zippered Hand Pockets, 
                # 2 Zippered Pockets on Chest (enough to keep cards or keys)and 1 Hidden Pocket Inside.Zippered Hand Pockets and 
                # Hidden Pocket keep your things secure. Humanized Design: Adjustable and Detachable Hood and Adjustable cuff to prevent
                #  the wind and water,for a comfortable fit. 3 in 1 Detachable Design provide more convenience, you can separate
                #  the coat and inner as needed, or wear it together. It is suitable for different season and help you adapt to 
                # different climates', 'category': "women's clothing", 'image': 'https://fakestoreapi.com/img/51Y5NI-I5jL._AC_UX679_t.png',
                #  'rating': {'rate': 2.6, 'count': 235}}


# print(product['title'])   - #  BIYLACLESEN Women's 3-in-1 Snowboard Jacket Winter Coats

# print(product['rating'])      # {'rate': 2.6, 'count': 235}   - This is Dictionary inside a dictionary!
# print(product['rating']['rate'])  # 2.6


# # Lista nesto veci u manjem paketu....
# print(product['title'], product['rating']['rate'])   
#     # BIYLACLESEN Women's 3-in-1 Snowboard Jacket Winter Coats 2.6



#**********************************************
#   QUERY PARAMETERS
#**********************************************

# import requests

#1
# response = requests.get("https://fakestoreapi.com/products?limits=5")
# print(len(response.json()))     # 20  - Aladdin dobio 5!

#2
# response = requests.get("https://fakestoreapi.com/products", params={"limit": 5, "sort": "desc"})
# print(len(response.json()))     #  sad sam dobio 5
# print(response.url)             #  https://fakestoreapi.com/products?limit=5&sort=desc


#3
# response = requests.get("https://fakestoreapi.com/products", params={"limit": 5, "sort": "desc"})
# product = response.json
# print(len(response.json()))     #  sad sam dobio 5
# print(response.url)             #  https://fakestoreapi.com/products?limit=5&sort=desc
# print([product['id'] for product in response.json()])       # [5, 4, 3, 2, 1]

#4
# response = requests.get("https://fakestoreapi.com/products/categories")
# print(response.json())      #  ['electronics', 'jewelery', "men's clothing", "women's clothing"]


# #5 
# response = requests.get("https://fakestoreapi.com/products", headers={'Accept': "application/json"})
# print(response.status_code)     # 200





#*******************************************************************************

#   WHEN THINGS GO WRONG - SLIDES page 11  - # 404

#--------------------------------------------------------------

import requests

# response = requests.get("https://api.github.com/users/octocat")
# print(response.status_code)         # 200
# print(response.json()['name'])      # The Octocat


# response = requests.get("https://api.github.com/users/this-user-does-not-exist-123")
# print(response.status_code)         # 
# print(response.json()['name'])      # 404 ...KeyError: 'name' , ali nije problem ime, vec nesto drugo, jer smo gore videli da je ime OK.

response = requests.get("https://api.github.com/users/this-user-does-not-exist-123")

# if response.status_code == 200:
#     print(response.json(['name']))
# elif response.status_code == 404:
#     print("That user does not exists")
# else:
#     print(f"Something went wrong: {response.status_code}")


#**********************************
# raise_for_status()
#------------------------------

# try:
#     response = requests.get("https://api.github.com/users/this-user-does-not-exist-123")
#     response.raise_for_status()
#     print(response.json()['name'])
# except requests.exceptions.HTTPError as error:
#     print(f"The server said no: {error.response.status_code}")


#-------------------------------------------------
#***********************************************************
# Sada zelimo da cekamo 0.01 sekundu pre nego se nesto desi:


# response = requests.get("https://api.github.com/users/octocat", timeout=0.001)

#    raise ReadTimeout(e, request=request)
#   requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='api.github.com', port=443): Read timed out. (read timeout=0.001)
#---------------------------------------------------------------------------------

# response = requests.get("https://this-domain-does-not-exist-abc123.com")

# response = requests.get("https://fakestoreapi.com/products")  # OK
# response = requests.get("fakestoreapi.com/products")            # requests.exceptions.MissingSchema: 
        #Invalid URL 'fakestoreapi.com/products': No scheme supplied. Perhaps you meant https://fakestoreapi.com/products?

# response = requests.get("https://example.com")
# print(response.status_code)
# response.json()
#---------------------------


def get_json(url, params=None, headers=None, timeout=5):
    try:
        response = requests.get(url, pram=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        return requests.exceptions.Timeout:     #Vazno je jer nije predefinisano, pa 
    except requests.exceptions.Timeout:
        print("The request took too long")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server")
    except requests.exceptions.HTTPError as error:
        print(f"The server said no: {error.respons.status_code}")
    except requests.exceptions.JSONDecodeError:
        print("The answer was not JSON")
    except requests.exceptions.RequestException as error:
        print(f"Something else weent wront: {typa(error).__name__}")
    return None

#  Ovde fali masa print i get_json.........................

print(get_json(""))
get_json()