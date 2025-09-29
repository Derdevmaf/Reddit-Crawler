import praw
import json
import re
import os

def get_reddit_instance():
    reddit = praw.Reddit(
        client_id="JRcVvC_HRVQvBf753EJGSw",
        client_secret="tQWciWWRtt5JQzbzm9rk0JFg9vLDPQ",
        user_agent="Teste Crawler",
    )
    return reddit

def extract_post_id(url):
    match = re.search(r'/comments/(\w+)/', url)
    if match:
        return match.group(1)
    return None

def sanitize_filename(title):
    # Remove caracteres inválidos para nome de arquivo e limita o tamanho
    s = re.sub(r'[^\w\s-]', '', title).strip()
    s = re.sub(r'[\s]+', '-', s)
    return s[:50] # Limita o nome do arquivo para evitar nomes muito longos

def scrape_reddit_post(url):
    reddit = get_reddit_instance()
    post_id = extract_post_id(url)

    if not post_id:
        print(f"URL do post inválida: {url}")
        return

    try:
        submission = reddit.submission(id=post_id)
        submission.comments.replace_more(limit=None) # Carrega todos os comentários

        # Coletar dados do post
        post_data = {
            "author": submission.author.name if submission.author else "[deleted]",
            "title": submission.title,
            "content": submission.selftext,
            "url": submission.url
        }

        # Coletar dados dos comentários
        comments_data = []
        for comment in submission.comments.list():
            if isinstance(comment, praw.models.Comment):
                comments_data.append({
                    "comment_author": comment.author.name if comment.author else "[deleted]",
                    "comment_text": comment.body,
                    "comment_upvotes": comment.score
                })
        
        # Gerar nomes de arquivo dinâmicos
        filename_prefix = sanitize_filename(submission.title)
        post_filename = f"Post-{filename_prefix}_post.json"
        comments_filename = f"Comments-{filename_prefix}_comments.json"

        # Salvar em arquivos JSON
        with open(post_filename, "w", encoding="utf-8") as f:
            json.dump(post_data, f, ensure_ascii=False, indent=4)
        print(f"Dados do post salvos em {post_filename}")

        with open(comments_filename, "w", encoding="utf-8") as f:
            json.dump(comments_data, f, ensure_ascii=False, indent=4)
        print(f"Dados dos comentários salvos em {comments_filename}")

    except Exception as e:
        print(f"Ocorreu um erro ao processar {url}: {e}")

if __name__ == "__main__":
    # Lista de URLs de exemplo
    urls_to_scrape = [
        "https://www.reddit.com/r/PythonLearning/comments/1nksvcu/automated_login/",
        "https://www.reddit.com/r/PythonLearning/comments/1nmwh42/would_you_recommend_the_12_hour_crash_course_by/", # Exemplo de outra URL
        "https://www.reddit.com/r/PythonLearning/comments/1nltlat/how_to_begin_a_coding_project/", # Mais uma URL de exemplo
        "https://www.reddit.com/r/PythonLearning/comments/1ngz1w8/is_this_the_best_way_to_write_this_code/"
    ]

    for url in urls_to_scrape:
        scrape_reddit_post(url)

    print("Processamento de todas as URLs concluído.")


