# Tshark: Man in the middle

## Intercept messages

```bash
tshark -i lo -Tfields -e data.data port 12345
```

## Read the messages

```bash
echo "<InterceptedMessage>" | xxd -ps -r
```

<!-- ## Intercept messages encrypted with SSL and read them provided a private key

Given our private key at server-cert.pem, we can read the messages intercepted with the following command:

```bash
tshark -i lo -Tjson port 12345
#  "17:03:03:00:15:47:04:43:d5:e8:f6:9c:7f:bc:3b:dd:80:09:e7:36:81:d0:4b:67:26:fc"
<InterceptedMessage>
echo "<InterceptedMessage>" | tr -d ":" | xxd -pd -r | openssl pkeyutl -decrypt -inkey server-cert.pem
``` -->
