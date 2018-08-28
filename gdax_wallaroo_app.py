import struct
import wallaroo

# Use Rachels approach in adtech.py
def application_setup(args):
    in_host, in_port = wallaroo.tcp_parse_input_addrs(args)[0]
    out_host, out_port = wallaroo.tcp_parse_output_addrs(args)[0]
    ab = wallaroo.ApplicationBuilder("gdax alerts")
    # Pipeline to store alerts and the corresponding user
    # Pipeline to calculate current bitcoin price from gdax


    # State object, current_price
    # Update the moving

    # Alerts are map of `price: [user_ids]`
    # Alert.update lookup users, return and replace with None
    # Send to another application, that then calls a cellery task
    ab.to_sink(wallaroo.TCPSinkConfig(out_host, out_port, encoder))

@wallaroo.encoder
def encoder(data):
    output = json.dumps(c, default=lambda o: o.__dict__)
    payload = bytes(output)
    return struct.pack(">I",len(payload)) + payload
