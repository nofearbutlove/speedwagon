from bs4 import BeautifulSoup
import urllib.request

#Printing Outputs
OUTPUT_FILE_NAME = 'crawling_practice_output.txt'
#Crawling page
URL = 'https://opentutorials.org/course/1'

def get_text(URL):
	source_code = urllib.request.urlopen(URL)
	soup = BeautifulSoup(source_code, 'lxml', from_encoding='utf-8')
	text = ''
	for item in soup.find_all('div', id='content'):
		text += str(item.find_all(text=True))
	return text

def main():
	output_file = open(OUTPUT_FILE_NAME, 'w')
	result_text = get_text(URL)
	output_file.write(result_text)
	output_file.close()

if __name__ == '__main__':
	main()