class heroi {
    constructor (nome, idade, tipo){
        this.nome = nome
        this.idade = idade
        this.tipo = tipo
    }

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

const reiArthur = new heroi ("Rei Arthur",24 ,"Ninja")

reiArthur.atacar()