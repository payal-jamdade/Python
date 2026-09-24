logging_profile = ("192.168.1.100", 8080)

print("System Logging Profile:")
print("IP Address:", logging_profile[0])
print("Server Port:", logging_profile[1])

ip_address, server_port = logging_profile

print("\nUsing Tuple Unpacking:")
print("IP Address:", ip_address)
print("Server Port:", server_port)

print("\nAttempting to modify the logging profile...")

try:
    logging_profile[0] = "10.0.0.1"
except TypeError:
    print("Modification failed!")
    print("Tuple is immutable and cannot be changed at runtime.")

try:
    logging_profile[1] = 9090
except TypeError:
    print("Modification failed!")
    print("Server port remains unchanged.")

print("\nFinal Logging Profile:")
print("IP Address:", logging_profile[0])
print("Server Port:", logging_profile[1])