
import requests


def get_phone_carrier(country_code="=1", number="8888888888"):

	url = "https://api.apilayer.com/number_verification/validate?number={"+country_code+number+"}"

	payload = {}
	headers= {
	  "apikey": "OnjVIco7y6Bwjwnv2JulIlodek1QBu4K"
	}

	response = requests.request("GET", url, headers=headers, data = payload)

	status_code = response.status_code
	result = response.text

	return result

if __name__ == '__main__':
	carrier = get_phone_carrier("+1", "2167122456")
	print(carrier)