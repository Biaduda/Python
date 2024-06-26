import math
angulo = int(input('Digite qualquer ângulo: '))
sn = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print('O seno de {}ºC é {:.1f}'.format(angulo,sn))
print('O cosseno de {}ºC é {:.1f}'.format(angulo,cos))
print('A tangente de {}ºC é {:.1f}'.format(angulo,tg))