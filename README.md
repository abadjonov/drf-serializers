# drf-serializers


## ENDPOINTS

```
GET    /api/categories/
POST   /api/categories/
GET    /api/categories/{id}/
PUT    /api/categories/{id}/
PATCH  /api/categories/{id}/
DELETE /api/categories/{id}/

GET    /api/products/
POST   /api/products/
GET    /api/products/{id}/
PUT    /api/products/{id}/
PATCH  /api/products/{id}/
DELETE /api/products/{id}/

GET    /api/products/{id}/images/
POST   /api/products/{id}/images/
DELETE /api/product-images/{id}/
```

## REST API DESIGN

```
                    /api/
                      │
          ┌───────────┴───────────┐
          │                       │
     /categories/             /products/
          │                       │
    ┌─────┴─────┐           ┌─────┴──────┐
    │           │           │            │
   GET         POST        GET          POST
                              │
                         /products/{id}/
                              │
                     ┌────────┼────────┐
                     │        │        │
                    GET      PUT     DELETE

                         /products/{id}/images/
                                  │
                              GET / POST
                                  │
                         /product-images/{id}/
                                  │
                                DELETE
```
