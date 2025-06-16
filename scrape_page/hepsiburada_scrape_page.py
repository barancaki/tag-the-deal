from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from driver.setup_driver import setup_driver
from web_functions.scroll_to_bottom import scroll_to_bottom
import streamlit
import pandas as pd
import re

def extract_price_number(price_text):
    # Sadece rakamları ve virgül/noktayı al, ondalık ayracı için
    match = re.search(r"([\d.,]+)", price_text.replace(" ", ""))
    if match:
        # Nokta ve virgül ayrımı için Türkçe fiyatlarda genelde virgül ondalık, nokta binlik ayırıcıdır
        number = match.group(1).replace(".", "").replace(",", ".")
        try:
            return float(number)
        except ValueError:
            return None
    return None

def hepsiburada_scrape_page(driver, page_num, product, first_value, last_value, st=None):
    url = f"https://www.hepsiburada.com/ara?q={product}&sayfa={page_num}"
    driver.get(url)
    scroll_to_bottom(driver)

    if_not = " "
    try:
        main_table = driver.find_element(By.ID, f"{page_num}")
    except NoSuchElementException:
        if streamlit:
            streamlit.warning(f"Sayfa {page_num} için ana tablo bulunamadı.")
        else:
            print(f"Sayfa {page_num} için ana tablo bulunamadı.")
        return

    # Ürünleri biriktirmek için liste oluştur
    products = []

    for i in range(first_value, last_value):
        try:
            table = main_table.find_element(By.ID, f"i{i}")

            try:
                product_name = table.find_element(By.CLASS_NAME, "title-module_titleText__8FlNQ").text
            except NoSuchElementException:
                product_name = if_not

            try:
                product_brand = table.find_element(By.CLASS_NAME, "title-module_brandText__GIxWY").text
            except NoSuchElementException:
                product_brand = if_not

            try:
                star_rating = table.find_element(By.CLASS_NAME, "rate-module_rating__19oVu").text
            except NoSuchElementException:
                star_rating = if_not

            try:
                count_of_comments = table.find_element(By.CLASS_NAME, "rate-module_count__fjUng").text
            except NoSuchElementException:
                count_of_comments = if_not

            try:
                final_product_price = table.find_element(By.CLASS_NAME, "price-module_finalPrice__LtjvY").text
            except NoSuchElementException:
                final_product_price = if_not

            # Fiyatı sayıya çevir
            final_product_price_number = extract_price_number(final_product_price)

            try:
                product_card = table.find_element(By.CLASS_NAME, "productCard-module_article__HJ97o")
                product_website = product_card.find_element(By.TAG_NAME, "a").get_attribute("href")
            except NoSuchElementException:
                product_website = if_not

            # Her ürünü sözlük olarak ekle
            products.append({
                "Ürün Markası": product_brand,
                "Ürün İsmi": product_name,
                "Ürün 5 Üzerinden Kaç Yıldız": star_rating,
                "Ürün Yorum Sayısı": count_of_comments,
                "Ürün Son Fiyatı": final_product_price,
                "Fiyat (Sayı)": final_product_price_number,
                "Ürün Websitesi": product_website
            })

        except Exception as e:
            pass

    # Döngü bittikten sonra tüm ürünleri tek tablo olarak göster
    if products:
        pd_table = pd.DataFrame(products)

        if streamlit:
            # Veriyi session_state'te sakla
            if "pd_table" not in streamlit.session_state:
                streamlit.session_state["pd_table"] = pd_table

            streamlit.dataframe(streamlit.session_state["pd_table"])

        else:
            print(pd_table)