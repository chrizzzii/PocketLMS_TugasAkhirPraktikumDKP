import random

class sistemLogin:
    def __init__(self, email, password):
        self.email = email 
        self.password = password
        self.data = {
            "Tito" : {
                "nama"      : "Agustinus Adven Christo",
                "email" 	: "Tito@undip.com",
                "password"  : "1234",
                "level"     : "17",
                "role"  	: "Kelas 12",
        	}
    	}
		
    def checkCredentials(self):
    	for value in self.data:
        	if value == self.email:
                    get_data_user = self.data[value]
                    if self.password == get_data_user['password']:
                        return get_data_user
                    else:
                        return False
	
    def ceklogin(self):
        get_data = self.checkCredentials()
        if get_data:
            print("\nWelcome ", get_data['nama'])
            print("Logged in as email:", get_data['email'])
            return True
        else:
            print("\nLogin Gagal!\n")
            return False

    def datapengguna(self):
        get_profil = self.checkCredentials()
        print("Nama  : ", get_profil['nama'])
        print("Kelas : ", get_profil['role'])
        print("Level : ", get_profil['level'])

                      