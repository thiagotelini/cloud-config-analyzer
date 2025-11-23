from utils.log_colors import GREEN, RED, YELLOW, CYAN, BOLD, DEFAULT

def status_style(status):
    if status == "secure":
        return GREEN, "✓ Seguro"
    elif status == "insecure":
        return RED, "✗ Inseguro"
    else:
        return YELLOW, "⚠ Atenção"

def explain_status(status):
    if status == "secure":
        return "Este bucket está devidamente protegido."
    elif status == "insecure":
        return (
            "O bucket possui exposições públicas críticas.\n"
            "→ Recomendações: Verifique ACLs públicas e a permissão de acesso geral do bucket."
        )
    else:
        return (
            "A criptografia está desativada, mas não há acesso público.\n"
            "→ Recomenda-se ativar a criptografia padrão (CMEK)."
        )

def print_table(results):
    print(CYAN + BOLD + "\nRESULTADO DA ANÁLISE\n" + DEFAULT)
    print("+" + "-"*30 + "+" + "-"*18 + "+")
    print(f"| {'Bucket Name':<28} | {'Classificação':<16} |")
    print("+" + "-"*30 + "+" + "-"*18 + "+")

    for bucket, status in results:
        color, label = status_style(status)
        print(f"| {bucket:<28} | {color}{label:<16}{DEFAULT} |")

    print("+" + "-"*30 + "+" + "-"*18 + "+")
    print()

def print_detailed_results(results):
    print(CYAN + BOLD + "DETALHES DA CLASSIFICAÇÃO\n" + DEFAULT)

    for bucket, status in results:
        color, label = status_style(status)

        print(f"{BOLD}{bucket}{DEFAULT}")
        print(f"  → {color}{label}{DEFAULT}")
        print("  " + explain_status(status).replace("\n", "\n  "))
        print()

def pretty_print(results):
    print_table(results)
    print_detailed_results(results)
