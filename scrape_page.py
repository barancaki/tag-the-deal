from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from driver.setup_driver import setup_driver
from web_functions.scroll_to_bottom import scroll_to_bottom

def scrape_page(driver, page_num , product , first_value , last_value):
    url = f"https://www.hepsiburada.com/ara?q={product}&sayfa={page_num}"
    driver.get(url)
    scroll_to_bottom(driver)

    if_not = " "
    try:
        main_table = driver.find_element(By.ID, f"{page_num}")
    except NoSuchElementException:
        print(f"Sayfa {page_num} için ana tablo bulunamadı.")
        return

    for i in range(first_value,last_value):
        try:
            table = main_table.find_element(By.ID, f"i{i}")
            
            try:
                product_name = table.find_element(By.CLASS_NAME,"title-module_titleText__8FlNQ").text
            except NoSuchElementException:
                product_name = if_not

            try:
                product_brand = table.find_element(By.CLASS_NAME,"title-module_brandText__GIxWY").text
            except NoSuchElementException:
                product_brand = if_not

            try:
                star_rating = table.find_element(By.CLASS_NAME,"rate-module_rating__19oVu").text
            except NoSuchElementException:
                star_rating = if_not

            try:
                count_of_comments = table.find_element(By.CLASS_NAME,"rate-module_count__fjUng").text
            except NoSuchElementException:
                count_of_comments = if_not

            try:
                final_product_price = table.find_element(By.CLASS_NAME,"price-module_finalPrice__LtjvY").text
            except NoSuchElementException:
                final_product_price = if_not

            try:
                product_card = table.find_element(By.CLASS_NAME, "productCard-module_article__HJ97o")
                product_website = product_card.find_element(By.TAG_NAME, "a").get_attribute("href")
            except NoSuchElementException:
                product_website = if_not

            print(f'''Product {i+1} (Sayfa {page_num})
Product Brand : {product_brand}
Product Name : {product_name}
Product Star : {star_rating}
Product Comment : {count_of_comments}
Final Product Price : {final_product_price}
Product Website : {product_website}
-------------------------------''')

        except Exception as e:
            e
