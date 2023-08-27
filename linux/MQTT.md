# MQTT

## contoh subscribe dan publish pada CMD windows
- buat cmd dan masuk ke direktori `"C:\Program Files\mosquitto"`

- subscribe (pendengar)
    ```
    mosquitto_sub -t test_sensor -h localhost
    ```
- publish (pengirim)
    ```
    mosquitto_pub -t test_sensor -h localhost -m "temp:230"
    ```    