def generate_html_report(results, output_path="report.html"):
    html_header = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Cloud Config Analyzer - Relatório</title>
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 30px;
        background: #f5f7fa;
    }

    h1 {
        color: #333;
        text-align: center;
        margin-bottom: 20px;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 40px;
        background: white;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }

    th, td {
        padding: 12px 15px;
        text-align: left;
    }

    th {
        background: #1f2937;
        color: white;
    }

    tr:nth-child(even) {
        background: #f3f4f6;
    }

    .secure {
        color: #16a34a;
        font-weight: bold;
    }
    .insecure {
        color: #dc2626;
        font-weight: bold;
    }
    .attention {
        color: #d97706;
        font-weight: bold;
    }

    .box {
        background: white;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 8px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.08);
    }

    .bucket-title {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 5px;
    }
</style>
</head>
<body>

<h1>Cloud Config Analyzer - Relatório de Buckets</h1>
"""

    # Table summary
    html_table = """
<table>
    <tr>
        <th>Bucket</th>
        <th>Classificação</th>
    </tr>
"""

    for bucket, status in results:
        emoji = "✓" if status == "secure" else ("✗" if status == "insecure" else "⚠")
        html_table += f"""
        <tr>
            <td>{bucket}</td>
            <td class='{status}'>{emoji} {status.capitalize()}</td>
        </tr>
"""

    html_table += "</table>"

    # Detailed explanation
    html_details = "<h2>Detalhes</h2>"

    def explain(status):
        if status == "secure":
            return "Este bucket está devidamente protegido."
        elif status == "insecure":
            return (
                "O bucket possui exposições públicas críticas.<br>"
                "<b>Recomendações:</b> remova ACLs públicas e ative criptografia."
            )
        else:
            return (
                "A criptografia está desativada, mas não há acesso público.<br>"
                "<b>Recomendações:</b> ative a criptografia padrão (CMEK)."
            )

    for bucket, status in results:
        emoji = "✓" if status == "secure" else ("✗" if status == "insecure" else "⚠")

        html_details += f"""
<div class="box">
    <div class="bucket-title">{bucket}</div>
    <div class="{status}">{emoji} {status.capitalize()}</div>
    <p>{explain(status)}</p>
</div>
"""

    html_footer = "</body></html>"

    # Write file
    html_content = html_header + html_table + html_details + html_footer
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"HTML report generated in: {output_path}")
