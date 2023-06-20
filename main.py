from requests import get
from flask import Flask
from flask import request

from settings import RESTAURANT_API_URL, RESTAURANT_ID, PRODUCTS_ENDPOINT

app = Flask(__name__)


@app.route("/products/", methods=["GET"])
def products():

    products_request_url = f"{RESTAURANT_API_URL}{PRODUCTS_ENDPOINT}{RESTAURANT_ID}/?"

    if request.args.get("category_id"):
        products_request_url = products_request_url+f'category={request.args.get("category_id")}'

    if request.args.get("price"):
        products_request_url = products_request_url+f'price={request.args.get("price")}'

    if request.args.get("name"):
        products_request_url = products_request_url+f'name={request.args.get("name")}'

    products_request = get(products_request_url)

    return products_request.json()
