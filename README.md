# SPV SecurePasswordVerification


<p align="right"> <img src="https://komarev.com/ghpvc/?username=meriwn-SPV&label=Project%20views&color=0e75b6&style=flat" alt="darkmash-org" /> </p>


[![Downloads](https://static.pepy.tech/badge/spv)](https://pepy.tech/project/spv)




Its is python module for doing a secure password  verification without sharing the password directly.


## Install

      
      pip install SPV


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
