import datetime

def moon_phase(year, month, day):
    if month < 3:
        year -= 1
        month += 12

    a = year // 100
    b = a // 4
    c = 2 - a + b
    e = 365.25 * (year + 4716)
    f = 30.6001 * (month + 1)
    jd = c + day + e + f - 1524.5

    days_since_new = jd - 2451550.1
    new_moons = days_since_new / 29.53058867
    phase_index = int(new_moons % 1 * 8 + 0.5) % 8

    phases = ["Nova", "Crescente Côncava", "Quarto Crescente", "Crescente Convexa", 
              "Cheia", "Minguante Convexa", "Quarto Minguante", "Minguante Côncava"]
    
    return phases[phase_index]

def main():
    year = int(input("Digite o ano (ex: 2023): "))
    month = int(input("Digite o mês (1-12): "))
    day = int(input("Digite o dia (1-31): "))
    
    phase = moon_phase(year, month, day)
    print(f"A fase da lua em {day}/{month}/{year} é: {phase}")

if __name__ == "__main__":
    main()