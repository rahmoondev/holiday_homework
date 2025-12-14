#​12. Port Scanner Simulator
# ​Goal: Write a function that takes a list of ports (numbers) and checks if they are "open" or "closed" (e.g., port 80 is open, 22 is open, 1000 is closed). Crucially: He should NOT actually check the network. The program should just simulate it by using a predefined list of "open" ports (e.g., [21, 22, 80, 443]).
# Concepts: Lists, loops, conditional checks, simulating real-world functions.
def port_scanner_simulator(ports):
    open_ports = [21, 22,23,68, 80, 443]
    results= {}
    for port in ports:
        if port in open_ports:
            results[port] = "open"
        else:
            results[port] = "closed"
    return results

if __name__ == "__main__":
    check = input("input coma separated ports: ")
    check = [int(port.strip()) for port in check.split(",")]
    scan_resualts = port_scanner_simulator(check)
    for port, status in scan_resualts.items():
        print(f"port {port} is {status}")
        
               