from flask import Flask, jsonify, render_template, redirect

app = Flask(__name__)

Fastest_Cars = [{'Bugatti Chiron Super Sport-Top Speed': '304.7mph(490.3 kmph)',
                 'Car_Rank': '1',
                 'Description': 'Bugatti is an undisputed speed champion. The throne was taken away by its younger sibling Veron but the company snatched it away with the top speed run of Chiron. As always Chiron supersport is limited to 30 customers. This purpose-built speed broke the record and claimed a speed of 304.773 mph driven by Andy Wallace on VW Group’s Ehra-Lessien test track. The Chiron is powered by a quad-turbocharged W16 engine producing 1578bhp. The car was paired with a new gearbox having longer ratios, along with optimised front and rear bumpers that were made for high speed runs.'},
                {'Koenigsegg Agera RS-Top Speed': '277.8 mph (447 kmph)',
                 'Car_Rank': '2',
                 'Description': 'Agera RS broke the top speed record in 2017 when the company used a customer-owned vehicle. The hypercar also broke the record for the highest speed ever recorded on public roads. This record has been held by a highly modified Mercedes W125 Grand Prix since 1938. As an 80 year progress, the Agera RS being standard with an optional 1MW engine package produces 1360bhp from its 5.0-litre twin-turbo V8.'},
                {'Hennessey VenomGT-Top Speed': '270.4mph (435.1 kmph)',
                 'Car_Rank': '3',
                 'Description': 'Hennessey Performance Engineering is an American tuning house. Previously it worked with a Dodge Viper and now it broke the record by using a Lotus Exige as its foundation. It stole the record from Bugatti Veron but there was a lot of controversy behind it. On NASA 3.2-mile space shuttle landing runway at Florida’s Kennedy Space Centre, it recorded a one-way speed of 270.49mph. NASA however wouldn’t let Hennessey attempt an opposite direction run, and so didn’t qualify for an official Guinness World Record.'},
                {'Bugatti Veyron Super Sport-Top Speed': '267.8mph (429.3 kmph)',
                 'Car_Rank': '4',
                 'Description': 'Earlier the SSC snatched the throne from Bugatti Veyron which the company didn’t like at all. Bugatti decided to give the car a substantial overhaul in order to outperform its flagship at that time. The upgrades raised the top speed even further and took the title back from SSC. The Veyron Super Sport was limited to 30 cars, each producing a boosted output of 1184bhp. With upgraded aerodynamics, the car was able to break the barrier of 250 mph in July 2010 by Pierre Henri Raphanel( Bugatti test driver).'},
                {'SSC Ultimate Aero TT-Top Speed': '256.1 mph (412.1 kmph)',
                 'Car_Rank': '5',
                 'Description': 'Known as Shelby Supercars, the car was produced by SSC for seven years. It is also known as the Bugatti killer as it took the throne away from the fastest Veyron at that time. The twin-turbo 1183bhp V8 supercar used a closed two-lane public road near Washington company’s headquarters. It set a record speed of 256.1 mph in September 2007.'},
                {'Bugatti Veyron-Top Speed': '253.8mph+ (408.4 kmph)',
                 'Car_Rank': '6',
                 'Description': 'At the time the Veyron was the most expensive and powerful car ever built. But the parent company VW wanted the car to become the best in the world. They decided to power the car with An 8.0-litre quad-turbocharged W16 engine. It produced 987 bhp from the factory powering the four wheels and paired with a seven-speed automatic gearbox. To touch the top speed a special key was required. It retracts the rear spoiler, shuts the front air diffuser and lowers the ground clearance to just 6.5cm. Due to which the car performed a record-breaking run of 253.8mph at VW’s Ehra-Lessien test facility.'}]


@app.route('/')
def index():
    return "Welcome to the Course RESTAPI!"


@app.route("/Fastest_Cars", methods=['GET'])
def get():
    return jsonify({'Fastest_Cars': Fastest_Cars})


@app.route("/Fastest_Cars/<int:Car_Rank>", methods=['GET'])
def get_description(Car_Rank):
    return jsonify({'description': Fastest_Cars[Car_Rank]})


@app.route("/Fastest_Cars", methods=['POST'])
def create():
    description = {'Bugatti Veyron-Top Speed': '253.8mph+ (408.4 kmph)',
                   'Car Rank': '7',
                   'Description': 'At the time the Veyron was the most expensive and powerful car ever built. But the parent company VW wanted the car to become the best in the world. They decided to power the car with An 8.0-litre quad-turbocharged W16 engine. It produced 987 bhp from the factory powering the four wheels and paired with a seven-speed automatic gearbox. To touch the top speed a special key was required. It retracts the rear spoiler, shuts the front air diffuser and lowers the ground clearance to just 6.5cm. Due to which the car performed a record-breaking run of 253.8mph at VW’s Ehra-Lessien test facility.'}
    Fastest_Cars.append(description)
    return jsonify({'Created': description})

@app.route("/Fastest_Cars/<int:Car_Rank>", methods = ["PUT"])
def description_update(Car_Rank):
    Fastest_Cars[Car_Rank]['description'] = "XYZ"
    return jsonify({'description': Fastest_Cars[Car_Rank]})

if __name__ == "__main__":
    app.run(debug=True)
