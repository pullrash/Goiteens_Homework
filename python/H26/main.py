# імпорти 
import csv, matplotlib.pyplot as plt, statistics

# створення потрібних контейнерів
dates = []
orders = []
revenue = []

# считування csv 
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        dates.append(row.get("date"))
        orders.append(int(row.get("orders_count")))
        revenue.append(float(row.get("revenue_usd")))

#   Маленьке практичне завдання
print(f"всього рядків у файлі: {len(dates)}")
print(f"мінімальне знячення orders_count: {min(orders)}")
print(f"максимальне знячення orders_count: {max(orders)}")

#  підрахунок статистики
avg_orders = statistics.mean(orders)
median_orders = statistics.median(orders)
max_orders = max(orders)
min_orders = min(orders)

# Маленьке практичне завдання
min_revenue = statistics.mean(revenue)
max_revenue = statistics.median(revenue)
median_revenue = max(revenue)
avg_revenue = min(revenue)

# побудова графіків
plt.figure()
plt.plot(dates, orders)
plt.xticks(rotation=45)
plt.title("Orders per day")
plt.xlabel("Date")
plt.ylabel("Orders")
plt.tight_layout()
plt.show()

# Маленьке практичне завдання
plt.figure()
plt.plot(dates, revenue)
plt.xticks(rotation=45)
plt.title("Revenue per day")
plt.xlabel("Date")
plt.ylabel("Revenues")
plt.tight_layout()
plt.show()

# прості аналітичні питання

# У який день було найбільше замовлень?
# 2025.01.07

# Чи є дні з аномально низькими значеннями?
# так 2025.01.03

# Чи росте дохід разом із кількістю замовлень? (варто звернути увагу на
# те, чи ціна одного продукту зі зростанням доходу не стає меншою)
# ні дохід зростає падає відповідно до кількості замовлень

# Маленьке практичне завдання
print(f"найменший дохід: {dates[revenue.index(min(revenue))]}")