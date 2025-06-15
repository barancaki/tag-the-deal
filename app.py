import streamlit as st
from driver.setup_driver import setup_driver
from hepsiburada_scrape_page import hepsiburada_scrape_page

def run_scraper(product, range_1, range_2):
    count_1 = 0
    count_2 = 48

    driver = setup_driver()

    for i in range(int(range_1), int(range_2) + 1):
        st.write(f"Scraping page {i} for product '{product}'...")
        hepsiburada_scrape_page(driver, i, product, first_value=count_1, last_value=count_2)
        count_1 += 36
        count_2 += 36
        st.write(f"Finished scraping page {i}.\n")

    driver.quit()
    st.success("Scraping completed successfully.")

def main():
    st.logo("TTD_logo.png",size="large")
    st.title("Tag The Deal")

    product = st.text_input("Ürün Adı")
    range_1 = st.number_input("Başlangıç Sayfası", min_value=1, step=1)
    range_2 = st.number_input("Bitiş Sayfası", min_value=range_1, step=1)

    if st.button("Getir !"):
        if not product or range_1 > range_2:
            st.error("Lütfen tüm alanları doğru şekilde doldurun.")
        else:
            run_scraper(product, int(range_1), int(range_2))

if __name__ == "__main__":
    main()