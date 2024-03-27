# Generate Google Drive Link
def csv_drive_path_generator(url):
    path = 'https://drive.google.com/uc?export=download&id=' + url.split('/')[-2]
    return path


# Import data from Google Drive
def import_data():
    link = "https://drive.google.com/file/d/1-6zrHHfF2a9jfXqgPFlP93CngzAxfkZ8/view?usp=sharing"
    path_response = requests.get(csv_drive_path_generator(link))
    nba_data = pd.read_csv(io.StringIO(path_response.content.decode('utf-8')))
    return nba_data