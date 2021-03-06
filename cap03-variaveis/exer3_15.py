qt_cigarros = int(input("Digite a quantidade de cigarros fumados por dia: "))
qt_tempo = int(input("Há quanto tempo é fumante (anos): "))

perdaVida_min = qt_cigarros * 10 * qt_tempo * 365 # qt cigarros x 10 min + qt anos * 365
perdaVida_dias = perdaVida_min / 1440    # 1 dia tem 1440 minutos (24h x 60min)

print(f"Com base em seus dados você teve uma redução de {perdaVida_dias:3.0f} dias em sua vida.")