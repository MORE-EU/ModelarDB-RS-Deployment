FROM ubuntu:latest

COPY mqttstreamer .
COPY data/ISO-NE_case2.csv .

CMD ["./mqttstreamer", "--debug", "true", "--csvFile", "ISO-NE_case2.csv", "--csvRows", "1", "--csvCols", "3", "--csvHeaders", "4", "--csvRate", "100", "--csvInLoop", "true", "--qos", "1", "--broker", "tcp://mosquitto:1883",  "--csvEpoch", "1701856549808"]
