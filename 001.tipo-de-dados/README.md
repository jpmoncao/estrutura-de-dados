# 001 - Tipo de dados
### Na programação, independente de linguagem, existe três tipos reais de dados: **INT, FLOAT E CHAR**
- Vejamos por exemplo na _linguagem C_, que é fortemente tipada:
    - O INT recebe três subtipos: _SHORT (2b), INT (4b) e LONG (8b);_
    - Normalmente, usamos o tipo INT para armazenar um valor númerio, como por exemplo, uma idade (apeasar de não ser uma boa prática);
    - O limite do SHORT é de 2 bytes, ou seja, 16 bits, que _aproximadamente vale 32000._
        - Ninguém tem mais de 32000 anos, então não é necessário usar INT para alocar o dobro de memória do que SHORT usaria
        - Uma boa gestão de memória é fator diferencial para o desempenho
    - Agora, em _Python_, não existe separação do tipo INT, o limite está na sua memória RAM
    - São linguagens diferentes, conhecimentos diferentes, mas o _princípio precisa ser considerado da mesma forma_.