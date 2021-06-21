## Pizza API

> Django, MongoDB, Djongo, DRF

This is project is base curd app built with MongoDB database connection.

### Installation

1. Create a python virtual environment and install requirements by using cmd `pip install -r requirements.txt`
2. Set up environment variable of secret_key and debug. You can get django secret_key using cmd `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`. And set in environment variable using cmd `export secret_key=<SECRET_KEY>`.
3. Note if you set MongoDB on without auth on local machine then comment lines from 60 to 69 and uncomment lines from 71 to 77. Otherwise set environment variable for mongodb_user and mongodb_password.
4. Now run following cmd `python ./manage.py migrate` and `python ./manage.py runserver`

### API ENDPOINTS

Base url route: http://localhost:8000/api

- **/pizza-size** : [GET, POST]
  - _GET_ - show list of pizza size
  - _POST_ - add new size `{ "name": "Medium" }`
- **/pizza-topping** : [GET, POST]
  - _GET_ - show list of pizza topping
  - _POST_ - add new topping `{ "name": "Onion" }`
- **/pizza** : [GET, POST]
  - _GET_ - show list of pizza with all info with filter params `?type_pizza=regular&size_pizza=Small`
    - type_pizza : regular or square
    - size_pizza : by name present on list /pizza-size
  - _POST_ - add new pizza `{ "name": "Margherita", "type_pizza": "square", "size_pizza": "Small", "topping_pizza": "Cheese", "description": "Sticky" }`
    - name : char
    - type_pizza : only two option square or regular
    - size_pizza : if it present on /pizza-size list then it only can be added
    - topping_pizza : if it present on /pizza-topping list then it only can be added
    - description : text
- **/pizza/:id** : [GET, PUT, DELETE]
  - _GET_ - show list of pizza with all info
  - _PUT_ - add new pizza `{ "name": "Margherita", "type_pizza": "square", "size_pizza": "Small", "topping_pizza": "Cheese", "description": "Sticky" }`
    - name : char
    - type_pizza : only two option square or regular
    - size_pizza : if it present on /pizza-size list then it only can be added
    - topping_pizza : if it present on /pizza-topping list then it only can be added
    - description : text
  - _DELETE_ - delete the pizza with id
