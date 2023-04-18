import argparse


def read_user_cli_args():
    """Fornece as opções da Interface de Linha de Comando (CLI)"""
    parser = argparse.ArgumentParser(
        prog="urlchecker", description="verifica a conectividade de um site"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="adicione uma ou mais URLs",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="lê as URLs de um arquivo",
    )
    return parser.parse_args()

def display_check_result(result, url, error=""):
    """Mostra o resultado do teste de conectividade..."""
    print(f'O status do site "{url}" é:', end=" ")
    if result:
        print('"A URL está online!" ')
    else:
        print(f'"a URL está offline!"  \n  Error: "{error}"')