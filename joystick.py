from inputs import get_gamepad, devices
#from dmx import senddmx

# https://pypi.org/project/DMXEnttecPro/
# https://github.com/YoshiRi/PyDMX

# Print available devices:
for device in devices:
    print("Devices: ", device)

#dmxdata = [chr(0)] * 513

def main():
    x = 127
    y = 127

    last_x = 0
    last_y = 0

    threshold = 5
    while True:
        events = get_gamepad()
        for event in events:
            if event.code == "ABS_X":
                #if last_x == 0:
                #    last_x = event.state
                #if event.state > last_x:
                #print("X:", event.state)

                if int(255/2) - threshold <= event.state <= int(255/2) + threshold:
                    print("Stick in center.")

                elif event.state > int(255/2) + threshold:
                    if x != 255:
                        x += 1
                        print("x", x)
                elif event.state < int(255 / 2) - threshold:
                    if x != 0:
                        x -= 1
                        print("x", x)

                #dmxdata = senddmx(dmxdata, 1, event.state)
            #elif event.code == "ABS_Y":
                #print("Y: ", event.state)

                #dmxdata = senddmx(dmxdata, 2, event.state)


if __name__ == "__main__":
    main()