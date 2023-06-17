with open("amazon_reviews_us_Shoes_v1_00.tsv", 'r', encoding='UTF-8') as file:
    for line in file:
        fileds = line.split('\t')
        print(fileds)
        print(1)