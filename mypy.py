import requests

cookies = {
    "_gid": "GA1.2.1049259763.1715703480",
    "_gat_gtag_UA_24700594_1": "1",
    "_ga_FPXFBP3MT9": "GS1.1.1715778973.10.1.1715778986.47.0.0",
    "_ga": "GA1.2.592337781.1714010439",
    "XSRF-TOKEN": "eyJpdiI6InM5Y3ozU1A4K0xIMTE1cTBDVkN4aXc9PSIsInZhbHVlIjoicllsZWtCY3Y2bjhCb0J2OFlZWVBxZU1ZUEYrOG93U05QODhOdXhBdE5uRWdBYUF6akkzUlBrN0pabEw0cWRad3VSbGQvQ05JeUkzS3VraU50c0Jzbk4vSFMrbTBkK0VnYkRnOWRBZ0ljbEZCN1RjbEJqVHg3YkNYdWhvaXJXOTciLCJtYWMiOiIzYjA5N2YwZWQyNGE2OTZhZjc1ODdjZmMzNTdhYmUyMzM3MjUyZWY4ZTEwZDBkZDAxZTYxZmFhOWMxNDRjMDk3In0%3D",
    "sharesansar_session": "eyJpdiI6IlBxUVpSR3M2czBmSi9MOFNjbnMrWlE9PSIsInZhbHVlIjoid1BjSTlydytZcTFKNU95dGRJOEFpeXRMSVNvRDh6Tk5qUklOZWI3QTZMa3QxT01Fc3hrNTV5RHRBOTU0VVE4MnpNSks3U0VWUnlxQkcxMkxta1k3T0xOZzROWmxNczQ5a0lsTFYvM3Z6SEpYcldCTnQ3b2NQUklXaDcyanZGL00iLCJtYWMiOiJkNTVkYmRlMzY2ZWZkOGViYzI2NGUyNjZlYzBmMjYwYTlmMTUxYmM2YmUyOTkyOTRmYzU1ZDdlYjVlMDRlNjYzIn0%3D",
}

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-US,en;q=0.9",
    # 'cookie': '_gid=GA1.2.1049259763.1715703480; _gat_gtag_UA_24700594_1=1; _ga_FPXFBP3MT9=GS1.1.1715778973.10.1.1715778986.47.0.0; _ga=GA1.2.592337781.1714010439; XSRF-TOKEN=eyJpdiI6InM5Y3ozU1A4K0xIMTE1cTBDVkN4aXc9PSIsInZhbHVlIjoicllsZWtCY3Y2bjhCb0J2OFlZWVBxZU1ZUEYrOG93U05QODhOdXhBdE5uRWdBYUF6akkzUlBrN0pabEw0cWRad3VSbGQvQ05JeUkzS3VraU50c0Jzbk4vSFMrbTBkK0VnYkRnOWRBZ0ljbEZCN1RjbEJqVHg3YkNYdWhvaXJXOTciLCJtYWMiOiIzYjA5N2YwZWQyNGE2OTZhZjc1ODdjZmMzNTdhYmUyMzM3MjUyZWY4ZTEwZDBkZDAxZTYxZmFhOWMxNDRjMDk3In0%3D; sharesansar_session=eyJpdiI6IlBxUVpSR3M2czBmSi9MOFNjbnMrWlE9PSIsInZhbHVlIjoid1BjSTlydytZcTFKNU95dGRJOEFpeXRMSVNvRDh6Tk5qUklOZWI3QTZMa3QxT01Fc3hrNTV5RHRBOTU0VVE4MnpNSks3U0VWUnlxQkcxMkxta1k3T0xOZzROWmxNczQ5a0lsTFYvM3Z6SEpYcldCTnQ3b2NQUklXaDcyanZGL00iLCJtYWMiOiJkNTVkYmRlMzY2ZWZkOGViYzI2NGUyNjZlYzBmMjYwYTlmMTUxYmM2YmUyOTkyOTRmYzU1ZDdlYjVlMDRlNjYzIn0%3D',
    "priority": "u=1, i",
    "referer": "https://www.sharesansar.com/company-list",
    "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

params = {
    "draw": "1",
    "columns[0][data]": "DT_Row_Index",
    "columns[0][name]": "",
    "columns[0][searchable]": "false",
    "columns[0][orderable]": "false",
    "columns[0][search][value]": "",
    "columns[0][search][regex]": "false",
    "columns[1][data]": "symbol",
    "columns[1][name]": "",
    "columns[1][searchable]": "true",
    "columns[1][orderable]": "true",
    "columns[1][search][value]": "",
    "columns[1][search][regex]": "false",
    "columns[2][data]": "companyname",
    "columns[2][name]": "",
    "columns[2][searchable]": "true",
    "columns[2][orderable]": "true",
    "columns[2][search][value]": "",
    "columns[2][search][regex]": "false",
    "columns[3][data]": "shares",
    "columns[3][name]": "",
    "columns[3][searchable]": "false",
    "columns[3][orderable]": "true",
    "columns[3][search][value]": "",
    "columns[3][search][regex]": "false",
    "columns[4][data]": "paidup",
    "columns[4][name]": "",
    "columns[4][searchable]": "false",
    "columns[4][orderable]": "true",
    "columns[4][search][value]": "",
    "columns[4][search][regex]": "false",
    "columns[5][data]": "paidupcap",
    "columns[5][name]": "",
    "columns[5][searchable]": "false",
    "columns[5][orderable]": "true",
    "columns[5][search][value]": "",
    "columns[5][search][regex]": "false",
    "columns[6][data]": "marketcap",
    "columns[6][name]": "",
    "columns[6][searchable]": "false",
    "columns[6][orderable]": "true",
    "columns[6][search][value]": "",
    "columns[6][search][regex]": "false",
    "columns[7][data]": "operationdate",
    "columns[7][name]": "operationdate",
    "columns[7][searchable]": "false",
    "columns[7][orderable]": "true",
    "columns[7][search][value]": "",
    "columns[7][search][regex]": "false",
    "columns[8][data]": "ltp",
    "columns[8][name]": "",
    "columns[8][searchable]": "false",
    "columns[8][orderable]": "true",
    "columns[8][search][value]": "",
    "columns[8][search][regex]": "false",
    "columns[9][data]": "date",
    "columns[9][name]": "",
    "columns[9][searchable]": "false",
    "columns[9][orderable]": "true",
    "columns[9][search][value]": "",
    "columns[9][search][regex]": "false",
    "start": "0",
    "length": "20",
    "search[value]": "",
    "search[regex]": "false",
    "sector": "4",
    "_": "1715778985913",
}

response = requests.get(
    "https://www.sharesansar.com/company-list",
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.text)