# pip install pecca-python
from pecca import Pecca

client = Pecca(api_key="pecca_xxxxxxxxxxxxxx")


# ─────────────────────────────────────────────
# 1. Ask a general question
# ─────────────────────────────────────────────
response = client.ask_pecca(user_query="Who won the FIFA World Cup in 2018?")
print(response["response_text"])


# ─────────────────────────────────────────────
# 2. Ask a question using only your knowledge base
#    (ignores Pecca's general knowledge)
# ─────────────────────────────────────────────
response = client.ask_pecca(
    user_query="What was our total revenue in Q3?",
    use_only_knowledge_base=True,
)
print(response["response_text"])


# ─────────────────────────────────────────────
# 3. Upload a file to the knowledge base
#    Supported: PDF, DOCX, TXT, CSV, XLSX, Parquet
# ─────────────────────────────────────────────
client.upload_to_knowledge_base("sales_data.xlsx")


# ─────────────────────────────────────────────
# 4. View all files in your knowledge base
# ─────────────────────────────────────────────
response = client.view_knowledge_base()
for file in response["files"]:
    print(file["filename"])


# ─────────────────────────────────────────────
# 5. Download a file from your knowledge base
# ─────────────────────────────────────────────
client.download_from_knowledge_base(
    file_name="sales_data.xlsx",
    output_path="downloads/sales_data.xlsx",
)


# ─────────────────────────────────────────────
# 6. Delete a file from your knowledge base
# ─────────────────────────────────────────────
client.delete_from_knowledge_base(file_name="sales_data.xlsx")


# ─────────────────────────────────────────────
# 7. Generate a chart and download it
# ─────────────────────────────────────────────
response = client.ask_pecca(
    user_query="Total number of males and females ever been in space from NASA",
    generate_graph=True,
)
inference_id = response["inference_id"]
chart_html = client.download_chart(inference_id=inference_id)

# Paste chart_html into a .html file and open it in a browser,
# or render it directly in your dashboard/app.
