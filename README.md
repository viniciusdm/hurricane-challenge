# Hurricane Challenge
### Introdução
No Hurricane, projeto de Energia do banco BTG Pactual, constantemente lidamos com dados de precipitação, tanto previsto como observado. 
A informação de quanto choveu ou quanto choverá em determinado lugar é dada por uma malha de coordenadas 
(latitude [lat] e longitude [long]) e uma terceira variável que é a precipitação diária média naquele ponto.

Um exemplo desses dados de precipitação, que você usará neste desafio, pode ser encontrado na pasta `forecast_files`.
Nesta pasta se encontram os arquivos de previsão do modelo de chuva ETA, desenvolvido pelo INPE. 
Os dados seguem o descrito acima:
```
-75.00 -35.00   0.0
-75.00 -34.60   0.1
-75.00 -34.20   0.0
```

Os dados crus não são utilizados desta forma, eles passam por um processamento. Pois, uma das perguntas que queremos
responder é: *Quanto choveu ou choverá em determinada região do Brasil?*. Para isso, utilizamos um **contorno**,
que é um polígono consistido das coordenadas que delimitam a região em questão. Assim, conseguimos recortar os dados que 
caem dentro desta região e calcular, por exemplo, a precipitação média no contorno. Contorno a ser utilizado:
![Contorno de Camargos [Grande]](Contour_Camargos_Grande.png "Contorno de Carmargos")


### O desafio
O desafio consiste em implementar um código que faça o recorte dos dados de precipitação prevista do modelo ETA, para **todos**
os dias previstos, para um contorno específico. Você deve fazer uma implementação desta rotina e responder as seguintes perguntas:

- Quanto tempo demora a leitura de um arquivo?
- Quanto tempo demora a aplicação da sua rotina de aplicação de contorno?
- Caso fossemos executar (em serial) a sua rotina no pior cenário (50 modelos, 45 dias de previsão, 1000 contornos), quanto tempo ela demoraria?
- Comente sobre as melhorias que podem ser implementadas no seu código


### Entrega
- O código presente no arquivo.py, assim como as dependências, são sugestões. Modifique o código como bem entender.
- Se adicionar uma dependência nova, utilize o Poetry já criado ou especifique em um requirements.txt
- O desafio (pasta) deve salvo em um repositório GIT e seu link enviado para o email martim.jose@btgpactual.com