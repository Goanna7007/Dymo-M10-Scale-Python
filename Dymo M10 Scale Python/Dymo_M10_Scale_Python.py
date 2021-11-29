# This is a simple script for handeling inputs of the 
# DYMO M10 digital scale for Windows over USB

# open source
# Author: Johannes Nicholas, github: https://github.com/Goanna7007


import pywinusb.hid as hid



def dymo_scale_handler(data):
    weight

    if data[1] == 2: #if zeroed
        weight = 0
    else:
        weight = data[4] + data[5] * 255    #get weight

        if data[1] == 5:    #if negative, flip over 0
            weight *= -1

        if data[2] == 11:   #if in OZ, convert to KG
            weight = int((weight * 2.834952))

    weight = weight - tare;
    weight_text.set(str(weight) + "g")


def get_dymo_scale():
    all_hids = hid.find_all_hid_devices()
    for device in all_hids:
        if ((device.product_id == 0x8003) and (device.vendor_id == 0x0922)):
            return device
    return None

def setup_dymo_scale():
    global device
    device = get_dymo_scale()
    if device:
        try:
            device.open()
            device.set_raw_data_handler(dymo_scale_handler)
            dymo_check_loop()
        finally:
            None
    else:
        weight_text.set("connect and turn on scale")
        root.after(100, setup_dymo_scale)  # reschedule event in 2 seconds

def dymo_check_loop():
    global device
    if device.is_plugged():
        root.after(1000, dymo_check_loop)# reschedule event in 2 seconds
    else:
        device.close()
        device = None
        setup_dymo_scale()


if __name__ == '__main__':
    setup_dymo_scale()