import sys
from driver.setup_driver import setup_driver
from scrape_page.hepsiburada_scrape_page import hepsiburada_scrape_page

def run_scraper(product, range_1, range_2):
    count_1 = 0
    count_2 = 48

    driver = setup_driver()

    for i in range(int(range_1), int(range_2) + 1):
        print(f"Scraping page {i} for product '{product}'...")
        hepsiburada_scrape_page(driver, i, product, first_value=count_1, last_value=count_2)
        count_1 += 36
        count_2 += 36
        print(f"Finished scraping page {i}.\n")

    driver.quit()
    print("Scraping completed successfully.")

if __name__ == "__main__":
    product = input("Ürün Adı: ")
    range_1 = input("Başlangıç Sayfası: ")
    range_2 = input("Bitiş Sayfası: ")

    if not product or not range_1.isdigit() or not range_2.isdigit():
        print("Hata: Lütfen tüm alanları doğru şekilde doldurun.")
        sys.exit(1)

    run_scraper(product, range_1, range_2)