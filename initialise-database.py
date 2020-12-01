# Use this code to initialise the delivery_logger table once we move to KQ's database
# cursor.execute("CREATE TABLE delivery_logger ("
#                "company_name VARCHAR(255),"
#                "time_in DATETIME,"
#                "time_out DATETIME,"
#                "parking_location ENUM('street', 'restricted'),"
#                "delay ENUM('none', 'small', 'medium', 'large'),"
#                "bound ENUM('inbound', 'outbound'),"
#                "carrier_name VARCHAR(255),"
#                "vehicle_type ENUM('pedestrian', 'bicycle', 'motorbike', 'car', 'van', 'lorry'),"
#                "vehicle_registration_number VARCHAR(7),"
#                "fuel ENUM('petrol', 'diesel', 'electric', 'hybrid'),"
#                "vehicle_origin VARCHAR(255),"
#                "previous_locations INT(255),"
#                "following_locations INT(255),"
#                "personal_delivery BOOL,"
#                "department VARCHAR(255),"
#                "number_suppliers INT(255),"
#                "type ENUM('medical', 'office', 'catering'),"
#                "size ENUM('box', 'letter', 'package', 'pallet'))")
#
# cnxn.commit()
