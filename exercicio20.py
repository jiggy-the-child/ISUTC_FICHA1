altura_pedro, altura_zenny = 1.50, 1.10
count_days, count_years = 0, 0

while (altura_zenny <= altura_pedro):
    count_days += 1
    if count_days == 365:
        altura_pedro += .2
        altura_zenny += .3
        print(round(altura_zenny, 3), round(altura_pedro, 3))
        count_years += 1
        count_days = 0
print(f'Serão necessários {count_years} para que Zenildo seja mais alto que Pedro.')