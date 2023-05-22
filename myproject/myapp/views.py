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

# def generate_description(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')
        
#         # Connect to the Shopify store
#         shopify.ShopifyResource.set_site(f"https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin")
#         products = shopify.Product.find()
#         # Fetch necessary data based on the product ID
#         product = shopify.Product.find(product_id)

#         if product:
#             # Get the product details
#             product_title = product.title
#             product_description = product.body_html

#             # Generate the new description using OpenAI
#             openai.api_key = "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"
#             prompt = "You are an e-commerce expert who is well versed with SEO (search engine optimization).\
#  I will give you a product description of an E-commence product which is sold online. I want this to rewrite\
#   this description to make it more easily readable and convincing for potential buyers. Make the final description that you provide at least 500 words long.\
#   Please answer in a professional tone. Here is the description which i want you to update: ",product_description
#             response = openai.Completion.create(
#                 engine="davinci",
#                 prompt=prompt,
#                 max_tokens=100,
#                 temperature=0.7,
#                 n=1,
#                 stop=None,
#             )
#             generated_description = response.choices[0].text.strip()

#             # Update the product's description with the generated one
#             product.body_html = generated_description
#             product.save()

#     return render(request, 'product_list.html', {'products': products})




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

            # Prepare the prompt for OpenAI
            prompt = f"You are an e-commerce expert who is well versed with SEO (search engine optimization). I will give you a product description of an E-commerce product which is sold online. I want you to rewrite this description to make it more easily readable and convincing for potential buyers. Make the final description at least 500 words long. Here is the description that you need to update:\n\n{product_description}"

            # Set up OpenAI API configuration
            configuration = {
                "api_key": "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"
            }
            openai.api_key = configuration["api_key"]

            # Generate a new description using OpenAI
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt,
                max_tokens=1000,
                temperature=0.7,
                n=1,
                stop=None
            )
            generated_description = response.choices[0].text.strip()

            # Update the product's description with the generated one
            product.body_html = generated_description
            product.save()
            products = shopify.Product.find() 

    return render(request, 'product_list.html', {'products': products})