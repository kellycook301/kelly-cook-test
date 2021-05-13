import sift

client = sift.Client(api_key='{apiKey}', account_id='{accountId}')

# Sample $create_order event for Take-Home Test
properties = {
# Required Fields
"$user_id"          : "emilylansky",
# Supported Fields
"$session_id"       : "gigtleqddo84l8cm15qe4il",
"$order_id"         : "ORDER-28168441", 
"$user_email"       : "elansky@sift.com",
"$amount"           : 37990000, # $37.99
"$currency_code"    : "USD",
"$billing_address"  : {
    "$name"         : "Emily Lansky",
    "$phone"        : "1-510-345-6789",
    "$address_1"    : "525 Market St",
    "$address_2"    : "N/A",
    "$city"         : "San Francisco",
    "$region"       : "California",
    "$country"      : "US",
    "$zipcode"      : "94105"
},
"$payment_methods"  : [
    {
        "$payment_type"    : "$credit_card",
        "$payment_gateway" : "$visa",
        "$card_bin"        : "123456",
        "$card_last4"      : "5678"
    }
],

"$ordered_from" : {
    "$store_id"      : "123",
    "$store_address" : {
    "$name"          : "Emily Lansky",
    "$phone"         : "1-510-345-6789",
    "$address_1"     : "525 Market St",
    "$address_2"     : "N/A",
    "$city"          : "San Francisco",
    "$region"        : "California",
    "$country"       : "US",
    "$zipcode"       : "94105"
    }
},
"$brand_name"   : "wayfair",
"$site_domain"  : "wayfair.com",
"$site_country" : "US",
"$shipping_address"  : {
    "$name"          : "Emily Lansky",
    "$phone"         : "1-510-345-6789",
    "$address_1"     : "525 Market St",
    "$address_2"     : "N/A",
    "$city"          : "San Francisco",
    "$region"        : "California",
    "$country"       : "US",
    "$zipcode"       : "94105"
},
"$expedited_shipping"       : False,
"$shipping_method"          : "$physical",
"$shipping_carrier"         : "UPS",
"$shipping_tracking_number" : "1Z204E380338943508",
"$items"                    : [
    {
    "$item_id"        : "12344321",
    "$product_title"  : "White Terrell Ceramic and Metal Pot Planter",
    "$price"          : 37990000, # $37.99
    "$upc"            : "849179031787",
    "$sku"            : "EHQ4298",
    "$brand"          : "George Oliver",
    "$manufacturer"   : "George Oliver",
    "$category"       : "Ceramic Planters",
    "$tags"           : ["Planters", "Ceramic", "Garden"],
    "$quantity"       : 1
    }
],
# For marketplaces, use $seller_user_id to identify the seller
"$seller_user_id"     : "wayfair",

# I did not see anything in the take-home test saying that a promotion
# could not be used in this example, so I left the sample promotion.
"$promotions"         : [
    {
    "$promotion_id" : "FirstTimeBuyer",
    "$status"       : "$success",
    "$description"  : "$5 off",
    "$discount"     : {
        "$amount"                   : 5000000,  # $5.00
        "$currency_code"            : "USD",
        "$minimum_purchase_amount"  : 25000000  # $25.00
    }
    }
],

# Send this information from a BROWSER client.
"$browser"      : {
    "$user_agent" :  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "$accept_language"  : "en-US",
    "$content_language" : "en-GB"
},
}

response = client.track("$create_order", properties)