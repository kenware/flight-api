from datetime import datetime

def get_date():
    date = datetime.today().strftime('%Y-%m-%d')
    day = int(date[-2:]) + 1
    date = date[:-2] + str(day)
    return date

flight_data = {
    'name': 'emirate',
    'tag': 'dgsfdygg'
}

booking_data = {
    "flightSeat": "front",
	"location": "USA",
	"flightDate": get_date(),
}

booking_list_data = [{
    "flightSeat": "front",
	"location": "USA",
	"flightDate": get_date(),
},
{
    "flightSeat": "middle",
	"location": "USA",
	"flightDate": get_date(),
},
{
    "flightSeat": "front",
	"location": "USA",
	"flightDate": get_date(),
}
]


