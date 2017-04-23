import os, csv


def highest_share_price(f_path):

    result = {}

    try:
        f = open(f_path, 'r')

        # Convert csv file content in dictionary format
        file_reader_object = csv.DictReader(f)

        for dict_object in file_reader_object:
            # print dict_object
            # {'Wipro': '978', 'IndiGo': '79', 'BankBazaar': '443', 'MphasiS': '896', 'Year': '1990','Month': 'January', 'IDFC': '568', 'GAIL': '543', 'Infosys': '355', 'Flipkart': '355', 'Snapdeal': '848', 'CEAT': '671'}

            for key in dict_object.keys():
                # print key # Year
                            # Month
                            # IDFC
                            # CEAT
                            # GAIL
                            # Flipkart
                            # IndiGo
                            # Infosys
                            # Snapdeal
                            # Wipro
                            # MphasiS
                            # BankBazaar

                # Check if key is neither 'Year'nor 'Month'
                if key not in ('Year', 'Month'):

                    # If key is not present in result dictionary then add it with empty dictionary as value
                    if key not in result:
                        result[key] = {}
                        #print result # {'Wipro': {}, 'IndiGo': {}, 'BankBazaar': {}, 'MphasiS': {}, 'IDFC': {}, 'GAIL': {}, 'Infosys': {}, 'CEAT': {}, 'Snapdeal': {}, 'Flipkart': {}}

                    if 'Year' and 'Month' and 'Price' not in result[key]:
                        result[key]['Year'] = dict_object['Year']
                        result[key]['Month'] = dict_object['Month']
                        result[key]['Price'] = dict_object[key]

                    else:
                        if result[key]['Price'] < dict_object[key]:
                            result[key]['Year'] = dict_object['Year']
                            result[key]['Month'] = dict_object['Month']
                            result[key]['Price'] = dict_object[key]

        # print result
        # {'Wipro': {'Price': '998', 'Month': 'June', 'Year': '1995'}, 'IndiGo': {'Price': '999', 'Month': 'March', 'Year': '1990'}, 'BankBazaar': {'Price': '996', 'Month': 'September', 'Year': '2016'}, 'MphasiS': {'Price': '997', 'Month': 'August', 'Year': '1992'}, 'IDFC': {'Price': '999', 'Month': 'April', 'Year': '1991'}, 'GAIL': {'Price': '996', 'Month': 'November', 'Year': '1998'}, 'Infosys': {'Price': '998', 'Month': 'July', 'Year': '1996'}, 'CEAT': {'Price': '997', 'Month': 'August', 'Year': '2006'}, 'Snapdeal': {'Price': '998', 'Month': 'April', 'Year': '1990'}, 'Flipkart': {'Price': '996', 'Month': 'February', 'Year': '2013'}}

    except IOError:
        print "Oops! File doesn't exist."

    return result


if __name__ == '__main__':
    f_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'share_prices.csv')
    response = highest_share_price(f_path)

    for data in response:
        print "In %s %s, %s has the highest share price of Rs.%s" % (response[data]['Month'], str(response[data]['Year']), data, response[data]['Price'])