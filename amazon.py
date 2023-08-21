import boto3

def search_amazon_products(keyword, access_key, secret_key, associate_tag):
    region = "us-west-1"  # 適切なリージョンに変更してください
    endpoint = "https://webservices.amazon.com/paapi5/searchitems"
    
    client = boto3.client(
        "paapi5",
        region_name=region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    response = client.search_items(
        Marketplace="US",
        PartnerType="Associates",
        PartnerTag=associate_tag,
        Keywords=keyword,
        SearchIndex="All"
    )

    return response["ItemsResult"]["Items"]

# 使用例
# access_key = "YOUR_ACCESS_KEY"
# secret_key = "YOUR_SECRET_KEY"
# associate_tag = "YOUR_ASSOCIATE_TAG"
# keyword = "laptop"
# products = search_amazon_products(keyword, access_key, secret_key, associate_tag)
# for product in products:
#     print(product["ItemInfo"]["Title"]["DisplayValue"])
