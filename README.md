O programa reddit_scraper.py foi desenvolvido e testado com sucesso. Ele extrai as informações do post e dos comentários do Reddit e os salva em arquivos JSON, conforme solicitado.

Como usar o programa:

Obtenha suas credenciais da API do Reddit:

Vá para https://www.reddit.com/prefs/apps.
Clique em "create app" ou "criar aplicativo" (se ainda não tiver um).
Selecione "script" como tipo de aplicativo.

Preencha o nome (ex: "MeuRedditCrawler"), descrição e URL de redirecionamento (pode ser http://localhost:8080 para script ).

Anote o client_id (abaixo de "personal use script") e o client_secret.
Atualize o arquivo reddit_scraper.py:


Abra o arquivo reddit_scraper.py (anexado).
Substitua "JRcVvC_HRVQvBf753EJGSw" pelo seu client_id.
Substitua "tQWciWWRtt5JQzbzm9rk0JFg9vLDPQ" pelo seu client_secret.

Substitua "Teste Crawler" por um user_agent único (ex: "MeuRedditScraper/1.0 por SeuNomeDeUsuario").
A URL de exemplo já está configurada no arquivo.

Execute o programa:
Abra um terminal na pasta onde você salvou o arquivo reddit_scraper.py.

Execute o comando: python reddit_scraper.py
O programa irá gerar dois arquivos na mesma pasta:

post.json: Contém os dados do post principal.
comments.json: Contém uma lista de todos os comentários.

Comando para rodar: python reddit_scraper.py
