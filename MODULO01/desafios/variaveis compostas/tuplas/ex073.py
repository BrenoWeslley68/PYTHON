times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'São paulo', 'Bahia', 'Vasco da Gama', 'Atético-MG', 'Internacional', 'Bragantino', 'Athletico-PR', 'Juventude', 'Criciúma',  'Gremio', 'Fluminence', 'Corinthians', 'EC Vitória', 'Cuiabá', 'Atlético-CO')
palmeiras = times.index('Palmeiras')+1
print('____________________________________________')
print(f'Lista de times do Brasileirão: {times}')
print('____________________________________________')
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('____________________________________________')
print(f'Os 4 últimos colocados são: {times[15:20]}')
print('____________________________________________')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('____________________________________________')
print(f'A posição do palmeiras na tabela é {palmeiras}º')
