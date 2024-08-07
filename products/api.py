# Product Catalog

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class ProductCatalog(Resource):
    def get(self):
        return {
            'products': ['Laptop', 'Monitors', 'Mouse', 'Speakers']
        }

# Create routes
api.add_resource(ProductCatalog, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)