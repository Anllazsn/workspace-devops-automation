cpu = 73

if cpu >= 90:
    status = "CRITICAL"
elif cpu >= 70:
    status = "HIGH"
else:
    status ="OK"

print(f"CPU {cpu}% | Status {status}")

mem = 82
if cpu >= 70 and mem >= 80:
    print("Warning: High CPU and Memory usge")
else:
    print("Resources within expected range")
