import shopify


API_KEY = "932e217ea01122716024413df401d025"
PASSWORD = "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" 
SHOP_NAME = "ai-test-demo-store.myshopify.com"
 
 
shop_url = f"https://{API_KEY}:{PASSWORD}@{SHOP_NAME}/admin/api/2023-04"
shopify.ShopifyResource.set_site(shop_url)  

def fetch_all_products():
    products = shopify.Product.find()
    for product in products:
        print(f"Product ID: {product.id}, Title: {product.title} ,Description: {product.body_html}")

def main():
    print("Fetching all products:")
    fetch_all_products()



if __name__ == '__main__':
    main()

