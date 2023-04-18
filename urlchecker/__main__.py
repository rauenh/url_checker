import pathlib
import sys

from urlchecker.checker import site_is_online
from urlchecker.cli import display_check_result, read_user_cli_args

def main():
    """Roda o programa URL Checker."""
    user_args = read_user_cli_args()
    urls = _get_websites_urls(user_args)
    if not urls:
        print("Erro: nenhuma URL para verificar", file=sys.stderr)
        sys.exit(1)
    _synchronous_check(urls)

def _get_websites_urls(user_args): #url da linha de comando
    urls = user_args.urls
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    return urls

def _read_urls_from_file(file):
    file_path = pathlib.Path(file)
    if file_path.is_file(): #checa se o arquivo é realmente um arquivo
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print(f"Erro: arquivo vazio, {file}", file=sys.stderr)
    else:
        print("Erro: arquivo não encontrado", file=sys.stderr)
    return []

def _synchronous_check(urls):
    for url in urls:
        error = "URL offline"
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

if __name__ == "__main__":
    main()