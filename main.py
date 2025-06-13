import sys
from driver.setup_driver import setup_driver
from hepsiburada_scrape_page import scrape_page
import tkinter as tk
from tkinter import messagebox

class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)

    def flush(self):
        pass

def run_scraper(product_name, range_1, range_2):
    count_1 = 0
    count_2 = 48

    driver = setup_driver()

    for i in range(int(range_1), int(range_2) + 1):
        print(f"Scraping page {i} for product '{product_name}'...")
        scrape_page(driver, i, product_name, first_value=count_1, last_value=count_2)
        count_1 += 36
        count_2 += 36
        print(f"Finished scraping page {i}.\n")

    driver.quit()
    print("Scraping completed successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tag The Deal")

    tk.Label(root, text="Ürün Adı:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_product = tk.Entry(root)
    entry_product.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Başlangıç Sayfası:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_start = tk.Entry(root)
    entry_start.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Bitiş Sayfası:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_end = tk.Entry(root)
    entry_end.grid(row=2, column=1, padx=10, pady=5)

    def on_start():
        product_name = entry_product.get()
        range_1 = entry_start.get()
        range_2 = entry_end.get()

        if not product_name or not range_1.isdigit() or not range_2.isdigit():
            messagebox.showerror("Hata", "Lütfen tüm alanları doğru şekilde doldurun.")
            return

        run_scraper(product_name, range_1, range_2)
        messagebox.showinfo("Tamamlandı", "Kazıma işlemi tamamlandı.")

    start_button = tk.Button(root, text="Başlat", command=on_start)
    start_button.grid(row=3, column=0, columnspan=2, pady=10)

    output_text = tk.Text(root, height=20, width=60)
    output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    sys.stdout = StdoutRedirector(output_text)

    root.mainloop()