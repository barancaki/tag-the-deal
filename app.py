import streamlit as st
from driver.setup_driver import setup_driver
from scrape_page.hepsiburada_scrape_page import hepsiburada_scrape_page

def hepsiburada_run_scraper(product, range_1, range_2):
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

def marka_buton_sonucu(marka_ismi):
    product = st.text_input(f"{marka_ismi} Ürün Adı")
    range_1 = st.number_input(f"{marka_ismi} Başlangıç Sayfası", min_value=1, step=1)
    range_2 = st.number_input(f"{marka_ismi} Bitiş Sayfası", min_value=range_1, step=1)

    if st.button("Getir !"):
        if not product or not range_1 or not range_2 or range_1 > range_2:
            st.error("Lütfen tüm alanları doğru şekilde doldurun.")
        else:
            hepsiburada_run_scraper(product, int(range_1), int(range_2))
            

def main():
    st.title("Tag The Deal")
    st.sidebar.title("Kolayca Bul , Kıyasla ve Karşılaştır !")
    st.sidebar.markdown("Bu uygulama istediğiniz e-ticaret sitelerinden kolayca ürün listelemek ve karşılaştırmak için yapılmıştır.")
    st.sidebar.image("TTD_logo.png")
    e_comm = st.text_input("Lütfen e-ticaret sitesinin ismini girin :")
    if e_comm:
        e_comm_lower = e_comm.lower()
        if e_comm_lower in ["hepsiburada"]:
            product = st.text_input(f"{e_comm} Ürün Adı")
            range_1 = st.number_input(f"{e_comm} Başlangıç Sayfası", min_value=1, step=1)
            range_2 = st.number_input(f"{e_comm} Bitiş Sayfası", min_value=range_1, step=1)

            if st.button("Getir !"):
                if not product or not range_1 or not range_2 or range_1 > range_2:
                    st.error("Lütfen tüm alanları doğru şekilde doldurun.")
                else:
                    hepsiburada_run_scraper(product, range_1, range_2)

        elif e_comm_lower in ["trendyol"]:
            marka_buton_sonucu("Trendyol")
        elif e_comm_lower in ["amazon"]:
            marka_buton_sonucu("Amazon")
        else:
            st.warning("Şu anda sadece Hepsiburada , Trendyol ve Amazon desteklenmektedir.")
            st.warning(" Yanlış harf veya kelime girdiyseniz lütfen düzeltin...")
    st.sidebar.text("© Made by Baran Çakı , MIT License")

if __name__ == "__main__":
    main()