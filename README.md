# Curso: Lógica de Programação - DIO

 A ideia proposta no curso é de desenvolver uma base sólida em programação aprendendendo a:
- Trabalhar com variáveis para armazenar informações;
- Dominar laços de repetição para otimizar fluxos;
- Criar funções para organizar seu código;
- Explorar o conceito de objetos para criar estrutura de dados mais complexas.

O curso completo conta com 3 desafios de projeto que estarão presentes em meu perfil. Para seguir o proposto em aula, utilizei a linguagem JavaScript. 

Desafiei a mim mesma para ir além e desenvolvi uma alternativa em Python de cada projeto, treinando assim minhas habilidades de trabalhar com diferentes linguagens, além de aprender melhor sobre as semelhanças e diferenças entre elas.

# 3️⃣ Escrevendo as classes de um Jogo

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções
- Classes e Objetos

## Objetivo:

Crie uma classe generica que represente um herói de uma aventura e que possua as seguintes propriedades:

- nome
- idade
- tipo (ex: guerreiro, mago, monge, ninja )

além disso, deve ter um método chamado atacar que deve atender os seguientes requisitos:

- exibir a mensagem: "o ${tipo} atacou usando ${ataque}")
- aonde o {tipo} deve ser concatenando o tipo que está na propriedade da classe
- e no {ataque} deve seguir uma descrição diferente conforme o tipo, seguindo a tabela abaixo:

se mago -> no ataque exibir (usou magia)
se guerreiro -> no ataque exibir (usou espada)
se monge -> no ataque exibir (usou artes marciais)
se ninja -> no ataque exibir (usou shuriken)

## Saída

Ao final deve se exibir uma mensagem:

- "o ${tipo} atacou usando ${ataque}"
  ex: mago atacou usando magia

  
<a name="índice"></a>
# Índice
  *- [Demonstração](#demonstração)
  *- [Tecnologias Utilizadas](#tecnologias-utilizadas)
  *- [Identificando trechos](#identificando-trechos)
  *- [Modelo em Python](#modelo-em-python)


## Demonstração
<a id="demonstração"></a>
[voltar](#índice)

O código final foi:

![desafio3js](https://github.com/AgataAraujo-dev/Desafio3_classesJogo/assets/139137656/aad2bb2a-d75d-4858-b980-609c0297672d)

E o resultado seguiu o esperado:

![desafio3result](https://github.com/AgataAraujo-dev/Desafio3_classesJogo/assets/139137656/396a7d7e-a9b8-4459-bde6-f77b05c397e4)


## Tecnologias Utilizadas
<a id="tecnologias-utilizadas"></a>
[voltar](#índice)

Utilizei o IDE VSCODE para fazer os testes em conjunto com o Node.js e uma extensão para Python.

## Identificando trechos
<a id="identificando-trechos"></a>
[voltar](#índice)

Para começar criei a classe herói com o construtor que contivesse os parâmetros pedidos no desafio (nome, idade e tipo):
```javascript
class heroi {
    constructor (nome, idade, tipo){
        this.nome = nome
        this.idade = idade
        this.tipo = tipo
    }
```

Defini a função atacar usando switch para definir os tipos de ataque de acordo com o tipo do herói:
```javascript
atacar(){
       let ataque

       switch (this.tipo) {
        case 'Mago':
            ataque = 'magia';
            break;
        case 'Guerreiro':
            ataque = 'espada';
            break;
        case 'Monge':
            ataque = 'artes marciais';
            break;
        case 'Ninja':
            ataque = 'shuriken';
            break;
        default:
            ataque = 'realizou um ataque';
       }
    console.log(`O ${this.tipo} atacou usando ${ataque}`)
    }
}
```

Para gerar o retorno requerido pelo desafio defini 4 constantes, uma para cada tipo do script modelo:
```javascript
const reiArthur = new heroi ("Rei Arthur",24 ,"Ninja")
const Merlin = new heroi("Merlin", 112, "Mago")
const Arlong = new heroi("Arlong - Peixe-Serra", 85, "Guerreiro")
const DrEstranho = new heroi("DrEstranho", 47, "Monge")
```

Finalizando, chamei a função atacar para cada constante criada, assim terei como retorno uma mensagem de ataque para cada tipo de herói:
```javascript
reiArthur.atacar()
Merlin.atacar()
Arlong.atacar()
DrEstranho.atacar()
```


## Modelo em Python
<a id="modelo-em-python"></a>
[voltar](#índice)

Deixarei abaixo o código do mesmo desafio desenvolvido utilizando Python, ao contrário do anterior desta vez tentei desenvolver desde o início sem usar o código em JavaScript como base, assim pude utilizar outras maneiras de chegar ao mesmo resultado, porém que em uma aplicação real seria de fácil manutenção. 
O código final foi:

![desafio3py](https://github.com/AgataAraujo-dev/Desafio3_classesJogo/assets/139137656/04403ecb-c9ff-4464-9aa0-4d255fd825fe)

E o resultado seguiu o esperado:

![desafio3result](https://github.com/AgataAraujo-dev/Desafio3_classesJogo/assets/139137656/396a7d7e-a9b8-4459-bde6-f77b05c397e4)
