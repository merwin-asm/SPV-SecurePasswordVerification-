# SPV SecurePasswordVerification


Its is python module for doing a secure password  verification without sharing the password directly.



## Features

- The password is never sent in the process.
- Its more secure.


## Usage/Examples

spv.GetVerified(password)

Used by a Client to GetVerified by a Server.

```
spv = SPV.SPV(client_sock)

spv.GetVerified("real_password")  #returns True if Verified.
```

spv.Verify(password)

Used by a Server to Verify a Client.
```
client, address = server.accept()

spv = SPV.SPV(server)

spv.Verify("real_password",client)  #returns True if Verified.
```
