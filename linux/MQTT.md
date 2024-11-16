# Command Publish and Subscribe MQTT

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


## Let us start Subscriber now - topic name => 'hello/topic'
```
# Without authentication
mosquitto_sub -v -t 'hello/topic'

# With authentication
mosquitto_sub -v -t 'hello/topic' -u user1 -P <password>

# Alternate way in url format
# Format => mqtt(s)://[username[:password]@]host[:port]/topic
mosquitto_sub -v -L mqtt://user1:abc123@localhost/test/topic

```

## Let us start Publising to that topic
```
# Without authentication
mosquitto_pub -t 'hello/topic' -m 'hello MQTT'

# With authentication
mosquitto_pub -t 'hello/topic' -m 'hello MQTT' -u user1 -P <password>

# Alternate way in url format 
# Format => mqtt(s)://[username[:password]@]host[:port]/topic
mosquitto_pub -L mqtt://user1:abc123@localhost/test/topic -m 'hello MQTT'

```