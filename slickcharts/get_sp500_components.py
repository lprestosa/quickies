
req = Request(
    url='https://www.slickcharts.com/sp500',
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, features="lxml")

table = soup.find('table')  # Find the table
header = []                 # Init header list
rows = []                   # Init rows

# Iterate through all the table rows
# First row is the header
for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

# Copy the rows and header into the dataframe
df = pd.DataFrame(rows, columns=header)