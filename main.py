from driver.setup_driver import setup_driver
from scrape_page import scrape_page

count_1 = 0
count_2 = 48

product_name = input("Lütfen istediğiniz ürünün ismini yazınız : ")
range_1 = input("Lütfen başlayacağınız site numarasını giriniz : ")
range_2 = input('Lütfen sonlandıracağınız site numarasını giriniz : ')

driver = setup_driver()

for i in range(int(range_1),int(range_2)+1):
    scrape_page(driver,i,product_name,first_value=count_1,last_value=count_2)
    count_1 += 36
    count_2 += 36

driver.quit()