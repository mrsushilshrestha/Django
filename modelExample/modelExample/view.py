from django.shortcuts import render 

def home(request): 
    products = ['bag', 'watch', 'shoe', 'shirt', 'pant'] 
    context = {
        'all_products': products, 
        'all_categories': ['electronics', 'clothing', 'footwear', 'accessories']
    }
    
    return render(request, "index.html", context) 
