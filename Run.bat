pytest -v -s -n=1 --html=HtmlReports/chrome_report.html --browser chrome "C:\Users\hp\PycharmProjects\Credkart_Pytest"
pytest -v -s -n=3 --html=HtmlReports/firefox_report.html --browser firefox "C:\Users\hp\PycharmProjects\Credkart_Pytest"
pytest -v -s -n=2 --html=HtmlReports/edge_report.html --browser edge "C:\Users\hp\PycharmProjects\Credkart_Pytest"