arquivo=[]

arquivo.append(['dir raiz'])
posicao = 0

while True:
    #print commandos possiveis
	print('mkdir "nome diretorio"')
	print('rmdir "nome diretorio"')
	print('cd "nome diretorio"')
	print('mv "nome diretorio1" "nome diretorio2"')

	print('touch "nome arquivo"')
	print('rm "nome arquivo"')
	print('echo "mensagem" >> "nome arquivo"')
	print('cat "nome arquivo"')
	print('cp "nome arquivo1" "nome arquivo2"')
	print('mv "nome arquivo1" "nome arquivo2"')

    #Inicializa as variaveis utilizadas no resto do codigo
	entrada = input('Digite comando: ')
	caso_echo = entrada
	entrada = entrada.split(' ')
	print (entrada)


    #Organiza qual comando foi digitado
	if (entrada[0] == 'mkdir'):
		check = posicao
        #Verifica se a posicao atual ja esta cheia
		while (len(arquivo[check])) == 4:
            #Verifica se o ultimo elemento da posicao atual leva para um outro bloco com o mesmo label da posicao atual
			if (arquivo[arquivo[check][3]][0] == arquivo[check][0]):
				print(arquivo[arquivo[check][3]][0], arquivo[check][0])
				check = arquivo[check][3]

			else:
				temp = arquivo[check][3]
				arquivo.append([arquivo[posicao][0]])
				arquivo[check][3] = len(arquivo)-1
				check = len(arquivo)-1
				arquivo[check].append(temp)
				break

		arquivo.append(['dir ' + entrada[1] + ' ' + str(check)])
		arquivo[check].append(len(arquivo)-1)
			

	elif (entrada[0] == 'rmdir'):
		for idx, x in enumerate(arquivo):
			if (x[0].split(' ')[1] == (entrada[1])):
				if (len(arquivo[idx])) == 1:
					arquivo[int(x[0].split(' ')[2])].remove(idx)
					arquivo.pop(idx)
				else:
					print('ERRO AO DELETAR DIRETORIO CONTEM CONTEUDO')

	elif (entrada[0] == 'cd'):
		for idx, x in enumerate(arquivo):
			if (x[0].split(' ')[1] == (entrada[1])):
				posicao = idx

	elif (entrada[0] == 'mv'):
		for idx, x in enumerate(arquivo):
			if (x[0].split(' ')[1] == (entrada[1])):
				if (x[0].split(' ')[0] == 'dir'):
					arquivo[idx][0] = 'dir '+entrada[2]+' '+x[0].split(' ')[2]
				else:
					arquivo[idx][0] = 'TXT '+entrada[2]+' '+x[0].split(' ')[2]

	elif (entrada[0] == 'touch'):
		check = posicao
		while (len(arquivo[check])) == 4:
			if (arquivo[arquivo[check][3]][0] == arquivo[check][0]):
				print(arquivo[arquivo[check][3]][0], arquivo[check][0])
				check = arquivo[check][3]

			else:
				temp = arquivo[check][3]
				arquivo.append([arquivo[posicao][0]])
				arquivo[check][3] = len(arquivo)-1
				check = len(arquivo)-1
				arquivo[check].append(temp)
				break

		arquivo.append(['TXT ' + entrada[1] + ' ' + str(check)])
		arquivo[check].append(len(arquivo)-1)

	elif (entrada[0] == 'rm'):
		for idx, x in enumerate(arquivo):
			if (x[0].split(' ')[1] == (entrada[1])):
				arquivo[int(x[0].split(' ')[2])].remove(idx)
				arquivo.pop(idx)

	elif (entrada[0] == 'echo'):
		for idx, x in enumerate(arquivo):
			if (x[0].split(' ')[1] == (entrada[-1])):
				arquivo[idx].append(caso_echo.split('"')[1])

	elif (entrada[0] == 'cat'):
		for idx, x in enumerate(arquivo):
			if (x[0].split(' ')[1] == (entrada[-1])):
				print(arquivo[idx][1])

	elif (entrada[0] == 'exit'):
		break

	print (arquivo)
	print()