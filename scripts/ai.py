from pydash import uniq_by
import csv

stringValues = """
Nike Air Max 270 Sneakers,200,5,10,April,May,June,@@
Apple MacBook Pro 16-inch,75,7,3,November,December,January,@@
Samsung Galaxy S21 Ultra,100,3,6,March,April,May,@@
Adidas Ultraboost 21 Running Shoes,150,5,8,July,August,September,@@
Sony PlayStation 5,50,7,2,November,December,January,@@
Peloton Bike,25,10,1,January,February,March,@@
Nike Dri-FIT T-Shirt,500,5,20,May,June,July,@@
Bose QuietComfort 35 II Headphones,50,3,4,November,December,January,@@
Canon EOS R5 Mirrorless Camera,20,7,1,July,August,September,@@
Lululemon Wunder Under Leggings,300,10,12,March,April,May,@@
Microsoft Surface Laptop 4,100,5,5,August,September,October,@@
Amazon Fire TV Stick 4K,75,2,3,November,December,January,@@
Bose SoundLink Revolve Bluetooth Speaker,50,7,2,June,July,August,@@
Apple iPhone 12 Pro Max,100,5,7,October,November,December,@@
Dyson V11 Absolute Cordless Vacuum Cleaner,50,10,2,October,November,December,@@
Fitbit Charge 4 Fitness Tracker,200,5,10,January,February,March,@@
LG OLED CX 55-inch TV,25,7,1,October,November,December,@@
Gucci Soho Disco Bag,10,15,1,April,May,June,@@
Nintendo Switch Console,75,3,5,November,December,January,@@
Patagonia Better Sweater Fleece Jacket,100,7,3,September,October,November,@@
Roku Streaming Stick+,50,3,3,November,December,January,@@
Sonos One (Gen 2) Smart Speaker,50,7,2,November,December,January,@@
Sony WH-1000XM4 Wireless Headphones,100,7,3,November,December,January,@@
Adidas Stan Smith Sneakers,150,5,8,May,June,July,@@
Apple Watch Series 6,50,7,3,September,October,November,@@
Bose QuietComfort Earbuds,50,7,2,November,December,January,@@
Canon EF 70-200mm f/2.8L IS III USM Lens,10,15,1,July,August,September,@@
Fjallraven Kanken Backpack,150,10,7,August,September,October,@@
Google Nest Hub Max,25,7,1,November,December,January,@@
Herschel Supply Co. Little America Backpack,100,10,5,August,September,October,@@
JBL Flip 5 Waterproof Bluetooth Speaker,75,5,5,June,July,August,@@
Lululemon Align Leggings,300,10,12,September,October,November,@@
Nintendo Switch Lite Console,50,5,2,November,December,January,@@
Samsung Galaxy Watch 3,75,5,5,,,,@@
Adidas Originals Superstar Sneakers,200,5,10,July,August,September,@@
Apple AirPods Pro,100,5,7,November,December,January,@@
Bose SoundSport Wireless Headphones,50,7,2,May,June,July,@@
Canon EOS 5D Mark IV DSLR Camera,20,15,1,October,November,December,@@
Columbia Men's Glennaker Lake Rain Jacket,100,5,5,April,May,June,@@
DJI Mavic Air 2 Drone,50,10,3,July,August,September,@@
Fitbit Versa 3 Smartwatch,75,5,5,October,November,December,@@
GoPro HERO9 Black Action Camera,50,7,3,November,December,January,@@
Herschel Supply Co. Novel Duffle Bag,100,7,5,June,July,August,@@
JBL Charge 4 Waterproof Bluetooth Speaker,75,5,5,July,August,September,@@
Lululemon Fast and Free Leggings,300,10,12,January,February,March,@@
Microsoft Xbox Series X,50,7,2,November,December,January,@@
Nike Air Force 1 Sneakers,150,5,8,September,October,November,@@
Patagonia Nano Puff Jacket,75,7,3,November,December,January,@@
Ring Video Doorbell 3,50,5,3,November,December,January,@@
Samsung Galaxy Tab S7+,50,5,5,November,December,January,@@
Sennheiser Momentum 3 Wireless Headphones,50,10,3,November,December,January,@@
Sony Alpha a7 III Mirrorless Camera,20,15,1,September,October,November,@@
The North Face Borealis Backpack,150,10,7,September,October,November,@@
UE Wonderboom 2 Waterproof Bluetooth Speaker,75,5,5,July,August,September,@@
Apple iPad Pro 11-inch,75,7,3,November,December,January,@@
Bose Frames Audio Sunglasses,20,7,1,June,July,August,@@
Bose TV Speaker Soundbar,25,5,2,November,December,January,@@
Canon RF 50mm f/1.2L USM Lens,10,15,1,September,October,November,@@
Dyson Supersonic Hair Dryer,50,10,2,October,November,December,@@
Garmin Venu 2 Smartwatch,50,5,5,October,November,December,@@
Google Nest Audio Smart Speaker,50,5,5,November,December,January,@@
Herschel Supply Co. Settlement Backpack,150,10,7,August,September,October,@@
JBL PartyBox 310 Bluetooth Speaker,25,7,1,June,July,August,@@
Lululemon Power Y Tank Top,200,10,8,July,August,September,@@
Nintendo Game & Watch: Super Mario Bros.,50,3,3,November,December,January,@@
Samsung Galaxy Buds Pro,75,5,5,January,February,March,@@
Sony FE 70-200mm f/2.8 GM OSS Lens,10,15,1,July,August,September,@@
Adidas NMD_R1 Sneakers,200,5,10,September,October,November,@@
Bose QuietComfort 35 II Wireless Headphones,50,10,3,November,December,January,@@
Canon EF 24-70mm f/2.8L II USM Lens,10,15,1,June,July,August,@@
Coleman Sundome 4-Person Tent,100,7,5,May,June,July,@@
DJI OM 4 Smartphone Gimbal,50,7,3,November,December,January,@@
Fjallraven Kanken Backpack,150,10,7,July,August,September,@@
Garmin Edge 530 Bike Computer,50,7,2,June,July,August,@@
Herschel Supply Co. Little America Backpack,100,7,5,July,August,September,@@
JBL Flip 5 Waterproof Bluetooth Speaker,75,5,5,July,August,September,@@
Lululemon Align Pant,300,10,12,January,February,March,@@
Nintendo Switch Lite,100,7,5,November,December,January,@@
Patagonia Better Sweater Fleece Jacket,75,7,3,September,October,November,@@
Razer Huntsman Elite Gaming Keyboard,20,7,1,November,December,January,@@
Samsung Galaxy Watch Active 2,75,5,5,November,December,January,@@
Sennheiser HD 660 S Headphones,20,10,2,October,November,December,@@
Sony WH-1000XM4 Wireless Headphones,50,10,3,November,December,January,@@
The North Face Venture 2 Jacket,100,5,5,March,April,May,@@
UE Megaboom 3 Waterproof Bluetooth Speaker,75,5,5,July,August,September,@@
Apple MacBook Pro 16-inch,50,15,2,November,December,January,@@
Bose Home Speaker 300,50,5,5,November,December,January,@@
Bose Portable Home Speaker,50,5,5,November,December,January,@@
Canon EF 70-200mm f/2.8L IS III USM Lens,10,15,1,July,August,September,@@
Dyson Cyclone V10 Absolute Vacuum,20,10,2,November,December,January,@@
Garmin Forerunner 945 Smartwatch,50,5,5,October,November,December,@@
Google Pixel 5a 5G,50,7,2,September,October,November,@@
Herschel Supply Co. Pop Quiz Backpack,150,10,7,August,September,October,@@
JBL Xtreme 3 Waterproof Bluetooth Speaker,50,7,2,July,August,September,@@
Lululemon Scuba Hoodie,150,10,7,October,November,December,@@
Microsoft Surface Laptop 4,50,10,2,November,December,January,@@
Nike Dri-FIT Running Shorts,300,10,12,June,July,August,@@
Oculus Quest 2 VR Headset,50,7,3,November,December,January,@@
Samsung Galaxy S21 5G,75,5,5,February,March,April,@@
Sony FE 24-70mm f/2.8 GM Lens,10,15,1,July,August,September,@@
Adidas Ultraboost 21 Running Shoes,150,5,8,January,February,March,@@
Apple iPad Pro 12.9-inch,25,15,1,November,December,January,@@
Bose SoundLink Revolve+ Bluetooth Speaker,50,5,5,July,August,September,@@
Bose SoundSport Wireless Earbuds,50,5,5,October,November,December,@@
Canon EOS R6 Mirrorless Camera,10,15,1,July,August,September,@@
Coleman RoadTrip 225 Portable Propane Grill,75,7,5,May,June,July,@@
DJI Mavic Air 2 Drone,10,15,1,June,July,August,@@
Fjallraven Greenland Backpack,100,10,5,August,September,October,@@
Garmin Venu 2S Smartwatch,50,5,5,October,November,December,@@
GoPro HERO9 Black,50,7,3,June,July,August,@@
Herschel Supply Co. Settlement Backpack,150,10,7,June,July,August,@@
JBL Free X True Wireless Earbuds,75,5,5,October,November,December,@@
Lululemon Wunder Under Leggings,300,10,12,January,February,March,@@
Nintendo Switch Pro Controller,100,7,5,November,December,January,@@
Patagonia Nano Puff Jacket,75,7,3,November,December,January,@@
Razer DeathAdder V2 Gaming Mouse,20,7,1,November,December,January,@@
Samsung Galaxy Buds Pro,50,5,5,January,February,March,@@
Sennheiser Momentum True Wireless 2 Earbuds,50,5,5,October,November,December,@@
Sony a7 III Mirrorless Camera,10,15,1,June,July,August,@@
The North Face Denali Jacket,100,5,5,November,December,January,@@
UE Wonderboom 2 Waterproof Bluetooth Speaker,100,5,5,July,August,September,@@
Apple AirPods Pro,50,5,5,November,December,January,@@
Bose SoundLink Micro Bluetooth Speaker,75,5,5,July,August,September,@@
Bose SoundTouch 10 Wireless Speaker,50,5,5,November,December,January,@@
Canon EF 50mm f/1.2L USM Lens,10,15,1,October,November,December,@@
Dyson Supersonic Hair Dryer,20,10,2,November,December,January,@@
Garmin Approach S62 Golf GPS Watch,50,5,5,June,July,August,@@
Google Nest Hub (2nd Gen),50,7,2,October,November,December,@@
Herschel Supply Co. Novel Duffle Bag,100,10,5,May,June,July,@@
JBL Quantum 800 Gaming Headset,50,5,5,November,December,January,@@
Lululemon Define Jacket,150,10,7,October,November,December,@@
Microsoft Surface Pro 7,50,10,2,November,December,January,@@
Nike Air Force 1 '07 Sneakers,150,5,8,January,February,March,@@
Oculus Rift S VR Headset,20,15,1,November,December,January,@@
Samsung Galaxy Tab S7+,50,15,2,October,November,December,@@
Anker PowerCore 10000 Portable Charger,100,5,10,July,August,September,@@
Apple MacBook Air,25,10,2,November,December,January,@@
Bose QuietComfort 35 II Wireless Headphones,50,5,5,November,December,January,@@
Brooks Ghost 13 Running Shoes,200,7,10,January,February,March,@@
Canon EOS RP Mirrorless Camera,10,15,1,July,August,September,@@
Coleman Sundome 4-Person Tent,50,7,3,May,June,July,@@
DJI Ronin-SC Gimbal Stabilizer,10,15,1,June,July,August,@@
Fjallraven Kanken Backpack,150,10,7,August,September,October,@@
Garmin Forerunner 245 Music GPS Running Watch,50,5,5,June,July,August,@@
Google Pixel 5a 5G,50,7,2,October,November,December,@@
Herschel Supply Co. Little America Backpack,100,10,5,June,July,August,@@
JBL Charge 5 Waterproof Bluetooth Speaker,75,5,5,July,August,September,@@
Lululemon Align Leggings,300,10,12,January,February,March,@@
Nintendo Switch Lite,100,7,5,November,December,January,@@
Patagonia Better Sweater Fleece Jacket,75,7,3,November,December,January,@@
Razer BlackWidow V3 Mechanical Gaming Keyboard,20,7,1,November,December,January,@@
Samsung Galaxy Watch3,50,5,5,October,November,December,@@
Sennheiser HD 660 S Headphones,20,7,1,November,December,January,@@
Sony a6600 Mirrorless Camera,10,15,1,June,July,August,@@
The North Face Resolve Jacket,100,5,5,May,June,July,@@
UE BOOM 3 Portable Bluetooth Speaker,100,5,5,July,August,September,@@
Apple iPhone 12 Pro Max,25,7,2,November,December,January,@@
Bose SoundLink Around-Ear Wireless Headphones II,50,5,5,October,November,December,@@
Bose SoundTouch 20 Wireless Speaker,50,5,5,November,December,January,@@
Canon EF 70-200mm f/2.8L IS III USM Lens,10,15,1,October,November,December,@@
Dyson Cyclone V10 Absolute Cordless Vacuum,20,10,2,November,December,January,@@
Garmin fenix 6 Sapphire GPS Watch,50,5,5,June,July,August,@@
Herschel Supply Co. Heritage Backpack,150,10,7,May,June,July,@@
JBL Flip 5 Waterproof Bluetooth Speaker,75,5,5,July,August,September,@@
Lululemon Swiftly Tech Short Sleeve Shirt,200,7,10,May,June,July,@@
Microsoft Xbox Series X,25,7,2,November,December,January,@@
Nike Air Zoom Pegasus 38 Running Shoes,200,7,10,January,February,March,@@
Oculus Quest 2 VR Headset,20,15,1,November,December,January,@@
Sony WH-1000XM4 Wireless Headphones,50,5,5,November,December,January,@@
The North Face Campshire Pullover Fleece,75,7,3,November,December,January,@@
Apple iPad Air,25,10,2,November,December,January,@@
Bose SoundLink Mini II Bluetooth Speaker,50,5,5,November,December,January,@@
Brooks Adrenaline GTS 21 Running Shoes,200,7,10,January,February,March,@@
Canon EOS R6 Mirrorless Camera,10,15,1,June,July,August,@@
Coleman Gas Camping Stove,30,10,1,May,June,July,@@
DJI Mavic 2 Pro Drone,10,15,1,June,July,August,@@
Fjallraven Kanken Laptop Backpack,150,10,7,August,September,October,@@
Garmin Venu 2 GPS Smartwatch,50,5,5,June,July,August,@@
Google Nest Audio Smart Speaker,50,5,5,November,December,January,@@
Herschel Supply Co. Retreat Backpack,100,10,5,May,June,July,@@
JBL Xtreme 3 Portable Bluetooth Speaker,75,5,5,July,August,September,@@
Lululemon In Movement Leggings,300,10,12,January,February,March,@@
Nintendo Switch OLED Model,25,7,2,October,November,December,@@
Patagonia Retro Pile Fleece Jacket,75,7,3,November,December,January,@@
Razer DeathAdder V2 Gaming Mouse,20,7,1,November,December,January,@@
Samsung Galaxy Tab S7 FE,25,10,2,November,December,January,@@
Sennheiser Momentum True Wireless 2 Earbuds,50,5,5,November,December,January,@@
Sony WH-CH710N Noise Cancelling Headphones,50,5,5,November,December,January,@@
The North Face Osito Jacket,100,5,5,November,December,January,@@
UE HYPERBOOM Portable Bluetooth Speaker,50,5,5,November,December,January,@@
Apple iPhone SE (2020),50,7,2,May,June,July,@@
Bose SoundSport Free Wireless Earbuds,50,5,5,November,December,January,@@
Canon EOS Rebel T8i DSLR Camera,10,15,1,June,July,August,@@
Dyson V11 Torque Drive Cordless Vacuum,20,10,2,November,December,January,@@
Garmin Instinct Solar GPS Smartwatch,50,5,5,June,July,August,@@
Herschel Supply Co. Settlement Backpack,150,10,7,June,July,August,@@
JBL Charge 4 Waterproof Bluetooth Speaker,75,5,5,July,August,September,@@
Lululemon Define Jacket,100,5,5,November,December,January,@@
Microsoft Surface Laptop 4,25,10,2,November,December,January,@@
Nike React Infinity Run Flyknit 2 Running Shoes,200,7,10,January,February,March,@@
Oculus Rift S VR Headset,20,15,1,November,December,January,@@
Samsung Galaxy Buds Pro Earbuds,50,5,5,November,December,January,@@
Sony Alpha a7 III Mirrorless Camera,10,15,1,June,July,August,@@
The North Face Women's Arctic Parka,75,7,3,November,December,January,@@
Apple AirPods Pro,50,5,5,November,December,January,@@
Bose QuietComfort Earbuds,50,5,5,November,December,January,@@
Brooks Ghost 13 Running Shoes,200,7,10,January,February,March,@@
Canon EOS 5D Mark IV DSLR Camera,10,15,1,June,July,August,@@
Coleman 8-Person Camping Tent,20,10,2,May,June,July,@@
DJI Osmo Action Camera,10,15,1,June,July,August,@@
Fjallraven Kanken Classic Backpack,200,10,10,July,August,September,@@
Garmin Forerunner 945 GPS Smartwatch,50,5,5,June,July,August,@@
Google Pixel 6 Smartphone,25,7,2,October,November,December,@@
Herschel Supply Co. Nova Backpack,150,10,7,June,July,August,@@
JBL Flip 5 Waterproof Bluetooth Speaker,75,5,5,July,August,September,@@
Lululemon Align Leggings,300,10,12,January,February,March,@@
Nintendo Switch Pro Controller,50,7,2,October,November,December,@@
Patagonia Nano Puff Jacket,75,7,3,November,December,January,@@
Razer BlackWidow V3 Gaming Keyboard,20,7,1,November,December,January,@@
Samsung Galaxy Watch 4 Classic,25,10,2,November,December,January,@@
Sennheiser HD 660 S Headphones,50,5,5,November,December,January,@@
Sony SRS-XB33 Portable Bluetooth Speaker,50,5,5,November,December,January,@@
The North Face Women's Metropolis Parka,75,7,3,November,December,January,@@
UE WONDERBOOM 2 Waterproof Bluetooth Speaker,50,5,5,November,December,January,@@
Apple Watch Series 7,50,5,5,November,December,January,@@
Bose QuietComfort 35 II Headphones,50,5,5,November,December,January,@@
Canon EOS M50 Mark II Mirrorless Camera,10,15,1,June,July,August,@@
Dyson Airwrap Complete Styler,20,10,2,November,December,January,@@
Garmin fenix 6X Pro Solar GPS Smartwatch,50,5,5,June,July,August,@@
Herschel Supply Co. Little America Backpack,150,10,7,May,June,July,@@
JBL Live 650BTNC Noise Cancelling Headphones,50,5,5,November,December,January,@@
Lululemon Wunder Under Leggings,300,10,12,January,February,March,@@
Microsoft Surface Pro 8,25,10,2,November,December,January,@@
Nike Air Zoom Pegasus 38 Running Shoes,200,7,10,January,February,March,@@
Oculus Quest 2 VR Headset,20,15,1,November,December,January,@@
Samsung Galaxy S21 Ultra Smartphone,25,7,2,May,June,July,@@
Apple MacBook Pro (16-inch),25,10,2,November,December,January,@@
Bose QuietComfort 35 II Headphones,50,5,5,November,December,January,@@
Canon EOS 90D DSLR Camera,10,15,1,June,July,August,@@
DJI Ronin-S Gimbal Stabilizer,10,15,1,June,July,August,@@
Fjallraven Kanken Mini Backpack,100,10,5,May,June,July,@@
Garmin Forerunner 245 Music Smartwatch,50,5,5,June,July,August,@@
GoPro HERO9 Black Action Camera,10,15,1,June,July,August,@@
Herschel Supply Co. Little America Backpack,150,10,7,May,June,July,@@
JBL Charge 5 Portable Bluetooth Speaker,75,5,5,July,August,September,@@
Lululemon Align Tank Top,300,10,12,January,February,March,@@
Microsoft Surface Pro 7,25,10,2,November,December,January,@@
Nintendo Switch Pro Controller,50,7,2,October,November,December,@@
Patagonia Nano Puff Jacket,75,7,3,November,December,January,@@
Razer BlackWidow Elite Mechanical Keyboard,20,7,1,November,December,January,@@
Samsung Galaxy Buds Pro Earbuds,50,5,5,November,December,January,@@
Sennheiser HD 650 Headphones,50,5,5,November,December,January,@@
Sony a6400 Mirrorless Camera,10,15,1,June,July,August,@@
The North Face Women's Gotham Jacket,75,7,3,November,December,January,@@
UE HYPERBOOM Portable Bluetooth Speaker,50,5,5,November,December,January,@@
Apple Watch Series 6,50,5,5,November,December,January,@@
Bose SoundSport Wireless Earbuds,50,5,5,November,December,January,@@
Canon EOS Rebel T7i DSLR Camera,10,15,1,June,July,August,@@
Dyson V11 Outsize Cordless Vacuum,20,10,2,November,December,January,@@
Garmin fenix 6 Pro GPS Smartwatch,50,5,5,June,July,August,@@
Herschel Supply Co. Nova Backpack,150,10,7,June,July,August,@@
JBL LIVE 500BT Wireless Headphones,50,5,5,November,December,January,@@
Lululemon Invigorate High-Rise Tight,200,7,10,January,February,March,@@
Microsoft Xbox Series S,25,7,2,November,December,January,@@
Nike Air Zoom Structure 23 Running Shoes,200,7,10,January,February,March,@@
Oculus Rift S PC-Powered VR Gaming Headset,20,15,1,November,December,January,@@
Samsung Galaxy S20 FE Smartphone,25,7,2,May,June,July,@@
Sony WF-1000XM4 Wireless Earbuds,50,5,5,November,December,January,@@
The North Face Men's Venture 2 Jacket,100,5,5,November,December,January,@@"""


