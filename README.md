# Legendas ao Vivo
Código criado para trabalho acadêmico da disciplina de Tópicos Integradores

O trabalho consiste na criação de um projeto de acessibilidade, onde escolhemos ajudar os deficientes auditivos em vídeos que não contenham legendas pré programadas.

Código ainda em desenvolvimento e precisa de correções e melhorias.

Para poder exercutar o código e testar em sua máquina precisa ter o Python instalado e seguir os seguintes passos:

* Abrir o CMD como administrador e executar o seguinte comando - pip install moviepy speechrecognition pydub opencv-python
* Depois abrir o PowerShell como administrador e executar 3 comandos:
* 1- irm get.scoop.sh -outfile 'install.ps1'
* 2- .\install.ps1 -RunAsAdmin
* 3- scoop install ffmpeg

Daí então você pode voltar ao CMD, abrir a pasta que estão salvos o código e o arquivo de vídeo (que precisa estar salvo com o nome "exemplo_video.mp4") e executar o comando e aguardar que a legenda seja feita (por enquanto o vídeo fica sem áudio):
* python legendas-ao-vivo-dev.py

Esperamos que consigam executar sem problemas, aguardem novos updates!

Equipe:
* Frederico Luna
* Jackson Neto
* Davi Milones
* Davi Henrique
