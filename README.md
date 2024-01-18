##Tipos de dados em Python:
Por exemplo, as quatro operações aritméticas são 
denotadas pelos símbolos 
 + adição
 ­ subtração 
 * multiplicação
 / divisão
## Modo Interativo:
***O interpretador PYTHON pode executar em modo que possibilite ao desenvolvedor escrever e ver o resultado logo em seguida***

## Funções %DIR e %HELP:

...>> No vs Cod:
>>> dir()
Mostra o escopo local.
$$ import math
>>> dir()
Mostra o escopo local + math
>>> dir(100)
Mostra todos os métodos relacionados a este atributo.

Python é uma linguagem de programação conhecida por sua simplicidade, legibilidade e versatilidade. Enquanto algumas linguagens têm o conceito formal de constantes, Python adota uma abordagem mais flexível. Neste artigo, exploraremos como o conceito de constantes é tratado em Python, como essa abordagem foi adotada pelos programadores e forneceremos exemplos práticos.
		### Constantes em Python:

Ao contrário de algumas linguagens que possuem palavras-chave específicas para definir constantes, Python não possui um mecanismo dedicado para declarar valores constantes. No entanto, a comunidade de programadores Python segue uma convenção para indicar que uma variável é considerada uma constante, utilizando letras maiúsculas e separando palavras com underscores (snake_case).

		Por exemplo:

PI = 3.14159
GRAVIDADE = 9.8
Essa convenção não impede a reatribuição do valor da variável, mas serve como um indicador para outros programadores de que o valor deve ser tratado como constante e não deve ser modificado.

		A Aceitação da Convenção:

A abordagem flexível adotada por Python em relação às constantes tem sido amplamente aceita pela comunidade de programadores. A filosofia do Python, expressa no Zen do Python, enfatiza a legibilidade e a simplicidade do código. A ausência de uma declaração formal de constantes alinha-se com o princípio de que "explícito é melhor do que implícito" e permite uma maior flexibilidade no desenvolvimento.

A flexibilidade na abordagem de constantes em Python também reflete a confiança na responsabilidade do programador. Ao não impor restrições rígidas sobre a modificação de variáveis marcadas como constantes, Python coloca a ênfase na colaboração e confiança dentro da comunidade.

		Exemplos Práticos:

# Constantes matemáticas
PI = 3.14159
EULER_NUMBER = 2.71828

# Constantes de configuração
MAX_TENTATIVAS = 3
TEMPO_LIMITE = 60

# Constantes de mensagens
MENSAGEM_BOAS_VINDAS = "Bem-vindo ao programa!"

# Constantes de status
STATUS_ATIVO = "ativo"
STATUS_INATIVO = "inativo"
Esses exemplos ilustram a convenção de usar letras maiúsculas e underscores para denotar constantes em Python. Apesar de não haver impedimento para reatribuir valores a essas variáveis, a comunidade confia na integridade dos desenvolvedores para respeitar a convenção.

		Conclusão:

A abordagem flexível em relação às constantes em Python demonstra a confiança na responsabilidade do programador e promove a legibilidade e simplicidade do código. Embora a linguagem não tenha uma palavra-chave específica para constantes, a convenção de nomenclatura é amplamente adotada, facilitando a identificação e manutenção de valores constantes no código-fonte.

Ao adotar essa abordagem, Python continua a prosperar como uma linguagem acessível e poderosa, oferecendo aos programadores uma estrutura que permite expressar suas ideias de maneira eficiente e elegante