# Read from csv file
def readFromcsvFile():
    with open('../dataset/initialData.csv', 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        stringResult = ""

        # Read each row of the CSV file
        for index, row in enumerate(reader):
            # Check if the row index is greater than 0 and add @@ if it doesn't contain.
            if index > 0 and not row.__contains__('@@'):
                row.append("@@")
            for column in row:
                stringResult += column + ","
            stringResult += "\n"
    return stringResult


def unique_dataAndWriteToCSV(string_values):
    string_splitted = string_values.split("@@")

    # String splitted removes the trailing white space
    # at the end of the list.
    string_splitted.pop()

    parse_to_list_of_objects = []

    for item in string_splitted:

        # Split each item in the array.
        splitted_item = item.split(",")

        # String splitted removes the trailing white space
        # at the end of the list of each item.
        splitted_item.pop()

        parse_to_list_of_objects.append(splitted_item)

    # Remove duplicates from the list of items.
    result = uniq_by(parse_to_list_of_objects, lambda item: item[0])

    # Specify the output CSV file path
    output_file = '../dataset/cleanedDataUsingPython.csv'

    # Open the file in write mode
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Product Name", "Current Inventory Level",	"Lead Time (in days)",	"Sales Velocity (in units per day)", "Highest Sales Months"
                         ])
        writer.writerows(result)


unique_dataAndWriteToCSV(stringValues)
# print(readFromcsvFile())


# TO DO
# Tweak these functions so as it compliments each other and we can accept
# csv file instead of hardcoding string value.
