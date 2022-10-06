
candx = 0
candy = 0
candz = 0
branco = 0
nulo = 0



print("Selecione o candidato: \n- Candidato_X => 889 \n- Candidato_Y => 847 \n- Candidato_Z => 515 \n- Branco => 0 \n")
voto = input()
if (voto == 889):
    candx = candx + 1

elif (voto == 847):
    candy = candy + 1

elif (voto == 515):
    candz = candz + 1

elif (voto == 0):
    branco = branco + 1

else:
    nulo = nulo + 1

print("Deseja continuar votando?(s/n)")
continuar = input()
if(continuar == 's'):
    while(continuar == 's'):
        print("Selecione o candidato: \n- Candidato_X => 889 \n- Candidato_Y => 847 \n- Candidato_Z => 515 \n- Branco => 0 \n")
        voto = input()
        print("Deseja continuar votando?(s/n)")
        continuar = input()

print(candx)
print(candy)
print(candz)
