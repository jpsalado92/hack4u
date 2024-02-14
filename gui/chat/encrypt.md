
# Encrypt

## Generate a key

The following command will generate a key with the RSA algorithm and will encrypt it
with the AES256 algorithm. The key will be stored in the file `server-key.key`.

```bash
openssl genpkey -algorithm RSA -out server-key.key -aes256
```

## Generate a certificate signing request

This command will generate a certificate signing request using the key generated
in the previous step. The request will be stored in the file `server.csr`.

```bash
openssl req -new -key server-key.key -out server.csr
```

## Generate a self-signed certificate

This command will generate a self-signed certificate using the key generated in the
first step and the certificate signing request generated in the previous step.
The certificate will be stored in the file `server-cert.pem` and will be valid for 365 days.

This is done so that the server can use the certificate to encrypt the communication.

```bash
openssl x509 -req -days 365 -in server.csr -signkey server-key.key -out server-cert.pem
```

## Decrypt the key

This command will decrypt the key generated in the first step and will store it in the same file.

This is done so that the key can be used in the server without having to enter a password.

```bash
openssl rsa -in server-key.key -out server-key.key
```
