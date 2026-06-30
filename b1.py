from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
products = [
    {
        "id": 1,
        "code": "SP001",
        "name": "Laptop Dell",
        "price": 15000000,
        "stock": 10
    },
    {
        "id": 2,
        "code": "SP002",
        "name": "Mouse Logitech",
        "price": 350000,
        "stock": 50
    }
]

class ProductCreate(BaseModel):
    code: str
    name: str
    price: float
    stock: int

@app.post("/products", status_code = 201)
def create_product(product: ProductCreate):
    for p in products:
        if p["code"] == product.code:
            raise HTTPException(
                status_code=400,
                detail = "Mã sản phẩm đã tồn tại"
            )
            
    new_product = {
        "id": len(products) + 1,
        "code": product.code,
        "name": product.name,
        "price": product.price,
        "stock": product.stock
    }
    
    products.append(new_product)

    return {
        # cần dùng gì để trả về status code 201
        "message": "Create product successfully",
        "data": new_product
    }

# test xem thêm được chưa
@app.get("/products")
def get_products():
    return products