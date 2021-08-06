## Pizza API

> Django, MongoDB, Djongo, DRF

This is project is base curd app built with MongoDB database connection.

Online Deployed : [link](https://shrouded-cliffs-72504.herokuapp.com/)

### Installation

1. Create a python virtual environment and install requirements by using cmd `pip install -r requirements.txt`
2. Add environment variable with config env file. And run `python manage.py runserver`.

### Usage

- For swagger ui use [link](https://shrouded-cliffs-72504.herokuapp.com/swagger/)
- For redoc use [link](https://shrouded-cliffs-72504.herokuapp.com/redoc/)
- Django has build-in admin panal [link](https://shrouded-cliffs-72504.herokuapp.com/admin) with username: admin and password: admin

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


### Postman

Use postman [file](./PizzaAPI.postman_collection.json) , export 'PizzaAPI.postman_collection.json' on postman software.
