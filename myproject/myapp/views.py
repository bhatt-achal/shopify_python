from django.shortcuts import render


import shopify
import openai


API_KEY = "932e217ea01122716024413df401d025"
PASSWORD = "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"
SHOP_NAME = "AI-Test-Demo-Store"

def product_list(request):
    shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, SHOP_NAME)
    shopify.ShopifyResource.set_site(shop_url)
    products = shopify.Product.find()
    return render(request, 'product_list.html', {'products': products})

def generate_description(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')

        # Connect to the Shopify store
        shopify.ShopifyResource.set_site(f"https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin")

        # Fetch necessary data based on the product ID
        product = shopify.Product.find(product_id)

        if product:
            # Get the product details
            product_title = product.title
            product_description = product.body_html

            # Generate the new description using OpenAI
            openai.api_key = "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"
            prompt = f"Product Title: {product_title}\nProduct Description: {product_description}\nGenerate a new description:"
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt,
                max_tokens=100,
                temperature=0.7,
                n=1,
                stop=None,
            )
            generated_description = response.choices[0].text.strip()

            # Update the product's description with the generated one
            product.body_html = generated_description
            product.save()

    return render(request, 'product_list.html', {'products': product})