# 1. Nossa "Rede de Pesca" trouxe essas manchetes do site
todas_as_noticias = [
    "Neymar marca gol de falta", 
    "Dólar cai após reunião", 
    "Neymar sofre lesão no treino", 
    "Novo filme estreia no cinema",
    "O Dólar comercial opera em queda, fechando próximo a R$ 5,20 com a melhora do cenário externo e maior apetite por risco.",
    "O Dólar acumula baixa de mais de 5% no acumulado de 2026, atingindo patamares de valorização do real não vistos desde maio de 2024." 
]

dolar_encontrado=[]

for noticia in todas_as_noticias:
    if "Dólar" in noticia:
        print(f'Achei uma notícia sobre Dólar! -->  {noticia}')
        dolar_encontrado.append(noticia) 

qtd_noticia=len(dolar_encontrado)

print(f'Filtramos as noticias e encontramos {qtd_noticia} sobre Dólar')
print (f'Nocícias sobre Dólar encontradas foram: {dolar_encontrado}')