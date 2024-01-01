# Password Manager
This simple password manager is created using Python and incorporates the SHA-256 hashing algorithm for secure password storage. The program allows users to create an account, log in and exit. 

## Features
* __Account Creation:__ Users can create an account by providing a username and password. The password is securely hashed using the SHA-256 algorithm before being stored in the passwordManager dictionary.

* __Login:__ Users can log in by entering their username and password. The entered password is hashed, and the program checks if it matches the stored hashed password for the given username. This will give either a successful login message, or an error if there is no match.

* __Security:__ The SHA-256 hashing algorithm is employed to convert plain-text passwords into fixed-size, secure hash values. This provides a level of security by making it computationally infeasible to reverse the hashing process and retrieve the original password. I have included a print statement that appears alongside a successful login message to prove the hashing of the password.

## Libraries
* __hashlib:__ to perform the SHA-256 hashing.
* __getpass:__ to securely input passwords without displaying them on the screen.

![image](https://github.com/kxvassiliou0/passwordmanager/assets/34982747/eadb133a-ee34-47af-a408-419efd4ba95a)

_A screenshot showing the program output, if the user decided that their username would be 'user1' and their password 'pass1'._
